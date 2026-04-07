import hashlib
import os
import sys

# Esta funcion calcula el SHA-256 de un archivo
# Se lee en bloques para que funcione aunque el archivo sea grande
def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:
        while True:
            bloque = archivo.read(4096)
            if not bloque:
                break
            sha256.update(bloque)

    return sha256.hexdigest()

# Se valida que se hayan enviado archivos por consola
if len(sys.argv) < 6:
    print("Uso: python generar_manifiesto.py archivo1 archivo2 archivo3 archivo4 archivo5 ...")
    sys.exit(1)

# Nombre del manifiesto
ruta_manifiesto = "SHA256SUMS.txt"

# Se abre el archivo en modo append para ir agregando el historial
with open(ruta_manifiesto, "a", encoding="utf-8") as manifiesto:
    for ruta in sys.argv[1:]:
        # Se valida que el archivo exista
        if not os.path.isfile(ruta):
            print("No existe:", ruta)
            continue

        # Se calcula el hash del archivo
        hash_archivo = calcular_sha256(ruta)

        # Solo se guarda el nombre del archivo, no toda la ruta
        nombre_archivo = os.path.basename(ruta)

        # Se agrega una linea al historial
        manifiesto.write(f"{hash_archivo} {nombre_archivo}\n")

        print("Agregado al manifiesto:", nombre_archivo)

print("\nManifiesto generado o actualizado correctamente.")