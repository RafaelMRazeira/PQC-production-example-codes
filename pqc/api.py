"""Main API router that includes all endpoint-specific routers."""
from fastapi import APIRouter

from pqc.endpoints import create_key, receive_message

api_router = APIRouter()

api_router.include_router(create_key.router, prefix="", tags=["create_key"])
api_router.include_router(receive_message.router, prefix="", tags=["receive_message"])
