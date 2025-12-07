from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Event(BaseModel):
    event_name: str
    date: str
    venue: str
    guest_count: int
    
    
class Event_DB(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    event_date = Column(String, index=True)
    venue = Column(String, index=True)
    guest_count = Column(Integer, index=True)

    guests = relationship("Guest_DB", back_populates="events")


class Guest(BaseModel):
    id: int
    guest_name: str
    email: str
    event_id: int


class Guest_DB(Base):
    __tablename__ = "guest"
    id = Column(Integer, primary_key=True)
    guest_name = Column(String, index=True)
    email = Column(String, index=True)
    event_id = Column(Integer, ForeignKey("events.id"),index=True)

    events = relationship("Event_DB", back_populates="guests")
