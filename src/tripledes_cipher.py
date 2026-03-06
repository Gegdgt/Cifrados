"""
3DES en modo CBC usando pad/unpad de la librería (NO manual).
"""

from Cryptodome.Cipher import DES3
from Cryptodome.Util.Padding import pad, unpad


def encrypt_3des_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    # Validaciones para 3DES-CBC
    if not isinstance(plaintext, (bytes, bytearray)):
        raise TypeError("plaintext debe ser bytes")
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("key debe ser bytes")
    if len(key) not in (16, 24):
        raise ValueError("La clave 3DES debe ser de 16 o 24 bytes")
    if not isinstance(iv, (bytes, bytearray)):
        raise TypeError("iv debe ser bytes")
    if len(iv) != 8:
        raise ValueError("El IV para 3DES-CBC debe ser de 8 bytes")

    cipher = DES3.new(bytes(key), DES3.MODE_CBC, iv=bytes(iv))

    # Padding PKCS#7 con la librería para bloque de 8
    padded = pad(bytes(plaintext), 8)

    return cipher.encrypt(padded)


def decrypt_3des_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    # Validaciones para 3DES-CBC
    if not isinstance(ciphertext, (bytes, bytearray)):
        raise TypeError("ciphertext debe ser bytes")
    if len(ciphertext) == 0 or (len(ciphertext) % 8) != 0:
        raise ValueError("ciphertext debe ser múltiplo de 8 y no vacío")
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("key debe ser bytes")
    if len(key) not in (16, 24):
        raise ValueError("La clave 3DES debe ser de 16 o 24 bytes")
    if not isinstance(iv, (bytes, bytearray)):
        raise TypeError("iv debe ser bytes")
    if len(iv) != 8:
        raise ValueError("El IV para 3DES-CBC debe ser de 8 bytes")

    cipher = DES3.new(bytes(key), DES3.MODE_CBC, iv=bytes(iv))

    padded_plaintext = cipher.decrypt(bytes(ciphertext))

    return unpad(padded_plaintext, 8)