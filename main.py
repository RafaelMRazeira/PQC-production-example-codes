"""Main FastAPI application file.

This file initializes the FastAPI application and sets up middleware, routers, and error handlers.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from pqc.api import api_router

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="DD8's Orchestrator API",
    description="API to management process in DD8's applications.",
    version="0.0.1",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="")


@app.get("/", include_in_schema=False)
async def health_check():
    """API health check endpoint."""
    return {"status": "healthy", "message": "Welcome to DD8's Scheduler API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
