from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.booking import Booking
from models.user import User
from core.dependencies import get_current_user

router = APIRouter(
    tags=["Bookings"]
)


@router.get("/booking/{booking_id}")
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    # 🔐 SECURITY: ensure user can only access their own booking
    if booking.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to access this booking"
        )

    return booking