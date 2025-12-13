# pydantic schema for organizers
from pydantic import BaseModel, Field


class Organizers(BaseModel):
    email: str = Field(min_length=1)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str= Field(min_length=1)