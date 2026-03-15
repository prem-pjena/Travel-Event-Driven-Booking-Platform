from fastapi import FastAPI

from database.session import engine, Base

# Import models so SQLAlchemy can register them
from models import user
from models import flight
from models import booking

# Import routers
from routers import users   # ← ADD THIS LINE
from routers import auth
from routers import flights
from routers import bookings


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Travel Booking API",
    version="1.0.0",
    description="Backend API for the Travel Event Driven Booking Platform"
)


# Register routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(flights.router)
app.include_router(bookings.router)


@app.get("/")
def root():
    return {"message": "Flight Booking API Running"}