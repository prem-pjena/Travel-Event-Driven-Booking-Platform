from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user in the system.
    """

    created_user = create_user(db, user)

    if not created_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return created_user