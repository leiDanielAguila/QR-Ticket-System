# database models for guests
from sqlalchemy import Column, Integer, String, ForeignKey, Uuid
from app.utils.database import Base
from sqlalchemy.orm import relationship

class Guest_DB(Base):
    __tablename__ = "guest"
    id = Column(Uuid, primary_key=True)
    guest_name = Column(String, index=True)
    email = Column(String, index=True)
    event_id = Column(Integer, ForeignKey("events.id"),index=True)

    events = relationship("Event_DB", back_populates="guests")