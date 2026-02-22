# models/booking.py

from datetime import datetime


class Booking:
    def __init__(self, booking_id: str, passenger_name: str, flight_id: str):
        self.booking_id = booking_id
        self.passenger_name = passenger_name
        self.flight_id = flight_id
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "passenger_name": self.passenger_name,
            "flight_id": self.flight_id,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        booking = cls(
            booking_id=data["booking_id"],
            passenger_name=data["passenger_name"],
            flight_id=data["flight_id"],
        )
        booking.timestamp = datetime.fromisoformat(data["timestamp"])
        return booking