from fastapi import FastAPI
from routers import flights, bookings

app = FastAPI()

app.include_router(flights.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {"message": "Flight Booking API Running"}