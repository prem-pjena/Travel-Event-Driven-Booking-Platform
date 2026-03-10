from storage.booking_storage import load_bookings, save_bookings


def create_booking(flight_id: str, user_id: int):
    bookings = load_bookings()

    booking_id = len(bookings) + 1

    booking = {
        "booking_id": booking_id,
        "flight_id": flight_id,
        "user_id": user_id,
    }

    bookings.append(booking)
    save_bookings(bookings)

    return booking


def cancel_booking(booking_id: int):
    bookings = load_bookings()

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            bookings.remove(booking)
            save_bookings(bookings)
            return {"message": "Booking cancelled"}

    return {"error": "Booking not found"}