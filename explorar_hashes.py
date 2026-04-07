import hashlib

# Texto original
texto_1 = "MediSoft-v2.1.0"

# Texto con cambio de capitalización
texto_2 = "medisoft-v2.1.0"

# Lista de algoritmos a comparar
algoritmos = [
    ("MD5", "md5", 128),
    ("SHA-1", "sha1", 160),
    ("SHA-256", "sha256", 256),
    ("SHA3-256", "sha3_256", 256)
]

# Esta funcion calcula el hash hexadecimal de un texto
def calcular_hash(texto, algoritmo):
    return hashlib.new(algoritmo, texto.encode("utf-8")).hexdigest()

# Esta funcion cuenta cuantos bits cambiaron entre dos hashes
# Se usa XOR para encontrar diferencias bit a bit
def contar_bits_distintos(hash_1, hash_2):
    numero_1 = int(hash_1, 16)
    numero_2 = int(hash_2, 16)

    xor_resultado = numero_1 ^ numero_2

    return bin(xor_resultado).count("1")

# Encabezado de la tabla
print("=" * 120)
print(f'{"Texto":20} {"Algoritmo":12} {"Bits":6} {"Hex chars":10} {"Hash"}')
print("=" * 120)

# Aqui se recorren ambos textos y todos los algoritmos
# Se imprime una fila por cada combinacion
for texto in [texto_1, texto_2]:
    for nombre_visible, nombre_hashlib, bits in algoritmos:
        valor_hash = calcular_hash(texto, nombre_hashlib)
        longitud_hex = len(valor_hash)

        print(f'{texto:20} {nombre_visible:12} {bits:<6} {longitud_hex:<10} {valor_hash}')

print("=" * 120)

# Se calcula el SHA-256 de ambos textos para comparar
sha256_texto_1 = calcular_hash(texto_1, "sha256")
sha256_texto_2 = calcular_hash(texto_2, "sha256")

# Aqui se cuentan los bits distintos entre ambos hashes
bits_distintos = contar_bits_distintos(sha256_texto_1, sha256_texto_2)

print("\nComparacion SHA-256")
print("-" * 40)
print("Texto 1:", texto_1)
print("SHA-256:", sha256_texto_1)
print()
print("Texto 2:", texto_2)
print("SHA-256:", sha256_texto_2)
print()
print("Bits distintos entre ambos hashes SHA-256:", bits_distintos)