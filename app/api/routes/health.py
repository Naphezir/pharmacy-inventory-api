from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter()


@router.get("/", tags=["Health"])
async def root():
    return {
            "message": "Pharmacy Inventory API",
            "status": "running"
            }


@router.get("/health/db", tags=["Health"])
async def database_health(db: Session = Depends(get_db)) -> dict:
    db.execute(text("SELECT 1"))
    return {"database": "connected", }
