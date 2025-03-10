from fastapi import FastAPI
from typing import Dict
from app.health import router as health_router
from app.dummy_endpoints import router as dummy_router

app = FastAPI(
    title="FastAPI Hello World",
    description="""
    A simple FastAPI application demonstrating basic setup and API documentation.
    
    ## Features
    * Automatic interactive API documentation
    * Health check endpoint
    * Dummy endpoints demonstrating all HTTP methods
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

# Include routers
app.include_router(health_router)
app.include_router(dummy_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 