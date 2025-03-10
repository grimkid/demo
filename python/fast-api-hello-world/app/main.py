from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="FastAPI Hello World",
    description="A simple FastAPI application demonstrating basic setup",
    version="0.1.0"
)

@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"message": "Hello World"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 