from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.session import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    departure_city = Column(String, nullable=False)

    arrival_city = Column(String, nullable=False)

    available_seats = Column(Integer, nullable=False)

    # 🔗 Relationship with bookings
    bookings = relationship("Booking", back_populates="flight")