import hashlib
import os

# Esta funcion calcula el SHA-256 de un archivo
def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:
        while True:
            bloque = archivo.read(4096)
            if not bloque:
                break
            sha256.update(bloque)

    return sha256.hexdigest()

# Nombre del manifiesto
ruta_manifiesto = "SHA256SUMS.txt"

# Carpeta donde estan los archivos a verificar
carpeta_archivos = "archivos"

# Se valida que exista el manifiesto
if not os.path.isfile(ruta_manifiesto):
    print("No existe el archivo SHA256SUMS.txt")
    raise SystemExit

print("Verificando integridad de archivos...\n")

correctos = 0
incorrectos = 0

# Se leen todas las lineas del manifiesto
with open(ruta_manifiesto, "r", encoding="utf-8") as manifiesto:
    for linea in manifiesto:
        linea = linea.strip()

        # Se ignoran lineas vacias
        if not linea:
            continue

        # Cada linea tiene: HASH nombre_archivo
        partes = linea.split(maxsplit=1)

        if len(partes) != 2:
            print("Linea invalida en manifiesto:", linea)
            continue

        hash_guardado = partes[0]
        nombre_archivo = partes[1]

        ruta_archivo = os.path.join(carpeta_archivos, nombre_archivo)

        # Si el archivo no existe, se reporta
        if not os.path.isfile(ruta_archivo):
            print(f"[NO ENCONTRADO] {nombre_archivo}")
            incorrectos += 1
            continue

        # Se recalcula el hash actual
        hash_actual = calcular_sha256(ruta_archivo)

        # Se compara contra el manifiesto
        if hash_actual == hash_guardado:
            print(f"[CORRECTO] {nombre_archivo}")
            correctos += 1
        else:
            print(f"[ALTERADO] {nombre_archivo}")
            incorrectos += 1

print("\nResumen")
print("Correctos :", correctos)
print("Incorrectos:", incorrectos)