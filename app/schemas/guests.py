# pydantic models for events
from pydantic import BaseModel, Field

class Guest(BaseModel):
    guest_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    event_id: int = Field(gt=0, title="event id should not be 0")
