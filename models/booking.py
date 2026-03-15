from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

from database.session import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False, index=True)

    seat_number = Column(String, nullable=False)

    status = Column(String, default="CONFIRMED")

    created_at = Column(DateTime, default=datetime.utcnow)

    # ORM relationships
    user = relationship("User", back_populates="bookings")

    flight = relationship("Flight", back_populates="bookings")

    __table_args__ = (
        UniqueConstraint("flight_id", "seat_number", name="unique_flight_seat"),
    )