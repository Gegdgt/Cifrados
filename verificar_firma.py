from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Archivo del manifiesto
archivo_manifiesto = "SHA256SUMS.txt"

# Archivo de firma
archivo_firma = "SHA256SUMS.sig"

# Archivo de clave publica
archivo_clave_publica = "medisoft_pub.pem"

# Se lee el contenido del manifiesto
with open(archivo_manifiesto, "rb") as f:
    datos = f.read()

# Se calcula el hash SHA-256 del manifiesto
hash_obj = SHA256.new(datos)

# Se lee la firma guardada
with open(archivo_firma, "rb") as f:
    firma = f.read()

# Se carga la clave publica
with open(archivo_clave_publica, "rb") as f:
    clave_publica = RSA.import_key(f.read())

# Se intenta validar la firma
try:
    pkcs1_15.new(clave_publica).verify(hash_obj, firma)
    print("Firma valida: el manifiesto fue firmado por MediSoft y no ha sido alterado.")
except (ValueError, TypeError):
    print("Firma invalida: el manifiesto fue modificado o la firma no corresponde.")