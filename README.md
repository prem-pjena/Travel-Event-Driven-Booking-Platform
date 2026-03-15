Travel Event-Driven Booking Platform (Backend Core)
Overview

This project is a backend-focused implementation of a flight booking system built using FastAPI, SQLAlchemy, and PostgreSQL, following clean layered architecture principles.

The objective of the project is not only to implement flight booking functionality, but to demonstrate production-oriented backend engineering practices, including proper domain modeling, separation of concerns, layered architecture, RESTful API design, request validation, relational database design, authentication, and production scalability awareness.

The project acts as the backend core of a scalable travel booking platform that can evolve into a distributed event-driven system.

The backend demonstrates how a real-world booking platform can be structured to support growth, maintainability, and reliability while keeping the codebase modular and extensible.

Architecture

The backend follows a layered service architecture designed to isolate responsibilities and allow the system to scale.

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

This layered approach ensures that HTTP handling is isolated from business logic, business logic is isolated from persistence logic, database implementation can evolve without impacting application logic, and each layer remains independently testable and maintainable.

Routers remain thin and only orchestrate request handling, while the service layer contains the core business rules.

Folder Structure

The backend project is organized into clearly separated layers.

main.py
database/
 session.py

core/
 config.py
 dependencies.py
 security.py

routers/
 auth.py
 flights.py
 bookings.py

schemas/
 flight_schema.py
 booking_schema.py
 user_schema.py
 token_schema.py

services/
 auth_service.py
 booking_service.py

repositories/
 booking_repository.py

models/
 flight.py
 booking.py
 user.py

tests/
 test_users.py
 test_bookings.py

Dockerfile
docker-compose.yml
README.md

Folder Responsibilities

routers/
Defines API endpoints and request routing logic. Routers remain thin and delegate business logic to the service layer.

schemas/
Contains Pydantic models used for request validation and response serialization. Ensures that invalid data never reaches the business logic layer.

services/
Implements business rules such as validating seat availability, enforcing authorization rules, and orchestrating database operations.

repositories/
Encapsulates database queries and persistence logic. This layer isolates SQLAlchemy operations from business logic.

models/
Defines SQLAlchemy ORM models that map Python classes to PostgreSQL tables.

core/
Contains authentication utilities and shared backend logic such as JWT token handling, security helpers, and dependency injection.

database/
Handles database configuration including the SQLAlchemy engine, session creation, and connection lifecycle.

tests/
Contains automated integration tests using pytest and FastAPI TestClient to validate API functionality.

Database Schema

The backend uses PostgreSQL as the primary persistence layer.

The relational schema consists of three core tables: Users, Flights, and Bookings.

Users

Stores user account information.

Fields include id, name, email, password_hash, and created_at.

Email addresses are unique and indexed to ensure fast lookup and prevent duplicate accounts.

Flights

Represents available flights in the system.

Fields include id, departure_city, arrival_city, available_seats, and created_at.

Departure and arrival cities are indexed to optimize search queries.

Bookings

Represents a seat reservation made by a user.

Fields include id, user_id, flight_id, seat_number, status, and created_at.

User and flight fields are foreign keys referencing their respective tables.

A unique constraint ensures that a seat cannot be booked more than once on the same flight.

UNIQUE (flight_id, seat_number)

This constraint protects the system from double-booking during concurrent requests.

Implemented API Endpoints
Authentication

Register User

POST /auth/register

Request body example

{
"name": "Prem",
"email": "prem@test.com
",
"password": "password123"
}

Creates a new user account and securely stores the hashed password using bcrypt.

Login User

POST /auth/login

Form data example

username = prem@test.com

password = password123

Returns a JWT access token used for authenticated requests.

Example response

{
"access_token": "JWT_TOKEN",
"token_type": "bearer"
}

Search Flights

GET /search-flights

Example request

/search-flights?source=DEL&destination=BLR

Returns flights between the specified cities.

Create Booking

POST /bookings

Protected endpoint requiring a valid JWT token.

Example request

POST /bookings?flight_id=1&seat_number=A1
Authorization: Bearer <JWT_TOKEN>

Creates a booking if seats are available.

Get Booking

GET /booking/{booking_id}

Protected endpoint requiring a valid JWT token.

Example request

GET /booking/1
Authorization: Bearer <JWT_TOKEN>

Returns booking details including related user and flight information using relational joins.

Example response

{
"id": 1,
"seat_number": "A1",
"status": "CONFIRMED",
"user": {
"id": 1,
"name": "Test User",
"email": "testuser@mail.com
"
},
"flight": {
"id": 1,
"departure_city": "DEL",
"arrival_city": "BLR",
"available_seats": 49
}
}

Booking Flow

Client sends booking request to the API.
FastAPI router receives the request.
JWT authentication validates the user.
Pydantic schema validates the request.
Service layer verifies seat availability.
Repository layer performs database operations.
SQLAlchemy ORM creates the booking entity.
PostgreSQL enforces uniqueness constraints.
Seat count is updated and booking confirmed.
The API returns a booking confirmation response.

Automated Testing

The backend includes automated API tests written using pytest and FastAPI TestClient.

Tests validate core functionality including user registration and booking creation.

Example command to run tests

pytest -v

Successful test run confirms that the booking and authentication flows operate correctly and that API endpoints behave as expected.

Dockerized Deployment

The backend is containerized using Docker and orchestrated using Docker Compose.

Two services are defined:

FastAPI backend container
PostgreSQL database container

The application can be started using

docker compose up

This ensures a reproducible development environment and simplifies deployment.

Key Backend Concepts Demonstrated

This project demonstrates several important backend engineering principles including layered backend architecture, separation of concerns, RESTful API design, Pydantic-based validation, SQLAlchemy ORM integration, relational database modeling, foreign key relationships, database constraints for data integrity, repository pattern abstraction, dependency injection, JWT authentication, OAuth2 bearer token authorization, database session lifecycle management, automated API testing, and containerized deployment.

Production Considerations Identified

During development several production-level risks were analyzed.

Potential challenges include race conditions during simultaneous seat booking, database connection limits under heavy traffic, query latency for large datasets, absence of caching for read-heavy endpoints, token theft risks, missing structured logging and monitoring, retry-based duplicate bookings, distributed locking requirements, and database bottlenecks under high concurrency.

Recognizing these limitations demonstrates awareness of real-world backend engineering challenges.

Scalability Path

To scale the system toward production readiness several improvements could be introduced.

Redis caching could be added for frequently searched routes.
Multiple FastAPI instances could be deployed behind a load balancer.
PostgreSQL read replicas could be introduced for read-heavy queries.
Transaction-safe seat reservation logic could be implemented.
Idempotency keys could protect booking endpoints from duplicate retries.
Background event processing could be implemented using message queues.
Observability could be added through logging, metrics, and tracing.
Authentication could be improved with refresh tokens and session management.

The current architecture allows these improvements without requiring major changes to the domain logic.

How to Run

Create a virtual environment and install dependencies.

pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] python-jose python-multipart email-validator

Start the development server.

uvicorn main:app --reload

Server runs at

http://127.0.0.1:8000

Interactive API documentation is available at

http://127.0.0.1:8000/docs

Engineering Focus

This project emphasizes clean backend architecture, modular design, explicit validation and error handling, secure authentication mechanisms, relational data integrity, production-oriented engineering thinking, and extensibility toward distributed systems.

Future Enhancements

Planned improvements include implementing seat reservation transactions, introducing Redis caching, adding refresh token authentication, expanding automated test coverage, implementing structured logging, introducing distributed message queues, enabling event-driven notifications, managing database migrations using Alembic, and deploying the system to cloud infrastructure.

Interview Explanation Summary

I designed a layered FastAPI backend that separates routing, validation, business logic, and persistence. The system models flights, users, and bookings using SQLAlchemy ORM mapped to a PostgreSQL relational database. Authentication is implemented using JWT tokens with OAuth2 bearer authentication. Database constraints enforce seat uniqueness to prevent double-booking during concurrent requests. Business logic resides in a service layer while database queries are isolated in a repository layer, keeping routers thin and persistence decoupled. The system includes automated API testing and Dockerized deployment. I also analyzed production risks such as race conditions, database bottlenecks, and scalability challenges to demonstrate system design awareness.

Author

Prem Prakash Jena
Backend Engineering Practice Project