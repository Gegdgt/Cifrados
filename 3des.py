# Tuve que cambiar las librerias porque no me funcionaba con Crypto. 
from Cryptodome.Cipher import DES3
from Cryptodome.Util.Padding import pad, unpad
import secrets
import random


def generate_3des_key(num_keys: int = 3) -> bytes:
    # Genera una clave 3DES segura (16 bytes para 2-key, 24 bytes para 3-key)
    if num_keys not in (2, 3):
        raise ValueError("num_keys debe ser 2 o 3 (2-key=16 bytes, 3-key=24 bytes)")

    key_len = 16 if num_keys == 2 else 24

    while True:
        raw_key = secrets.token_bytes(key_len)
        try:
            # Ajusta paridad y valida que no sea una clave débil
            return DES3.adjust_key_parity(raw_key)
        except ValueError:
            # Si es inválida/débil, se vuelve a generar
            continue


def generate_iv(block_size: int = 8) -> bytes:
    # Genera un IV aleatorio (nonce) para CBC
    if block_size != 8:
        raise ValueError("3DES usa bloque de 8 bytes, block_size debe ser 8")
    return secrets.token_bytes(block_size)


def encrypt_3des_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """    
    Example:
        >>> key = generate_3des_key(2)
        >>> iv = generate_iv(8)
        >>> plaintext = b"Mensaje secreto para 3DES"
        >>> ciphertext = encrypt_3des_cbc(plaintext, key, iv)
        >>> len(ciphertext) % 8
        0  # Debe ser múltiplo de 8 (tamaño de bloque de DES)
    """

    # Valida tipos y tamaños esperados para 3DES-CBC
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

    # Crea el cifrador 3DES en modo CBC
    cipher = DES3.new(bytes(key), DES3.MODE_CBC, iv=bytes(iv))

    # Aplica padding PKCS7 para que sea múltiplo del tamaño de bloque (8)
    padded = pad(bytes(plaintext), 8)

    # Cifra y retorna el ciphertext
    return cipher.encrypt(padded)


def decrypt_3des_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """    
    Example:
        >>> key = generate_3des_key(2)
        >>> iv = generate_iv(8)
        >>> plaintext = b"Mensaje secreto"
        >>> ciphertext = encrypt_3des_cbc(plaintext, key, iv)
        >>> decrypted = decrypt_3des_cbc(ciphertext, key, iv)
        >>> decrypted == plaintext
        True
    """
    # TODO: Implementar
    # 1. Validar longitud de clave y IV
    # 2. Crear cipher: DES3.new(key, DES3.MODE_CBC, iv=iv)
    # 3. Descifrar
    # 4. Eliminar padding usando unpad() de Crypto.Util.Padding
    # 5. Retornar

    # Valida tamaños esperados para 3DES-CBC
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

    # Crea el descifrador 3DES en modo CBC
    cipher = DES3.new(bytes(key), DES3.MODE_CBC, iv=bytes(iv))

    # Descifra el contenido
    padded_plaintext = cipher.decrypt(bytes(ciphertext))

    # Elimina el padding y retorna el plaintext original
    return unpad(padded_plaintext, 8)




# Genera clave 3DES de 24 bytes (3-key)
key = generate_3des_key(3)

# Genera IV aleatorio de 8 bytes
iv = generate_iv(8)

# Mensaje de prueba
plaintext = b"Mensaje secreto para probar 3DES CBC"

print("Texto original:", plaintext)

# Cifrado
ciphertext = encrypt_3des_cbc(plaintext, key, iv)
print("Ciphertext:", ciphertext)
print("Longitud ciphertext:", len(ciphertext))
print("Multiplo de 8:", len(ciphertext) % 8 == 0)

# Descifrado
decrypted = decrypt_3des_cbc(ciphertext, key, iv)
print("Texto descifrado:", decrypted)

# Validación final
print("Funciona correctamente:", decrypted == plaintext)