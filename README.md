# Travel Event-Driven Booking Platform (Backend Core)

## Overview

This project is a backend-focused implementation of a flight booking system designed using clean layered architecture principles.  

The goal of this project is not just to “make booking work”, but to demonstrate:

- Proper domain modeling using OOP
- Separation of concerns
- Encapsulation of business rules
- Isolated persistence layer
- Production-level architectural thinking

This project serves as the foundational core for scaling into a distributed, event-driven booking platform.

---

## Architecture

The system follows a layered backend architecture:


Interface Layer (CLI)
↓
Service Layer (BookingService)
↓
Domain Models (Flight, Booking)
↓
Persistence Layer (BookingStorage - JSON)


### Folder Structure


.
├── main.py
├── models/
│ ├── flight.py
│ └── booking.py
├── services/
│ └── booking_service.py
└── storage/
└── booking_storage.py


---

## Core Components

### 1. Flight (Domain Model)

Represents a flight entity.

Responsibilities:
- Stores flight_id
- Manages seat availability
- Protects seat invariants
- Raises domain-specific exception when no seats available

Encapsulation ensures seat count cannot be modified arbitrarily.

Example invariant:

seats_available >= 0


---

### 2. Booking (Domain Model)

Represents a booking record.

Stores:
- booking_id
- passenger_name
- flight_id
- timestamp

Implements:
- `to_dict()` for JSON serialization
- `from_dict()` for object reconstruction

This preserves domain behavior while enabling persistence.

---

### 3. BookingService (Service Layer)

Coordinates booking workflow.

Responsibilities:
- Validate flight existence
- Trigger seat booking
- Create booking object
- Persist booking via storage layer

Service layer does not:
- Handle file system directly
- Modify seat state manually
- Print output

It orchestrates domain interactions.

---

### 4. BookingStorage (Persistence Layer)

Handles JSON-based storage.

Responsibilities:
- Load bookings from file
- Save new bookings
- Convert dictionary ↔ object
- Handle missing or corrupted files gracefully

Persistence logic is fully isolated, allowing easy migration to a database.

---

## Booking Flow

1. User submits booking request.
2. BookingService validates flight.
3. Flight.book_seat() reduces seat safely.
4. Booking object is created.
5. BookingStorage persists booking.
6. Confirmation returned.

---

## Key Backend Concepts Demonstrated

- Layered architecture
- Separation of concerns
- Encapsulation
- Custom domain exceptions
- Object serialization/deserialization
- Clean orchestration via service layer
- Persistence isolation
- Production risk analysis

---

## Production Considerations Identified

The current JSON-based implementation has known limitations:

- Not concurrency safe
- Entire file rewritten on each booking
- Seat state stored in memory
- No transaction safety
- No idempotency protection
- No distributed locking
- No logging or monitoring

These were intentionally analyzed to bridge into system design thinking.

---

## Scalability Path

To scale this system:

1. Replace JSON storage with PostgreSQL or DynamoDB.
2. Move seat state to database for atomic updates.
3. Deploy multiple FastAPI instances behind a load balancer.
4. Add transactional seat reservation logic.
5. Introduce message queue for asynchronous notifications.
6. Implement idempotency keys for duplicate request protection.

The current architecture supports these transitions without changing domain logic.

---

## How to Run


python main.py


Follow CLI prompts to create a booking.

Bookings persist in `booking.json`.

---

## Engineering Focus

This project emphasizes:

- Correctness over shortcuts
- Clean architecture over script-style coding
- Production thinking from early stages
- Explicit error handling
- Extensibility for distributed systems

---

## Future Enhancements

- Replace JSON with relational database
- Add FastAPI interface
- Add Redis caching
- Add message queue for event-driven flow
- Implement concurrency-safe booking logic
- Add structured logging
- Add test suite

---

## Interview Explanation Summary

"I designed a layered booking backend with domain-driven modeling. The Flight entity encapsulates seat management using custom exceptions to enforce invariants. The service layer orchestrates booking logic while remaining decoupled from persistence. JSON storage is isolated and replaceable, allowing migration to a transactional database without modifying domain logic. I also analyzed production risks including race conditions, state inconsistency, and scalability limitations."

---

## Author

Prem Prakash Jena  
Backend Engineering Practice Project