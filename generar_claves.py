from Crypto.PublicKey import RSA

# Tamaño de la llave RSA
RSA_BITS = 2048

# Contraseña para proteger la llave privada
PASSPHRASE = "lab04uvg"

# Genera el par de llaves
key = RSA.generate(RSA_BITS)

# Obtiene la llave privada en formato PEM protegida con contraseña
private_key = key.export_key(
    format="PEM",
    passphrase=PASSPHRASE,
    pkcs=8,
    protection="scryptAndAES128-CBC"
)

# Obtiene la llave pública en formato PEM
public_key = key.publickey().export_key(format="PEM")

# Guarda la llave privada
with open("private_key.pem", "wb") as priv_file:
    priv_file.write(private_key)

# Guarda la llave pública
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("Llaves generadas correctamente.")
print("Archivo creado: private_key.pem")
print("Archivo creado: public_key.pem")