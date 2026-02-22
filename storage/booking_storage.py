# storage/booking_storage.py

import json
import os
from models.booking import Booking


class BookingStorage:
    def __init__(self, file_path="booking.json"):
        self.file_path = file_path

    def load_bookings(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Booking.from_dict(item) for item in data]
        except json.JSONDecodeError:
            # Corrupted file case
            return []

    def save_booking(self, booking: Booking):
        bookings = self.load_bookings()
        bookings.append(booking)

        with open(self.file_path, "w") as f:
            json.dump([b.to_dict() for b in bookings], f, indent=4)