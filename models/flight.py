# models/flight.py

class NoSeatsAvailableError(Exception):
    """Raised when attempting to book a seat on a full flight."""
    pass


class Flight:
    def __init__(self, flight_id: str, seats_available: int):
        self.flight_id = flight_id
        self.seats_available = seats_available

    def book_seat(self):
        if self.seats_available <= 0:
            raise NoSeatsAvailableError(
                f"No seats available for flight {self.flight_id}"
            )

        self.seats_available -= 1
        return True