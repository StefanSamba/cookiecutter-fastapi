from app.api.v1.endpoints import {{cookiecutter.endpoint_name}}
from fastapi import APIRouter

v1_router = APIRouter()
v1_router.include_router(
    {{cookiecutter.endpoint_name}}.router,
    prefix="/v1",
)
