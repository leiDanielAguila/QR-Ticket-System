# auth router
from sqlalchemy.orm import Session
from app.dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from app.services import generate_id
from app.models.organizers import Organizer_DB
from app.models.auth import User_DB
from app.schemas.organizers import Organizers
from app.api.auth.services import get_password_hash, check_user_exists, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
async def login(db: Session = Depends(get_db)):
    pass


@router.post("/sign_up")
async def sign_up(o: Organizers, db: Session = Depends(get_db)):
    
    if check_user_exists(o.email, db):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account is already created"
        )
    
    # add password validation here from services

    organizer_id = generate_id()

    new_organizer = Organizer_DB(
        id = organizer_id,
        email = o.email,
        first_name = o.first_name,
        last_name = o.last_name
    )

    organizer_account = User_DB(
        id = organizer_id,
        password = get_password_hash(o.password)
    )
    try:
        db.add(new_organizer)
        db.add(organizer_account)
        db.commit()
        db.refresh(new_organizer)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create account"
        )
    
    return {
        "message": "Account created successfully",
        "user": {
            "id": organizer_id,
            "email": o.email,
            "name": f"{o.first_name} {o.last_name}"
        }
    }




