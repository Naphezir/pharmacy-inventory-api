from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Health"])
async def root():
    return {
            "message": "Pharmacy Inventory API",
            "status": "running"
            }
