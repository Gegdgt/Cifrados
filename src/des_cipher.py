"""
DES en modo ECB con padding PKCS#7 manual.
"""

from Cryptodome.Cipher import DES
from .utils import pkcs7_pad, pkcs7_unpad


def encrypt_des_ecb(plaintext: bytes, key: bytes) -> bytes:
    # Validaciones básicas
    if not isinstance(plaintext, (bytes, bytearray)):
        raise TypeError("plaintext debe ser bytes")
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("key debe ser bytes")
    if len(key) != 8:
        raise ValueError("DES requiere clave de 8 bytes")

    cipher = DES.new(bytes(key), DES.MODE_ECB)

    # Padding manual PKCS#7 para bloque de 8 bytes
    padded = pkcs7_pad(bytes(plaintext), 8)

    return cipher.encrypt(padded)


def decrypt_des_ecb(ciphertext: bytes, key: bytes) -> bytes:
    # Validaciones básicas
    if not isinstance(ciphertext, (bytes, bytearray)):
        raise TypeError("ciphertext debe ser bytes")
    if len(ciphertext) == 0 or (len(ciphertext) % 8) != 0:
        raise ValueError("ciphertext debe ser múltiplo de 8 y no vacío")
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("key debe ser bytes")
    if len(key) != 8:
        raise ValueError("DES requiere clave de 8 bytes")

    cipher = DES.new(bytes(key), DES.MODE_ECB)

    padded_plaintext = cipher.decrypt(bytes(ciphertext))

    # Unpad manual
    return pkcs7_unpad(padded_plaintext)