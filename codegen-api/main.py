from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_main_tf

app = FastAPI()

class ServiceParams(BaseModel):
    type: str
    params: dict

class BlueprintRequest(BaseModel):
    cloud: str
    project_name: str
    services: list[ServiceParams]

@app.post("/generate")
def generate(req: BlueprintRequest):
    user_input = req.dict()
    result = generate_main_tf(user_input)
    return result
