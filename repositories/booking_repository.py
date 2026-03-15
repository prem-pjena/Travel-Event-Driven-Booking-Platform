from sqlalchemy.orm import Session
from models.booking import Booking
from models.flight import Flight

from sqlalchemy.orm import joinedload


def get_booking_with_details(db: Session, booking_id: int):
    return (
        db.query(Booking)
        .options(
            joinedload(Booking.user),
            joinedload(Booking.flight)
        )
        .filter(Booking.id == booking_id)
        .first()
    )


def get_flight_by_id(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()


def create_booking(db: Session, user_id: int, flight_id: int, seat_number: str):
    booking = Booking(
        user_id=user_id,
        flight_id=flight_id,
        seat_number=seat_number
    )

    db.add(booking)
    return booking


def update_flight_seats(db: Session, flight: Flight):
    flight.available_seats -= 1
    db.add(flight)