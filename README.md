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
ORM Layer (SQLAlchemy)
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
├── database.py
├── core/
│   ├── config.py
│   ├── dependencies.py
│   └── security.py
├── routers/
│   ├── auth.py
│   ├── flights.py
│   ├── bookings.py
│   └── users.py
├── schemas/
│   ├── flight_schema.py
│   ├── booking_schema.py
│   ├── user_schema.py
│   └── token_schema.py
├── services/
│   ├── auth_service.py
│   └── booking_service.py
├── models/
│   ├── flight.py
│   ├── booking.py
│   └── user.py
├── storage/
│   └── booking_storage.py
├── booking.json
└── README.md
```

### Folder Responsibilities

**routers/**
Defines API endpoints and request routing logic. Routers remain thin and delegate business logic to the service layer.

**schemas/**
Contains Pydantic models used for request validation and response serialization. Ensures that invalid data never reaches the business logic layer.

**services/**
Implements business rules such as creating bookings, validating seat availability, and orchestrating database operations.

**models/**
Defines SQLAlchemy ORM models that map Python classes to PostgreSQL tables.

**core/**
Contains authentication and shared backend utilities such as JWT token handling, security helpers, and dependency injection logic.

**database.py**
Centralized database configuration file that manages the SQLAlchemy engine, database sessions, and connection lifecycle.

**storage/**
Legacy JSON storage layer used in the initial version of the project. It demonstrates how persistence layers can be swapped without affecting the business logic.

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
* flight_number
* origin
* destination
* departure_time
* arrival_time
* total_seats
* available_seats
* created_at

Origin and destination columns are indexed to optimize flight search queries.

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

### Get Booking

GET /booking/{booking_id}

Protected endpoint requiring a valid JWT token.

Example request:

```
GET /booking/1
Authorization: Bearer <JWT_TOKEN>
```

Returns booking details if the booking exists and belongs to the authenticated user.

Example response:

```
{
  "id": 1,
  "user_id": 1,
  "flight_id": 1,
  "seat_number": "12A",
  "status": "CONFIRMED"
}
```

---

## Booking Flow

1. Client sends booking request to the API.
2. FastAPI router receives the request.
3. Pydantic schema validates input data.
4. Service layer checks seat availability.
5. Booking object is created through SQLAlchemy ORM.
6. Database transaction inserts the booking and updates seat availability.
7. PostgreSQL enforces seat uniqueness constraints.
8. Confirmation response is returned to the client.

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
* Database session management
* JWT authentication using OAuth2 bearer tokens
* Dependency-based authorization in FastAPI

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

Identifying these limitations early demonstrates awareness of **real-world backend engineering challenges**.

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

The current architecture is designed so these improvements can be introduced without rewriting the core domain logic.

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

"I designed a layered FastAPI backend that separates routing, validation, business logic, and persistence. The system models flights, users, and bookings using SQLAlchemy ORM mapped to a PostgreSQL relational database. Authentication is implemented using JWT tokens with OAuth2 bearer authentication. Database constraints enforce seat uniqueness to prevent double-booking during concurrent requests. Business logic resides in a service layer, keeping routers thin and persistence isolated. I also analyzed production risks such as race conditions, database bottlenecks, and scaling challenges to demonstrate system design awareness."

---

## Author

Prem Prakash Jena
Backend Engineering Practice Project
