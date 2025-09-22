"""Crud Schemas."""
from pydantic import BaseModel, Field


class ReceiveMessageResponse(BaseModel):
    """Status request model."""

    status: str = Field(..., description="Status of the document processing")
    message: str = Field(..., description="Message status")


class ReceiveMessagePayload(BaseModel):
    """Status request model."""

    kem_ciphertext: str = Field(..., description="Kem Cyphertext.")
    encrypted_message: str = Field(..., description="Encrypted Message.")
    uuid: str = Field(..., description="Client's uuid.")
    iv: str = Field(..., description="Client's iv.")
