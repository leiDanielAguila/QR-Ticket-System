# database model for organizer

from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.database import Base
from sqlalchemy.orm import relationship

class Organizer_DB(Base):
    __tablename__ = "organizer"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    email = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    
    user = relationship("User_DB", back_populates="organizer")