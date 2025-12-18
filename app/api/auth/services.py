# functions for authentication
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from app.models.organizers import Organizer_DB
from sqlalchemy import Exists
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from app.schemas.organizers import Organizers
import jwt
import os

load_dotenv()

def password_validation(password: str):
    """ Check if the submitted password follows the password policy """
    pass

def create_token(u: Organizers):
    user_name = u.first_name + " " + u.last_name

    payload = {
        "sub" : user_name,
        "exp" : datetime.now(timezone.utc) + timedelta(minutes=5)
    }

    secret_key = os.getenv("JWT_SECRET_KEY")

    token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")

    return token


def validate_token(token: str):
    pass


def check_user_exists(email: str, db: Session) -> bool:
    """ Checks if this email exists in our database """
    return db.query(
        Exists().where(Organizer_DB.email == email)
    ).scalar()
    

def get_password_hash(password: str) -> str:
    """
    returns an encrypted password using bcrypt

    """

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