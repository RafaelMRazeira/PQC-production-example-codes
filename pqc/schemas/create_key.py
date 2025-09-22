"""Crud Schemas."""
from pydantic import BaseModel, Field


class StatusResponse(BaseModel):
    """Status request model."""

    status: str = Field(..., description="Status of the document processing")
    generated_key: bytes = Field(..., description="Status message of the document processing")
    uuid: bytes = Field(..., description="Generated Client uuid")
