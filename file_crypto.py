import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from aes_crypto import derive_key_from_password


SALT_SIZE = 16
NONCE_SIZE = 12


def encrypt_file(file_data: bytes, password: str) -> bytes:
    """Encrypt file bytes using password-derived AES-256-GCM key."""

    if not file_data:
        raise ValueError("File data cannot be empty.")

    if not password:
        raise ValueError("Password cannot be empty.")

    # Generate random salt
    salt = os.urandom(SALT_SIZE)

    # Generate AES-256 key from password
    key = derive_key_from_password(password, salt)

    # Generate random nonce
    nonce = os.urandom(NONCE_SIZE)

    # AES-256-GCM encryption
    aes = AESGCM(key)

    ciphertext = aes.encrypt(
        nonce,
        file_data,
        None,
    )

    # Format:
    # SALT + NONCE + CIPHERTEXT
    return salt + nonce + ciphertext


def decrypt_file(encrypted_data: bytes, password: str) -> bytes:
    """Decrypt password-protected AES-256-GCM file."""

    if not encrypted_data:
        raise ValueError("Encrypted file cannot be empty.")

    if not password:
        raise ValueError("Password cannot be empty.")

    if len(encrypted_data) < SALT_SIZE + NONCE_SIZE + 16:
        raise ValueError("Invalid encrypted file.")

    # Extract salt
    salt = encrypted_data[:SALT_SIZE]

    # Extract nonce
    nonce = encrypted_data[
        SALT_SIZE:SALT_SIZE + NONCE_SIZE
    ]

    # Extract ciphertext
    ciphertext = encrypted_data[
        SALT_SIZE + NONCE_SIZE:
    ]

    # Generate same AES-256 key
    key = derive_key_from_password(
        password,
        salt,
    )

    # AES-256-GCM decryption
    aes = AESGCM(key)

    decrypted_data = aes.decrypt(
        nonce,
        ciphertext,
        None,
    )

    return decrypted_data