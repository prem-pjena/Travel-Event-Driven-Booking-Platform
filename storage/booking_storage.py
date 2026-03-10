import json

FILE_PATH = "booking.json"


def load_bookings():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []


def save_bookings(bookings):
    with open(FILE_PATH, "w") as f:
        json.dump(bookings, f, indent=2)