# main.py

from models.flight import Flight
from storage.booking_storage import BookingStorage
from services.booking_service import BookingService
from models.flight import NoSeatsAvailableError

def main():
    # Setup
    flights = {
        "AI101": Flight("AI101", 2)
    }

    storage = BookingStorage()
    service = BookingService(flights, storage)

    passenger_name = input("Enter passenger name: ")
    flight_id = input("Enter flight ID: ")

    try:
        booking = service.create_booking(passenger_name, flight_id)
        print("Booking successful!")
        print("Booking ID:", booking.booking_id)
    except NoSeatsAvailableError as e:
        print("Booking failed:", str(e))
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()