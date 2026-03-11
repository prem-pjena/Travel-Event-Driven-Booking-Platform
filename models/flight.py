from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    flight_number = Column(String, nullable=False)

    origin = Column(String, index=True, nullable=False)
    destination = Column(String, index=True, nullable=False)

    departure_time = Column(DateTime, nullable=False)

    arrival_time = Column(DateTime, nullable=False)

    total_seats = Column(Integer, nullable=False)

    available_seats = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)