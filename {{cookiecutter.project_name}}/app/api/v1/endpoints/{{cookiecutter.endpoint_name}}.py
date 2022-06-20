# Import utils
from app.schemas.schemas import Request
from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.post("/{{cookiecutter.endpoint_name}}")
def {{cookiecutter.endpoint_name}}(request: Request) -> JSONResponse:
    """{{cookiecutter.endpoint_name}} endpoint

    Args:
        request (Request): request with dummy utterances

    Returns:
        dict: a dummy response
    """
    # Add your code here
    # Create some helper function in utils/
    # Use your helper functions by utils.functionname()

    return dict(request)
