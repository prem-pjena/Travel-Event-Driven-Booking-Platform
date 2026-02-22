# services/booking_service.py

import uuid
from models.booking import Booking
from models.flight import NoSeatsAvailableError


class BookingService:
    def __init__(self, flights: dict, storage):
        self.flights = flights  # dict of flight_id -> Flight object
        self.storage = storage

    def create_booking(self, passenger_name: str, flight_id: str):
        if flight_id not in self.flights:
            raise ValueError("Flight does not exist")

        flight = self.flights[flight_id]

        # Seat reduction (may raise NoSeatsAvailableError)
        flight.book_seat()

        booking = Booking(
            booking_id=str(uuid.uuid4()),
            passenger_name=passenger_name,
            flight_id=flight_id,
        )

        self.storage.save_booking(booking)

        return booking