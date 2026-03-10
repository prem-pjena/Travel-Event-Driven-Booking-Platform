from pydantic import BaseModel


class BookFlightRequest(BaseModel):
    flight_id: str
    user_id: int


class BookingResponse(BaseModel):
    booking_id: int
    flight_id: str
    user_id: int