# pydantic models for events
from pydantic import BaseModel

class Event(BaseModel):
    event_name: str
    date: str
    venue: str
    guest_count: int