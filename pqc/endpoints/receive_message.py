"""Receive Message example module."""
import base64

import oqs
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from fastapi import APIRouter

from pqc.schemas.receive_message import ReceiveMessagePayload, ReceiveMessageResponse
from pqc.settings import logger, redis_cache

router = APIRouter()


@router.post(
    "/receive_message",
    response_model=ReceiveMessageResponse,
)
def receive_message(body: ReceiveMessagePayload):
    """Receive all available sections."""
    alg = "Kyber768"  # we can use too the new ML-KEM-768
    server_kem = oqs.KeyEncapsulation(alg)
    client_uuid = body.uuid
    server_secret_key = redis_cache.get(client_uuid)
    server_kem.secret_key = server_secret_key
    shared_secret_server = server_kem.decap_secret(base64.b64decode(body.kem_ciphertext))
    cipher = Cipher(algorithms.AES(shared_secret_server), modes.CBC(base64.b64decode(body.iv)))
    decryptor = cipher.decryptor()
    padded = decryptor.update(base64.b64decode(body.encrypted_message)) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(padded) + unpadder.finalize()
    decrypted_message = decrypted_data.decode()
    logger.info(f"Message received: {decrypted_message}")
    resp = {"status": str(200), "message": "received!"}
    return resp
