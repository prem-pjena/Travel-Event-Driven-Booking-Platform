from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.user import User
from schemas.user_schema import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: UserCreate):
    """
    Creates a new user in the database.
    """

    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Create user object
    new_user = User(
    name=user.name,
    email=user.email,
    password_hash=hashed_password
)

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user