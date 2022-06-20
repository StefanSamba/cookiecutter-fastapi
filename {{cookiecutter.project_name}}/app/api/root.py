from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
def read_root():
    return {"About": "{{cookiecutter.project_name}} API"}


@root_router.get("/healthz")
def get_healthz():
    """To check the service health"""
    return {"status": "ok"}
