from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

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