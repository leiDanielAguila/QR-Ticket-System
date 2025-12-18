# database model for User

from sqlalchemy import Column, Integer, String
from app.utils.database import Base
from sqlalchemy.orm import relationship

class User_DB(Base):
    __tablename__ = "users"
    id = Column(String , index=True, primary_key=True)
    password = Column(String, index=True)
    
    organizer = relationship("Organizer_DB", back_populates="user", uselist=False)