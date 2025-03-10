from fastapi import FastAPI, status
from typing import Dict

app = FastAPI(
    title="FastAPI Hello World",
    description="""
    A simple FastAPI application demonstrating basic setup and API documentation.
    
    ## Features
    * Automatic interactive API documentation
    * Health check endpoint
    * Modern Python practices
    
    ## Getting Started
    Visit `/docs` for the interactive Swagger documentation.
    """,
    version="0.1.0",
    contact={
        "name": "Your Name",
        "url": "https://github.com/yourusername/fast-api-hello-world",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

@app.get("/",
    response_model=Dict[str, str],
    summary="Root endpoint",
    description="Returns a friendly greeting message",
    tags=["general"]
)
async def read_root() -> Dict[str, str]:
    """
    Root endpoint that returns a greeting message.
    
    Returns:
        Dict[str, str]: A dictionary containing a welcome message
    """
    return {"message": "Hello World"}

@app.get("/health",
    response_model=Dict[str, str],
    summary="Health check endpoint",
    description="Checks if the application is running properly",
    tags=["system"],
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Application is healthy",
            "content": {
                "application/json": {
                    "example": {"status": "healthy"}
                }
            }
        },
        503: {
            "description": "Application is unhealthy",
            "content": {
                "application/json": {
                    "example": {"status": "unhealthy", "details": "Database connection failed"}
                }
            }
        }
    }
)
async def health_check() -> Dict[str, str]:
    """
    Performs a health check of the application.
    
    This endpoint can be used by monitoring tools to check if the application
    is running properly.
    
    Returns:
        Dict[str, str]: A dictionary containing the health status
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 