from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from cloudpricing import get_aws_price, get_azure_price, get_gcp_price
from utils import generate_main_tf
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load static data once at startup
regions = json.load(open("regions.json"))
with open("mapping.json") as f:
    service_map = json.load(f)

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def form_post(
    request: Request,
    primary_cloud: str = Form(...),
    include_clouds: list[str] = Form(None),
    services: list[str] = Form(None),
    offhours: str = Form(None),
    project_name: str = Form(...)
):
    """
    Main handler:
    - builds multi-cloud service plan based on user's selections
    - maps to equivalent services across clouds
    - calculates cost
    - generates terraform code per cloud
    """

    all_clouds = set(include_clouds or [])
    all_clouds.add(primary_cloud)  # ensure primary always included

    # Build a dict: {cloud: [services...]}
    multi_cloud_plan = {}

    for cloud in all_clouds:
        cloud_services = []
        for svc in services:
            module_path = service_map.get(svc, {}).get(cloud)
            if module_path:
                # Add params as needed; here simplified
                cloud_services.append({
                    "type": svc,
                    "module": module_path,
                    "params": {"project_name": project_name}
                })
        # Off‑hours scheduler as extra service
        if offhours == "yes":
            cloud_services.append({
                "type": "scheduler",
                "module": f"service-catalog/{cloud}/scheduler",
                "params": {"enabled": True}
            })
        multi_cloud_plan[cloud] = cloud_services

    # Cost & default region per cloud
    cost_per_cloud = {}
    default_regions = {}
    for cloud, svc_list in multi_cloud_plan.items():
        est_cost = 0.0
        for s in svc_list:
            if cloud == "aws":
                est_cost += get_aws_price(s["type"])
            elif cloud == "azure":
                est_cost += get_azure_price(s["type"])
            elif cloud == "gcp":
                est_cost += get_gcp_price(s["type"])
        cost_per_cloud[cloud] = est_cost
        default_regions[cloud] = regions[cloud][0]

    # Generate terraform code per cloud
    tf_outputs = {}
    for cloud, svc_list in multi_cloud_plan.items():
        user_input = {
            "cloud": cloud,
            "project_name": project_name,
            "services": svc_list
        }
        tf_code = generate_main_tf(user_input)
        tf_outputs[cloud] = tf_code

        # Save to generated/{cloud}/main.tf (optional)
        out_path = f"generated/{cloud}/main.tf"
        with open(out_path, "w") as f:
            f.write(tf_code)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "tf_outputs": tf_outputs,
        "cost_per_cloud": cost_per_cloud,
        "default_regions": default_regions
    })
