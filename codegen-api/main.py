from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import generate_main_tf
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load once at startup:
pricing = json.load(open("pricing.json"))
regions = json.load(open("regions.json"))

@app.post("/generate", response_class=HTMLResponse)
def form_post(
    request: Request,
    cloud: str = Form(...),
    project_name: str = Form(...),
    service_type: str = Form(...),
    cluster_name: str = Form(...),
    db_identifier: str = Form(...)
):
    services = []

    if service_type == "container_orchestrator":
        services.append({
            "type": "container_orchestrator",
            "params": { "cluster_name": cluster_name }
        })
    elif service_type == "managed_postgres_db":
        if cloud == "aws":
            params = {
                "db_identifier": db_identifier,
                "instance_class": "db.t3.medium",
                "username": "admin",
                "password": "secret"
            }
        elif cloud == "azure":
            params = {
                "db_name": db_identifier,
                "resource_group_name": "my-resource-group",
                "location": "eastus",
                "admin_username": "admin",
                "admin_password": "secret",
                "sku_name": "GP_Gen5_2",
                "storage_mb": 5120,
                "backup_retention_days": 7,
                "geo_redundant_backup": "Disabled",
                "tags": {"Project": project_name}
            }
        elif cloud == "gcp":
            params = {
                "project_id": "my-gcp-project",
                "db_name": db_identifier,
                "region": "us-central1",
                "tier": "db-custom-1-3840",
                "admin_password": "secret",
                "tags": {"Project": project_name}
            }
        services.append({
            "type": "managed_postgres_db",
            "params": params
        })

    # dynamic cost & region logic block (should add api block for realtime processing ) ***
    est_cost = sum(
        pricing[cloud].get(s["type"], 0)
        for s in services
    )
    default_region = regions[cloud][0]  # e.g., "us-east-1"

    # Generate Terraform code
    user_input = {
        "cloud": cloud,
        "project_name": project_name,
        "services": services
    }
    tf_code = generate_main_tf(user_input)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "tf_code": tf_code,
        "est_cost": est_cost,
        "default_region": default_region
    })
