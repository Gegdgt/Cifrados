from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Archivo a firmar
archivo_manifiesto = "SHA256SUMS.txt"

# Se lee el contenido del manifiesto
with open(archivo_manifiesto, "rb") as f:
    datos = f.read()

# Se calcula el hash SHA-256 del archivo
hash_obj = SHA256.new(datos)

# Se carga la clave privada
with open("medisoft_priv.pem", "rb") as f:
    clave_privada = RSA.import_key(f.read())

# Se firma el hash
firma = pkcs1_15.new(clave_privada).sign(hash_obj)

# Se guarda la firma en archivo binario
with open("SHA256SUMS.sig", "wb") as f:
    f.write(firma)

print("Manifiesto firmado correctamente.")
print("Firma guardada en SHA256SUMS.sig")