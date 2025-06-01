import hashlib
from cryptography.fernet import Fernet
import base64
import os

def generate_key(password: str) -> bytes:
    # Deriva una clave de 32 bytes a partir de la contraseña usando SHA256
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def encrypt_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()

