from sqlalchemy.orm import Session
from app.dependencies import get_db
from fastapi import APIRouter, Depends
from typing import Optional
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
async def login(db: Session = Depends(get_db)):
    pass


@router.post("/sign_up")
async def sign_up(db: Session = Depends(get_db)):
    pass





