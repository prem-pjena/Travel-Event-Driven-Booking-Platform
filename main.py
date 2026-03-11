from fastapi import FastAPI
from routers import flights, bookings
from database import engine
from models import user
from database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(flights.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {"message": "Flight Booking API Running"}