from fastapi import FastAPI
from app.api.routes.health import router

app = FastAPI(
    title="Pharmacy Inventory API",
    version="0.1.0",
    description="Backend API for pharmacy inventory management.",
)

app.include_router(router)


# to run use: uv run uvicorn name-of-main-file:name-of-app --reload (reloads after change in file)
# e.g. here:  uv run uvicorn app.main:app --reload
# (uv run pomaga użyć właściwych wersji zależności)
