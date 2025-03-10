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

### 3. Dummy Endpoints (`/dummy`)

A collection of endpoints demonstrating different HTTP methods and request/response patterns.

#### GET `/dummy`
Demonstrates query parameters and headers.
```bash
# Basic request
curl "http://localhost:8000/dummy?name=test&age=25"

# With custom header
curl "http://localhost:8000/dummy?name=test&age=25" \
  -H "X-Custom-Header: test-header"
```

#### POST `/dummy`
Creates a new resource with JSON body.
```bash
curl -X POST http://localhost:8000/dummy \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test",
    "value": 42,
    "tags": ["tag1", "tag2"]
  }'
```

#### PUT `/dummy/{item_id}`
Updates an existing resource.
```bash
curl -X PUT http://localhost:8000/dummy/123 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test",
    "value": 42,
    "tags": ["tag1", "tag2"]
  }'
```

#### PATCH `/dummy/{item_id}`
Partially updates a resource.
```bash
curl -X PATCH http://localhost:8000/dummy/123 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "updated-name"
  }'
```

#### DELETE `/dummy/{item_id}`
Deletes a resource.
```bash
# Basic delete
curl -X DELETE http://localhost:8000/dummy/123

# Force delete
curl -X DELETE "http://localhost:8000/dummy/123?force=true"
```

#### OPTIONS `/dummy`
Returns allowed methods.
```bash
curl -X OPTIONS http://localhost:8000/dummy
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

## Request/Response Models

### DummyRequest Model
```json
{
  "name": "string",
  "value": "integer",
  "tags": ["string"]
}
```

### DummyResponse Model
```json
{
  "message": "string",
  "request_info": {
    "headers": {},
    "query_params": {},
    "body": {}
  },
  "status": "success"
}
```

## Request Logging

All dummy endpoints log request information including:
- HTTP Method
- URL
- Headers
- Query Parameters
- Request Body (if present)

You can see these logs in the server console.

## Testing with Different Tools

### 1. Using curl
Examples provided above for each endpoint.

### 2. Using httpie
```bash
# GET request
http :8000/dummy name==test age==25 X-Custom-Header:test-header

# POST request
http POST :8000/dummy name=test value:=42 tags:='["tag1", "tag2"]'
```

### 3. Using Python requests
```python
import requests

# GET request
response = requests.get(
    "http://localhost:8000/dummy",
    params={"name": "test", "age": 25},
    headers={"X-Custom-Header": "test-header"}
)

# POST request
response = requests.post(
    "http://localhost:8000/dummy",
    json={
        "name": "test",
        "value": 42,
        "tags": ["tag1", "tag2"]
    }
)
```

### 4. Using Swagger UI
1. Open `http://localhost:8000/docs` in your browser
2. Find the endpoint you want to test
3. Click "Try it out"
4. Fill in the parameters/body
5. Click "Execute"
6. View the response

## API Metadata
- Version: 0.1.0
- License: MIT
- Documentation Format: OpenAPI 3.0 