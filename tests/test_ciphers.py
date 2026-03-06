import os
from src.utils import (
    generate_des_key,
    generate_3des_key,
    generate_aes_key,
    generate_iv,
    pkcs7_pad,
    pkcs7_unpad,
)
from src.des_cipher import encrypt_des_ecb, decrypt_des_ecb
from src.tripledes_cipher import encrypt_3des_cbc, decrypt_3des_cbc
from src.aes_cipher import encrypt_image_aes_ecb, encrypt_image_aes_cbc


def test_pkcs7_pad_unpad_cases():
    # Casos básicos de padding manual
    m5 = b"ABCDE"
    p5 = pkcs7_pad(m5, 8)
    assert pkcs7_unpad(p5) == m5

    m8 = b"12345678"
    p8 = pkcs7_pad(m8, 8)
    assert pkcs7_unpad(p8) == m8

    m10 = b"ABCDEFGHIJ"
    p10 = pkcs7_pad(m10, 8)
    assert pkcs7_unpad(p10) == m10


def test_des_ecb_with_txt():
    print("\n\n\n1.1 DES ECB con padding manual")

    # Leer archivo de entrada
    with open("txt/des.txt", "rb") as f:
        data = f.read()

    key = generate_des_key()

    ct = encrypt_des_ecb(data, key)
    pt = decrypt_des_ecb(ct, key)

    # Guardar resultados
    with open("txt/des_encrypted.bin", "wb") as f:
        f.write(ct)

    with open("txt/des_decrypted.txt", "wb") as f:
        f.write(pt)

    print("Resultado:")
    print("Texto original:", data.decode(errors="ignore"))
    print("Ciphertext (hex):", ct.hex())
    print("Texto descifrado:", pt.decode(errors="ignore"))

    assert pt == data


def test_3des_cbc_with_txt():
    print("\n\n\n1.2 3DES CBC con IV aleatorio")

    # Leer archivo de entrada
    with open("txt/3des.txt", "rb") as f:
        data = f.read()

    key = generate_3des_key(3)
    iv = generate_iv(8)

    ct = encrypt_3des_cbc(data, key, iv)
    pt = decrypt_3des_cbc(ct, key, iv)

    # Guardar resultados
    with open("txt/3des_encrypted.bin", "wb") as f:
        f.write(ct)

    with open("txt/3des_decrypted.txt", "wb") as f:
        f.write(pt)

    print("Resultado:")
    print("Texto original:", data.decode(errors="ignore"))
    print("IV (hex):", iv.hex())
    print("Ciphertext (hex):", ct.hex())
    print("Texto descifrado:", pt.decode(errors="ignore"))

    assert pt == data


def test_aes_image_ecb_vs_cbc():
    print("\n\n\n1.3 AES-256 ECB vs CBC")

    key = generate_aes_key(256)

    in_path = os.path.join("images", "original.png")
    out_ecb = os.path.join("images", "aes_ecb.png")
    out_cbc = os.path.join("images", "aes_cbc.png")

    iv = encrypt_image_aes_cbc(in_path, out_cbc, key)
    encrypt_image_aes_ecb(in_path, out_ecb, key)

    print("Resultado:")
    print("Imagen original:", in_path)
    print("AES-ECB:", out_ecb)
    print("AES-CBC:", out_cbc)
    print("IV CBC (hex):", iv.hex())
    print("Abrir imágenes para comparar patrones visuales")

    assert os.path.exists(out_ecb)
    assert os.path.exists(out_cbc)