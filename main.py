from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Event, Event_DB
from database import engine, Base
from dependencies import get_db
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

name = 'lei'


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def greet():
    return {"Welcome": "Ticketing system"}

@app.post("/api/event/")
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