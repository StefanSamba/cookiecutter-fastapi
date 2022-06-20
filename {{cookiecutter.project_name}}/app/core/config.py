from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application():
    _app = FastAPI(title="{{cookiecutter.project_name}}")
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app
