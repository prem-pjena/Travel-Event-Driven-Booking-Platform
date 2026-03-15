from sqlalchemy.orm import Session
from repositories import booking_repository


def create_booking(db: Session, user_id: int, flight_id: int, seat_number: str):

    flight = booking_repository.get_flight_by_id(db, flight_id)

    if not flight:
        raise Exception("Flight not found")

    if flight.available_seats <= 0:
        raise Exception("No seats available")

    booking = booking_repository.create_booking(
        db,
        user_id=user_id,
        flight_id=flight_id,
        seat_number=seat_number
    )

    booking_repository.update_flight_seats(db, flight)

    db.commit()
    db.refresh(booking)

    return booking
def get_booking_by_id(db, booking_id: int):

    booking = booking_repository.get_booking_with_details(
        db,
        booking_id
    )

    return booking