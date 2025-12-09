# guests router
from fastapi import APIRouter, Depends
from app.models.guests import Guest_DB
from app.schemas.guests import Guest
from services import generate_id
from sqlalchemy.orm import Session

from app.dependencies import get_db

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.get("/")
async def get_guests(db: Session = Depends(get_db)):
    return db.query(Guest_DB).all()


@router.post("/")
async def create_guest(guest: Guest, db: Session = Depends(get_db)):
    guest_id = generate_id()

    new_guest = Guest_DB(
        id = guest_id,
        guest_name = guest.guest_name,
        email = guest.email,
        event_id = guest.event_id
    )
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest