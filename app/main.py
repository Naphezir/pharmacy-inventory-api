from fastapi import FastAPI

from app.api.routes.health import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(router)


# to run use: uv run uvicorn name-of-main-file:name-of-app --reload (reloads after change in file)
# e.g. here:  uv run uvicorn app.main:app --reload
# (uv run pomaga użyć właściwych wersji zależności)
