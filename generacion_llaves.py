"""
Generador de claves criptográficamente seguras.
"""
import secrets


def generate_des_key():
    """
    Genera una clave DES aleatoria de 8 bytes (64 bits).
    
    Nota: DES usa efectivamente 56 bits (los otros 8 son de paridad),
    pero la clave es de 8 bytes.

    """

    # 8 bytes
    key = secrets.token_bytes(8) 
    return key


def generate_3des_key(key_option: int = 2):
    """
    Genera una clave 3DES aleatoria.   

    """

    # key_option = 2 → 16 bytes (2 claves)
    # key_option = 3 → 24 bytes (3 claves)

    if key_option == 2:
        key = secrets.token_bytes(16)  
    elif key_option == 3:
        key = secrets.token_bytes(24) 
    else:
        raise ValueError("key_option debe ser 2 o 3")

    return key


def generate_aes_key(key_size: int = 256):
    """
    Genera una clave AES aleatoria.
    
    """
    # Convertir bits a bytes: key_size // 8
    key_bytes = key_size // 8  
    
    key = secrets.token_bytes(key_bytes) 
    return key


def generate_iv(block_size: int = 8) -> bytes:
    """
    Genera un vector de inicialización (IV) aleatorio.

    """
    # El IV debe tener el mismo tamaño que el bloque
    iv = secrets.token_bytes(block_size)
    return iv
