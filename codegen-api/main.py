from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import generate_main_tf
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
        services.append({
            "type": "managed_postgres_db",
            "params": {
                "db_identifier": db_identifier,
                "instance_class": "db.t3.medium",
                "username": "admin",
                "password": "secret"
            }
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
