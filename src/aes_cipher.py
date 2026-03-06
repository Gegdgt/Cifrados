"""
AES-256 ECB vs CBC aplicado a los bytes de píxeles de una imagen (análisis visual).
"""

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from PIL import Image
from .utils import generate_iv


def _image_to_raw_bytes(path: str):
    # Abre la imagen y devuelve (img_mode, size, raw_bytes)
    img = Image.open(path)
    img = img.convert("RGBA")
    raw = img.tobytes()
    return img.mode, img.size, raw


def _raw_bytes_to_image(mode: str, size: tuple, raw: bytes, out_path: str):
    img = Image.frombytes("RGBA", size, raw)
    img.save(out_path)


def encrypt_image_aes_ecb(in_path: str, out_path: str, key: bytes) -> None:
    # AES-256 en ECB
    if len(key) != 32:
        raise ValueError("AES-256 requiere clave de 32 bytes")

    mode, size, raw = _image_to_raw_bytes(in_path)

    cipher = AES.new(key, AES.MODE_ECB)

    padded = pad(raw, AES.block_size)
    enc = cipher.encrypt(padded)

    # Recortamos al tamaño original para poder reconstruir RGBA
    enc_raw = enc[:len(raw)]

    _raw_bytes_to_image(mode, size, enc_raw, out_path)


def encrypt_image_aes_cbc(in_path: str, out_path: str, key: bytes) -> bytes:
    # AES-256 en CBC con IV aleatorio
    if len(key) != 32:
        raise ValueError("AES-256 requiere clave de 32 bytes")

    mode, size, raw = _image_to_raw_bytes(in_path)

    iv = generate_iv(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    padded = pad(raw, AES.block_size)
    enc = cipher.encrypt(padded)

    enc_raw = enc[:len(raw)]

    _raw_bytes_to_image(mode, size, enc_raw, out_path)

    # Para CBC, el IV debe guardarse/transmitirse junto al ciphertext en un caso real
    return iv


def decrypt_image_aes_cbc(in_path: str, out_path: str, key: bytes, iv: bytes) -> None:
    # Esta función es opcional para la parte visual, pero útil para completar el ciclo
    if len(key) != 32:
        raise ValueError("AES-256 requiere clave de 32 bytes")
    if len(iv) != AES.block_size:
        raise ValueError("IV inválido para AES-CBC")

    mode, size, raw = _image_to_raw_bytes(in_path)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    padded_plain = cipher.decrypt(pad(raw, AES.block_size))
    plain = unpad(padded_plain, AES.block_size)

    plain_raw = plain[:len(raw)]

    _raw_bytes_to_image(mode, size, plain_raw, out_path)