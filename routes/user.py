from fastapi import APIRouter
from models.models import User

router = APIRouter()

@router.get("/profile", tags=["User"])
async def get_profile():
    pass