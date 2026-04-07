import hashlib
import requests

# Lista de contraseñas a evaluar
passwords = ["admin", "123456", "hospital", "medisoft2024"]

# Esta funcion calcula SHA-256 (solo para mostrar)
def hash_sha256(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

# Esta funcion calcula SHA-1 (necesario para HIBP)
def hash_sha1(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

# Esta funcion consulta la API de HIBP usando k-anonymity
def consultar_hibp(hash_sha1):
    prefijo = hash_sha1[:5]   # primeros 5 caracteres
    sufijo = hash_sha1[5:]    # resto del hash

    url = f"https://api.pwnedpasswords.com/range/{prefijo}"

    # Se hace la solicitud a la API
    response = requests.get(url)

    # Si falla la conexion
    if response.status_code != 200:
        print("Error al consultar HIBP")
        return 0

    # La API devuelve lista de sufijos + conteo
    lineas = response.text.splitlines()

    for linea in lineas:
        hash_suffix, count = linea.split(":")

        # Se compara el sufijo con el hash local
        if hash_suffix == sufijo:
            return int(count)

    return 0  # no encontrado

# Encabezado
print("=" * 80)
print(f'{"Password":15} {"SHA-256":64} {"Filtraciones"}')
print("=" * 80)

# Proceso principal
for password in passwords:
    sha256 = hash_sha256(password)
    sha1 = hash_sha1(password)

    # Se consulta si ha sido filtrada
    filtraciones = consultar_hibp(sha1)

    print(f'{password:15} {sha256} {filtraciones}')

print("=" * 80)
