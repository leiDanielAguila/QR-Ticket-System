# events router
from fastapi import APIRouter, Depends
from app.models.events import Event_DB
from app.schemas.events import Event
from sqlalchemy.orm import Session

from app.dependencies import get_db

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
async def get_events(db: Session = Depends(get_db)):
    return db.query(Event_DB).all()


@router.post("/")
async def create_event(event: Event, db: Session = Depends(get_db)):
    new_event = Event_DB(
        event_name=event.event_name,
        event_date=event.date,
        venue=event.venue,
        guest_count=event.guest_count,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event
