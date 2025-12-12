from sqlalchemy.orm import Session
from app.dependencies import get_db
from fastapi import APIRouter, Depends
from typing import Optional
from app.dependencies import get_db

router = APIRouter(prefix="/organizers", tags=["organizers"])

@router.get("/")
async def get_organizers(organizer_name: Optional[str] = None, db: Session = Depends(get_db)):
    pass


@router.post("/")
async def create_organizer():
    pass


@router.delete("/")
async def delete_organizer():
    pass


