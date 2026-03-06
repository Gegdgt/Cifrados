"""
Funciones auxiliares: generación de llaves e IV, y padding PKCS#7 manual.
"""

import secrets
from Cryptodome.Cipher import DES3


def generate_des_key() -> bytes:
    """
    Genera una clave DES aleatoria de 8 bytes (64 bits).
    Nota: DES usa efectivamente 56 bits (los otros 8 son de paridad).
    """
    return secrets.token_bytes(8)


def generate_3des_key(key_option: int = 2) -> bytes:
    """
    Genera una clave 3DES segura de 16 bytes (2-key) o 24 bytes (3-key).
    Ajusta paridad y evita claves débiles.
    """
    if key_option not in (2, 3):
        raise ValueError("key_option debe ser 2 o 3")

    key_len = 16 if key_option == 2 else 24

    while True:
        raw_key = secrets.token_bytes(key_len)
        try:
            return DES3.adjust_key_parity(raw_key)
        except ValueError:
            continue


def generate_aes_key(key_size_bits: int = 256) -> bytes:
    """
    Genera una clave AES aleatoria.
    Para AES-256: key_size_bits = 256 -> 32 bytes.
    """
    if key_size_bits not in (128, 192, 256):
        raise ValueError("key_size_bits debe ser 128, 192 o 256")
    return secrets.token_bytes(key_size_bits // 8)


def generate_iv(block_size: int) -> bytes:
    """
    Genera un vector de inicialización (IV) aleatorio.
    """
    return secrets.token_bytes(block_size)


def pkcs7_pad(data: bytes, block_size: int = 8) -> bytes:
    """
    Implementa padding PKCS#7 según RFC 5652.
    Si el mensaje ya es múltiplo exacto del bloque, agrega un bloque completo.
    """
    padding_len = block_size - (len(data) % block_size)
    if padding_len == 0:
        padding_len = block_size

    padding = bytes([padding_len] * padding_len)
    return data + padding


def pkcs7_unpad(data: bytes) -> bytes:
    """
    Elimina padding PKCS#7 de los datos.
    """
    if not data:
        raise ValueError("Padding inválido")

    padding_len = data[-1]

    if padding_len < 1 or padding_len > len(data):
        raise ValueError("Padding inválido")

    if data[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Padding inválido")

    return data[:-padding_len]