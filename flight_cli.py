# -------------------------------
# Data Layer
# -------------------------------

def get_all_flights():
    return [
        {
            "flight_id": 1,
            "airline": "IndiGo",
            "source": "DEL",
            "destination": "BOM",
            "departure_time": "08:00",
            "arrival_time": "10:00",
            "price": 5000,
            "seats_available": 5
        },
        {
            "flight_id": 2,
            "airline": "Air India",
            "source": "DEL",
            "destination": "BOM",
            "departure_time": "12:00",
            "arrival_time": "14:30",
            "price": 4500,
            "seats_available": 0
        },
        {
            "flight_id": 3,
            "airline": "SpiceJet",
            "source": "DEL",
            "destination": "BLR",
            "departure_time": "09:00",
            "arrival_time": "11:45",
            "price": 6000,
            "seats_available": 3
        },
    ]


# -------------------------------
# Service Layer
# -------------------------------

def search_flights(flights, source, destination):
    return [
        flight for flight in flights
        if flight["source"] == source and flight["destination"] == destination
    ]


def filter_available_seats(flights):
    return [
        flight for flight in flights
        if flight["seats_available"] > 0
    ]


def filter_by_max_price(flights, max_price):
    return [
        flight for flight in flights
        if flight["price"] <= max_price
    ]


def sort_flights(flights, key, reverse=False):
    return sorted(flights, key=lambda x: x[key], reverse=reverse)


# -------------------------------
# Interface Layer
# -------------------------------

def display_flights(flights):
    if not flights:
        print("\nNo flights found.\n")
        return

    print("\nAvailable Flights:\n")
    for flight in flights:
        print(f"Flight ID: {flight['flight_id']}")
        print(f"Airline: {flight['airline']}")
        print(f"Route: {flight['source']} → {flight['destination']}")
        print(f"Departure: {flight['departure_time']}")
        print(f"Arrival: {flight['arrival_time']}")
        print(f"Price: ₹{flight['price']}")
        print(f"Seats Available: {flight['seats_available']}")
        print("-" * 40)


def main():
    flights = get_all_flights()

    source = input("Enter source (e.g., DEL): ").upper()
    destination = input("Enter destination (e.g., BOM): ").upper()
    max_price_input = input("Enter maximum price (or press Enter to skip): ")

    results = search_flights(flights, source, destination)
    results = filter_available_seats(results)

    if max_price_input:
        max_price = int(max_price_input)
        results = filter_by_max_price(results, max_price)

    results = sort_flights(results, key="price")

    display_flights(results)


if __name__ == "__main__":
    main()
