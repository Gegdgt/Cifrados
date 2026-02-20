"""
Módulo de padding PKCS#7 para cifrados de bloque.
Implementación manual sin usar bibliotecas externas.
"""

def pkcs7_pad(data: bytes, block_size: int = 8):
    """
    Implementa padding PKCS#7 según RFC 5652.
    
    Regla: Si faltan N bytes para completar el bloque,
    agregar N bytes, cada uno con el valor N (recuerden seguir la regla de pkcs#7).
    
    Importante: Si el mensaje es múltiplo exacto del tamaño
    de bloque, se agrega un bloque completo de padding.
    
    Examples:
        >>> pkcs7_pad(b"HOLA", 8).hex()
        '484f4c4104040404'
        
        >>> pkcs7_pad(b"12345678", 8).hex()
        '31323334353637380808080808080808'
    """
    
    # Calculamos cuantos bytes faltan para completar el bloque
    padding_len = block_size - (len(data) % block_size)

    # Si es múltiplo exacto, agregamos un bloque completo
    if padding_len == 0:
        padding_len = block_size

    # Creamos bytes de padding con valor igual a padding_len
    padding = bytes([padding_len] * padding_len)

    # Retornamos datos originales + padding
    return data + padding


def pkcs7_unpad(data: bytes) -> bytes:
    """
    Elimina padding PKCS#7 de los datos.
    
    Examples:
        >>> padded = pkcs7_pad(b"HOLA", 8)
        >>> pkcs7_unpad(padded)
        b'HOLA'
    """

    # El ultimo byte indica cuantos bytes de padding hay
    padding_len = data[-1]

    if padding_len < 1 or padding_len > len(data):
        raise ValueError("Padding inválido")

    # Verificamos que todos los bytes tengan el mismo valor
    if data[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Padding inválido")

    # Mensaje sin padding
    return data[:-padding_len]
