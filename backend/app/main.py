from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

api = FastAPI(
    root_path=settings.API_V1_STR,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
)

app.mount(settings.API_V1_STR, api)
