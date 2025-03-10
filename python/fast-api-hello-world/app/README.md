# FastAPI Application Endpoints

This document explains how to interact with the available API endpoints.

## Available Endpoints

### 1. Root Endpoint (`/`)

Returns a welcome message.

```bash
# Using curl
curl http://localhost:8000/

# Expected response
{"message": "Hello World"}
```

### 2. Health Check (`/health`)

Checks if the application is running properly.

```bash
# Using curl
curl http://localhost:8000/health

# Expected response
{"status": "healthy"}
```

## API Documentation (Swagger)

The API documentation is available in three ways:

### 1. Swagger UI (Interactive)
- URL: `http://localhost:8000/docs`
- Features:
  - Interactive API testing
  - Request/response examples
  - Schema information
  - Try-it-out functionality

### 2. ReDoc (Alternative View)
- URL: `http://localhost:8000/redoc`
- Features:
  - Clean documentation layout
  - Easy-to-read format
  - Search functionality

### 3. OpenAPI Schema (Raw)
- URL: `http://localhost:8000/openapi.json`
- Features:
  - Raw OpenAPI/Swagger specification
  - Useful for automated tools

## Using Project Commands

If you're using the project's command runner (just), you can:

```bash
# Start the server
just dev

# Check health
just health

# Open Swagger documentation
just docs
```

## Response Codes

### Health Check Endpoint
- `200 OK`: Application is healthy
  ```json
  {"status": "healthy"}
  ```
- `503 Service Unavailable`: Application is unhealthy
  ```json
  {
    "status": "unhealthy",
    "details": "Database connection failed"
  }
  ```

## Testing with Different Tools

### 1. Using curl
```bash
# Root endpoint
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health
```

### 2. Using httpie (more user-friendly alternative)
```bash
# Root endpoint
http :8000/

# Health check
http :8000/health
```

### 3. Using Python requests
```python
import requests

# Root endpoint
response = requests.get("http://localhost:8000/")
print(response.json())

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())
```

### 4. Using Swagger UI
1. Open `http://localhost:8000/docs` in your browser
2. Find the endpoint you want to test
3. Click "Try it out"
4. Click "Execute"
5. View the response

## API Metadata
- Version: 0.1.0
- License: MIT
- Documentation Format: OpenAPI 3.0 