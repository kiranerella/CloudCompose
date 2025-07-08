from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import generate_main_tf
import json
# optionally: from utils import commit_and_push

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
        params = {}
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
                "resource_group_name": "my-resource-group",  # Could be dynamic
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
                "project_id": "my-gcp-project",  # Could be dynamic
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


    user_input = {
        "cloud": cloud,
        "project_name": project_name,
        "services": services
    }

    tf_code = generate_main_tf(user_input)

    # Optionally:
    # commit_and_push(os.getcwd(), "infra", f"feat: add {service_type} on {cloud}")

    return templates.TemplateResponse("result.html", {"request": request, "tf_code": tf_code})

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

pricing = load_json("pricing.json")
regions = load_json("regions.json")
