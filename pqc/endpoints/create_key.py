"""Crud module."""
import uuid

import oqs
from fastapi import APIRouter

from pqc.schemas.create_key import StatusResponse
from pqc.settings import logger, redis_cache

router = APIRouter()


@router.get("/create_key", response_model=StatusResponse)
def create_key():
    """Get all available sections."""
    alg = "Kyber768"  # we can use too the new ML-KEM-768
    server_kem = oqs.KeyEncapsulation(alg)
    server_public_key = server_kem.generate_keypair()
    server_private_key = server_kem.export_secret_key()
    client_uuid = uuid.uuid4()
    redis_cache.set(str(client_uuid), server_private_key)
    logger.info("Key setted sucessfully.")
    resp = {"status": str(200), "generated_key": str(server_public_key), "uuid": str(client_uuid)}
    return resp
