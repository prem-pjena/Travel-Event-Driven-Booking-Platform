from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, UniqueConstraint
from datetime import datetime

from database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)

    seat_number = Column(String, nullable=False)

    status = Column(String, default="CONFIRMED")

    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("flight_id", "seat_number", name="unique_flight_seat"),
    )