# Travel Event-Driven Booking Platform (Backend Core)

## Overview

This project is a backend-focused implementation of a flight booking system built using FastAPI and clean layered architecture principles.

The objective of the project is not only to implement flight booking functionality, but to demonstrate production-oriented backend engineering practices including:

* Proper domain modeling
* Clear separation of concerns
* Encapsulation of business rules
* Layered backend architecture
* API design using REST principles
* Validation using Pydantic schemas
* Persistence isolation
* Production risk analysis

The project acts as the **backend core** for a scalable travel booking platform that can evolve into a distributed event-driven system.

---

## Architecture

The backend follows a layered service architecture designed to separate responsibilities and support scalability.

Client
↓
FastAPI Router Layer
↓
Schema Validation (Pydantic)
↓
Service Layer (Business Logic)
↓
Storage Layer (JSON Persistence)

This layered approach ensures that:

* HTTP handling is isolated from business logic
* Business logic is isolated from persistence
* Storage mechanisms can be replaced without impacting domain logic

---

## Folder Structure

```
.
├── main.py
├── booking.json
├── routers/
│   ├── flights.py
│   └── bookings.py
├── schemas/
│   ├── flight_schema.py
│   └── booking_schema.py
├── services/
│   └── booking_service.py
├── storage/
│   └── booking_storage.py
├── models/
│   ├── flight.py
│   └── booking.py
└── README.md
```

### Folder Responsibilities

**routers/**
Defines API endpoints and request routing.

**schemas/**
Contains Pydantic models for request validation and response serialization.

**services/**
Implements business logic such as creating and canceling bookings.

**storage/**
Handles persistence logic using JSON file storage.

**models/**
Represents domain entities such as Flight and Booking.

---

## Implemented API Endpoints

### Search Flights

GET /search-flights

Query Parameters:

* source
* destination

Example Request:

```
GET /search-flights?source=DEL&destination=BLR
```

Returns matching flights between the specified cities.

---

### Book Flight

POST /book-flight

Request Body:

```
{
 "flight_id": "AI203",
 "user_id": 1
}
```

Response Example:

```
{
 "booking_id": 1,
 "flight_id": "AI203",
 "user_id": 1
}
```

Creates a new booking and persists it.

---

### Cancel Booking

DELETE /cancel-booking/{booking_id}

Example:

```
DELETE /cancel-booking/1
```

Response:

```
{
 "message": "Booking cancelled"
}
```

Removes an existing booking.

---

## Domain Models

### Flight

Represents a flight entity with properties such as:

* flight_id
* airline
* source
* destination
* departure_time
* arrival_time

Flights are currently stored in an in-memory structure for demonstration purposes.

---

### Booking

Represents a booking record containing:

* booking_id
* flight_id
* user_id

Bookings are serialized to JSON for persistence.

---

## Booking Flow

1. Client sends booking request to API.
2. Router receives request and validates input using Pydantic schema.
3. Service layer processes the booking request.
4. Storage layer loads existing bookings from JSON.
5. New booking object is created.
6. Booking is appended and saved to storage.
7. Confirmation response is returned to the client.

---

## Key Backend Concepts Demonstrated

This project demonstrates several important backend engineering concepts:

* Layered architecture
* Separation of concerns
* RESTful API design
* Pydantic-based request validation
* Domain modeling
* JSON-based persistence
* HTTP status handling
* Production risk analysis
* Modular project structure

---

## Production Considerations Identified

The current JSON-based storage system has several known limitations:

* Not safe for concurrent writes
* Entire file rewritten on each booking
* No transaction safety
* No indexing for fast queries
* No idempotency protection
* No distributed locking
* No authentication
* No monitoring or logging

These limitations were intentionally analyzed to demonstrate awareness of production challenges.

---

## Scalability Path

To scale this system to production level:

1. Replace JSON persistence with PostgreSQL or DynamoDB.
2. Store seat availability in the database for atomic updates.
3. Deploy multiple FastAPI instances behind a load balancer.
4. Introduce Redis caching for frequently searched routes.
5. Implement database transactions to prevent double booking.
6. Introduce idempotency keys for retry-safe booking requests.
7. Add message queues for event-driven workflows.
8. Add observability through logging and monitoring tools.

The current architecture allows these improvements without changing the domain logic.

---

## How to Run

Create a virtual environment and install dependencies:

```
pip install fastapi uvicorn
```

Start the API server:

```
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

## Engineering Focus

This project emphasizes:

* Clean backend architecture
* Explicit validation and error handling
* Modular design for maintainability
* Early-stage production thinking
* Extensibility toward distributed systems

---

## Future Enhancements

Planned improvements include:

* Replace JSON storage with relational database
* Add Redis caching layer
* Implement seat reservation logic
* Introduce authentication and authorization
* Implement idempotent booking requests
* Add structured logging
* Add automated test suite
* Introduce message queue for event-driven booking notifications

---

## Interview Explanation Summary

"I designed a layered FastAPI backend that separates routing, validation, business logic, and persistence. The system models flights and bookings using domain entities while Pydantic schemas enforce request validation. Business logic resides in a service layer, keeping routers thin and storage isolated. Bookings are persisted using a JSON storage layer designed to be easily replaceable with a database. I also analyzed production risks such as race conditions, concurrency issues, and scalability bottlenecks to demonstrate system design awareness."

---

## Author

Prem Prakash Jena
Backend Engineering Practice Project
