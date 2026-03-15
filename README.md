# Travel Event-Driven Booking Platform (Backend Core)

## Overview

This project is a backend-focused implementation of a flight booking system built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, following clean layered architecture principles.

The objective of the project is not only to implement flight booking functionality, but to demonstrate **production-oriented backend engineering practices**, including:

* Proper domain modeling
* Clear separation of concerns
* Encapsulation of business rules
* Layered backend architecture
* RESTful API design
* Request validation using Pydantic schemas
* Relational database design using PostgreSQL
* Persistence abstraction using SQLAlchemy ORM
* Data integrity through foreign keys and constraints
* Authentication and authorization using JWT tokens
* Production risk and scalability analysis

The project acts as the **backend core of a scalable travel booking platform** that can evolve into a distributed event-driven system.

---

## Architecture

The backend follows a **layered service architecture** designed to isolate responsibilities and allow the system to scale.

Client
↓
FastAPI Router Layer
↓
Schema Validation (Pydantic)
↓
Service Layer (Business Logic)
↓
Repository Layer (Persistence Abstraction)
↓
SQLAlchemy ORM
↓
PostgreSQL Database

This layered approach ensures that:

* HTTP handling is isolated from business logic
* Business logic is isolated from persistence logic
* Database implementation can evolve without impacting application logic
* Each layer remains independently testable and maintainable

---

## Folder Structure

```
.
├── main.py
├── database/
│   └── session.py
├── core/
│   ├── config.py
│   ├── dependencies.py
│   └── security.py
├── routers/
│   ├── auth.py
│   ├── flights.py
│   └── bookings.py
├── schemas/
│   ├── flight_schema.py
│   ├── booking_schema.py
│   ├── user_schema.py
│   └── token_schema.py
├── services/
│   ├── auth_service.py
│   └── booking_service.py
├── repositories/
│   └── booking_repository.py
├── models/
│   ├── flight.py
│   ├── booking.py
│   └── user.py
├── README.md
```

### Folder Responsibilities

**routers/**
Defines API endpoints and request routing logic. Routers remain thin and delegate business logic to the service layer.

**schemas/**
Contains Pydantic models used for request validation and response serialization. Ensures that invalid data never reaches the business logic layer.

**services/**
Implements business rules such as validating seat availability, enforcing authorization rules, and orchestrating database operations.

**repositories/**
Encapsulates database queries and persistence logic. This layer isolates SQLAlchemy operations from business logic.

**models/**
Defines SQLAlchemy ORM models that map Python classes to PostgreSQL tables.

**core/**
Contains authentication utilities and shared backend logic such as JWT token handling, security helpers, and dependency injection.

**database/**
Handles database configuration including the SQLAlchemy engine, session creation, and connection lifecycle.

---

## Database Schema

The backend uses **PostgreSQL as the primary persistence layer**.

The relational schema consists of three core tables.

### Users

Stores user account information.

Fields:

* id (primary key)
* name
* email (unique)
* password_hash
* created_at

Email addresses are indexed and unique to ensure fast lookup and prevent duplicate accounts.

---

### Flights

Represents available flights in the system.

Fields:

* id (primary key)
* departure_city
* arrival_city
* available_seats
* created_at

Departure and arrival cities are indexed to optimize flight search queries.

---

### Bookings

Represents a seat reservation made by a user.

Fields:

* id (primary key)
* user_id (foreign key → users.id)
* flight_id (foreign key → flights.id)
* seat_number
* status
* created_at

A unique constraint ensures that a seat cannot be booked more than once on the same flight.

```
UNIQUE (flight_id, seat_number)
```

This protects the system from double-booking during concurrent requests.

---

## Implemented API Endpoints

### Authentication

#### Register User

POST /auth/register

Request body:

```
{
  "name": "Prem",
  "email": "prem@test.com",
  "password": "password123"
}
```

Creates a new user account and securely stores the hashed password using bcrypt.

---

#### Login User

POST /auth/login

Form data:

```
username = prem@test.com
password = password123
```

Returns a **JWT access token** used for authenticated requests.

Example response:

```
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

### Search Flights

GET /search-flights

Example request:

```
/search-flights?source=DEL&destination=BLR
```

Returns matching flights between the specified cities.

---

### Create Booking

POST /bookings

Protected endpoint requiring a valid JWT token.

Example request:

```
POST /bookings?flight_id=1&seat_number=A1
Authorization: Bearer <JWT_TOKEN>
```

Creates a booking if seats are available.

---

### Get Booking

GET /booking/{booking_id}

Protected endpoint requiring a valid JWT token.

Example request:

```
GET /booking/1
Authorization: Bearer <JWT_TOKEN>
```

Returns booking details along with related flight and user data using relational JOIN queries.

Example response:

```
{
  "id": 1,
  "seat_number": "A1",
  "status": "CONFIRMED",
  "user": {
    "id": 1,
    "name": "Test User",
    "email": "testuser@mail.com"
  },
  "flight": {
    "id": 1,
    "departure_city": "DEL",
    "arrival_city": "BLR",
    "available_seats": 49
  }
}
```

---

## Booking Flow

1. Client sends booking request to the API.
2. FastAPI router receives the request.
3. JWT authentication validates the user.
4. Pydantic schema validates input data.
5. Service layer checks seat availability.
6. Repository layer performs database operations.
7. SQLAlchemy ORM creates the booking object.
8. PostgreSQL enforces seat uniqueness constraints.
9. Seat count is updated and booking confirmed.
10. API returns the booking confirmation response.

---

## Key Backend Concepts Demonstrated

This project demonstrates several important backend engineering principles:

* Layered backend architecture
* Separation of concerns
* RESTful API design
* Pydantic-based request validation
* SQLAlchemy ORM integration
* Relational database modeling
* Foreign key relationships
* Database constraints for data integrity
* Modular service-based backend design
* Repository pattern for persistence abstraction
* Database session management
* JWT authentication using OAuth2 bearer tokens
* Dependency-based authorization in FastAPI
* ORM relationship loading using JOIN queries

---

## Production Considerations Identified

During development several production-level risks were analyzed.

Potential challenges include:

* Race conditions during simultaneous seat booking
* Database connection limits under heavy traffic
* Query latency for large datasets
* Need for caching for read-heavy endpoints
* Token theft and authentication security risks
* Lack of structured logging and monitoring
* Missing retry-safe booking logic
* Absence of distributed locking
* Potential database bottlenecks under high write load

Identifying these limitations demonstrates awareness of **real-world backend engineering challenges**.

---

## Scalability Path

To scale this system toward production readiness:

1. Introduce Redis caching for frequently searched routes.
2. Deploy multiple FastAPI instances behind a load balancer.
3. Introduce read replicas for the PostgreSQL database.
4. Implement transaction-safe seat reservation logic.
5. Add idempotency keys to protect against retry-based duplicate bookings.
6. Introduce background event processing using message queues.
7. Add observability through metrics, logs, and tracing.
8. Implement authentication refresh tokens and session management.

The current architecture is designed so these improvements can be introduced **without rewriting the core domain logic**.

---

## How to Run

Create a virtual environment and install dependencies:

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] python-jose python-multipart email-validator
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
* Proper database modeling
* Explicit validation and error handling
* Modular service-layer design
* Relational data integrity
* Authentication and authorization mechanisms
* Production-oriented engineering thinking
* Extensibility toward distributed systems

---

## Future Enhancements

Planned improvements include:

* Implement full booking creation API
* Implement seat reservation transactions
* Introduce Redis caching layer
* Implement refresh token authentication
* Add automated test suite
* Add structured logging
* Introduce distributed message queues
* Implement event-driven notifications
* Add database migrations using Alembic
* Deploy backend using containerized infrastructure

---

## Interview Explanation Summary

"I designed a layered FastAPI backend that separates routing, validation, business logic, and persistence. The system models flights, users, and bookings using SQLAlchemy ORM mapped to a PostgreSQL relational database. Authentication is implemented using JWT tokens with OAuth2 bearer authentication. Database constraints enforce seat uniqueness to prevent double-booking during concurrent requests. Business logic resides in a service layer while database queries are isolated in a repository layer, keeping routers thin and persistence decoupled. I also analyzed production risks such as race conditions, database bottlenecks, and scaling challenges to demonstrate system design awareness."

---

## Author

Prem Prakash Jena
Backend Engineering Practice Project
