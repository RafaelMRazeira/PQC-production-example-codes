"""Client module use example."""
import ast
import base64
import json
import os

import oqs
import requests
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

client_kem = oqs.KeyEncapsulation("Kyber768")
headers = {"accept": "text/plain", "Content-Type": "application/json"}
response = requests.get("http://localhost:5000/create_key", headers=headers).json()
kem_ciphertext, shared_secret_client = client_kem.encap_secret(ast.literal_eval(response["generated_key"]))

uuid = response["uuid"]
message = "Hello, secure world!"
key = shared_secret_client
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(message.encode()) + padder.finalize()
encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

data = {
    "kem_ciphertext": base64.b64encode(kem_ciphertext).decode("utf-8"),
    "encrypted_message": base64.b64encode(encrypted_message).decode("utf-8"),
    "uuid": uuid,
    "iv": base64.b64encode(iv).decode("utf-8"),
}
resp = requests.post("http://localhost:5000/receive_message", headers=headers, data=json.dumps(data))
