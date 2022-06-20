from app.api.root import root_router
from app.api.v1.api import v1_router
from app.core.config import get_application

app = get_application()
app.include_router(root_router, tags=["Default"])
app.include_router(v1_router, tags=["V1"])
