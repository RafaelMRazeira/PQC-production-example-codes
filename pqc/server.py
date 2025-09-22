"""Server API use example."""
import os

import oqs
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Server side: Generate keypair
alg = "Kyber768"  # we can use too the new ML-KEM-768
server_kem = oqs.KeyEncapsulation(alg)
server_public_key = server_kem.generate_keypair()
server_private_key = server_kem.export_secret_key()  # Store securely

# Client side: Encapsulate shared secret and encrypt message
client_kem = oqs.KeyEncapsulation(alg)
kem_ciphertext, shared_secret_client = client_kem.encap_secret(server_public_key)

message = "Hello, secure world!"
key = shared_secret_client  # 32-byte shared secret
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(message.encode()) + padder.finalize()
encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

# Simulate sending: kem_ciphertext, iv, encrypted_message to server

# Server side: Decapsulate and decrypt
shared_secret_server = server_kem.decap_secret(kem_ciphertext)
assert shared_secret_server == shared_secret_client  # For demo; remove in prod

cipher = Cipher(algorithms.AES(shared_secret_server), modes.CBC(iv))
decryptor = cipher.decryptor()
padded = decryptor.update(encrypted_message) + decryptor.finalize()
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
decrypted_data = unpadder.update(padded) + unpadder.finalize()
decrypted_message = decrypted_data.decode()

print(f"Decrypted message: {decrypted_message}")
