# FastAPI Cache Service

This project is a FastAPI-based service designed to handle payload transformations and caching. It provides RESTful endpoints to create and retrieve payloads, leveraging a database for storage.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: ORM for database interactions.
- **Docker**: Containerization for easy deployment.
- **Uvicorn**: ASGI server for running FastAPI applications.

## Prerequisites

- Python 3.11
- Docker (optional, for containerized deployment)
- PostgreSQL or any other SQL database supported by SQLAlchemy

## Installation

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**

   Ensure your database is running and update the database connection settings in `app/core/database.py`.

5. **Run the Application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

### Docker Setup

1. **Build the Docker Image:**

   ```bash
   docker build -t fastapi-cache-service .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -p 8000:8000 fastapi-cache-service
   ```

   The application will be available at `http://localhost:8000`.

## API Documentation

FastAPI provides interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

- **POST /payload**: Create a new payload.
  - Request Body: `PayloadRequest` (list_1, list_2)
  - Response: `PayloadResponse` (output)

- **GET /payload/{id}**: Retrieve a payload by ID.
  - Response: `PayloadResponse` (output)

## Testing

To run the tests, use:

```bash
pytest tests/
```

Ensure that your test database is configured correctly.
