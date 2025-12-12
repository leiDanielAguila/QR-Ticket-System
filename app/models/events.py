# database models for events
from sqlalchemy import Column, Integer, String
from app.utils.database import Base
from sqlalchemy.orm import relationship

class Event_DB(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    event_date = Column(String, index=True)
    venue = Column(String, index=True)
    guest_count = Column(Integer, index=True)

    guests = relationship("Guest_DB", back_populates="events")