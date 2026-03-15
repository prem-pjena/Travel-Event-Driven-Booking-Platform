from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_db
from models.user import User
from core.dependencies import get_current_user
from services import booking_service


router = APIRouter(
    tags=["Bookings"]
)


@router.get("/booking/{booking_id}")
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = booking_service.get_booking_by_id(db, booking_id)

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
@router.post("/bookings")
def create_booking(
    flight_id: int,
    seat_number: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = booking_service.create_booking(
        db,
        current_user.id,
        flight_id,
        seat_number
    )

    return booking