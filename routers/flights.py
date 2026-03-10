from fastapi import APIRouter
from typing import List
from schemas.flight_schema import Flight

router = APIRouter()

# temporary in-memory flight database
flights_db = [
    {
        "flight_id": "AI203",
        "airline": "Air India",
        "source": "DEL",
        "destination": "BLR",
        "departure_time": "10:30",
        "arrival_time": "13:10",
    },
    {
        "flight_id": "6E405",
        "airline": "Indigo",
        "source": "DEL",
        "destination": "BLR",
        "departure_time": "12:00",
        "arrival_time": "14:40",
    },
]


@router.get("/search-flights", response_model=List[Flight])
def search_flights(source: str, destination: str):
    results = []

    for flight in flights_db:
        if (
            flight["source"].lower() == source.lower()
            and flight["destination"].lower() == destination.lower()
        ):
            results.append(flight)

    return results