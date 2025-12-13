# pydantic models for events
from pydantic import BaseModel, Field

class Event(BaseModel):
    event_name: str = Field(min_length=3, title="event name should not be empty or less than 3 characters")
    date: str
    venue: str
    guest_count: int = Field(gt=0, title="event can not be empty")