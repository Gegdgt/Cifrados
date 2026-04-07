from Crypto.PublicKey import RSA

# Se genera un par de claves RSA de 2048 bits
clave = RSA.generate(2048)

# Se exporta la clave privada
clave_privada = clave.export_key()

with open("medisoft_priv.pem", "wb") as archivo_priv:
    archivo_priv.write(clave_privada)

# Se exporta la clave publica
clave_publica = clave.publickey().export_key()

with open("medisoft_pub.pem", "wb") as archivo_pub:
    archivo_pub.write(clave_publica)

print("Claves generadas correctamente.")
print("Clave privada: medisoft_priv.pem")
print("Clave publica: medisoft_pub.pem")