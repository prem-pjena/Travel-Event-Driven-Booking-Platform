from fastapi import APIRouter, HTTPException
from schemas.booking_schema import BookFlightRequest
from services.booking_service import create_booking, cancel_booking

router = APIRouter()


@router.post("/book-flight", status_code=201)
def book_flight(request: BookFlightRequest):
    booking = create_booking(request.flight_id, request.user_id)
    return booking


@router.delete("/cancel-booking/{booking_id}")
def cancel_booking_api(booking_id: int):
    result = cancel_booking(booking_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result