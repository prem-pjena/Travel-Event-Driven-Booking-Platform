from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.booking import Booking

router = APIRouter()


@router.get("/booking/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        return {"error": "Booking not found"}

    return booking