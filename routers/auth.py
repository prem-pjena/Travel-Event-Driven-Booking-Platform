from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database.session import get_db
from models.user import User
from schemas.user_schema import UserCreate
from schemas.token_schema import Token

from core.security import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    # check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # hash password
    hashed_pw = hash_password(user.password)

    # create new user
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email
    }


@router.post("/login", response_model=Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # find user
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # verify password
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # create JWT token
    access_token = create_access_token(
        data={"user_id": user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }