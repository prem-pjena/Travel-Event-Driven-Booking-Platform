from sqlalchemy.orm import Session
from models.booking import Booking
from models.flight import Flight


def create_booking(db: Session, user_id: int, flight_id: int, seat_number: str):

    flight = db.query(Flight).filter(Flight.id == flight_id).first()

    if not flight:
        raise Exception("Flight not found")

    if flight.available_seats <= 0:
        raise Exception("No seats available")

    booking = Booking(
        user_id=user_id,
        flight_id=flight_id,
        seat_number=seat_number
    )

    flight.available_seats -= 1

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking