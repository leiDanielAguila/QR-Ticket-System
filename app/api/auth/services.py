# functions for authentication
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from app.models.organizers import Organizer_DB
from sqlalchemy import Exists

def password_validation(password: str):
    """ Check if the submitted password is valid """
    pass


def check_user_exists(email: str, db: Session) -> bool:
    """ Checks if this email exists in our database """
    return db.query(
        Exists().where(Organizer_DB.email == email)
    ).scalar()
    

def get_password_hash(password: str) -> str:
    """ 
    Get string password, convert to bcrypt hash, returns a hashed password

    args:
        password: String  
    returns:
        hashed password 
    example:
        >>> password = "password123"
        >>> get_password_hash(password)
        '$2b$13$HMQTprwhaUwmir.g.ZYoXuRJhtsbra4uj.qJPHrKsX5nGlhpts0jm'            
    """
    if password:
        return bcrypt.hash(password)
    
    
def verify_password(input_password: str, stored_password: str) -> bool:
    """
    Verify a plain text password against a stored hash
    
    args:
        input_password: Plain text password to verify
        stored_password: Bcrypt hashed password from database
    returns:
        True if password matches, False otherwise
    """
    return bcrypt.verify(input_password, stored_password)