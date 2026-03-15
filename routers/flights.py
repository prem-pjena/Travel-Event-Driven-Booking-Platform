from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from models.flight import Flight

router = APIRouter(
    tags=["Flights"]
)


@router.post("/flights")
def create_flight(
    departure_city: str,
    arrival_city: str,
    available_seats: int,
    db: Session = Depends(get_db)
):

    flight = Flight(
        departure_city=departure_city,
        arrival_city=arrival_city,
        available_seats=available_seats
    )

    db.add(flight)
    db.commit()
    db.refresh(flight)

    return flight