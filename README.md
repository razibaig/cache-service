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

## API Endpoints

### 1. Create Payload

**Endpoint**: `POST /payload`

**Description**: This endpoint creates a new payload by transforming and interleaving two lists of strings. It returns an identifier for the generated payload, along with a flag indicating whether the result was cached.

**Request Example**:

```bash
curl -X POST "http://127.0.0.1:8000/payload" \
     -H "Content-Type: application/json" \
     -d '{
           "list_1": ["first string", "second string", "third string"],
           "list_2": ["other string", "another string", "last string"]
         }'
```

**Explanation**:
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/payload`
- **Headers**: `Content-Type: application/json` specifies that the request body is in JSON format.
- **Body**: A JSON object containing `list_1` and `list_2`, which are the two lists of strings to be transformed and interleaved.
- **Expected Response**: A JSON object containing:
  - `id`: The identifier of the newly created payload.
  - `cached`: A boolean flag indicating whether the output was retrieved from the cache.
  - `output`: The transformed and interleaved output.

**Response Example**:

```json
{
    "id": 1,
    "cached": false,
    "output": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
}
```

### 2. Retrieve Payload

**Endpoint**: `GET /payload/{id}`

**Description**: This endpoint retrieves a payload by its ID and returns the output of the payload.

**Request Example**:

```bash
curl -X GET "http://127.0.0.1:8000/payload/{id}"
```

- Replace `{id}` with the actual ID obtained from the `POST /payload` response.

**Explanation**:
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/payload/{id}`
- **Expected Response**: A JSON object containing:
  - `output`: The transformed and interleaved output of the payload.

**Response Example**:

```json
{
    "output": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
}
```

## Testing

To run the tests, use:

```bash
pytest tests/
```

Ensure that your test database is configured correctly.
