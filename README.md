# Parte 2 – Análisis de Seguridad del Stream Cipher

## 2.1 Variación de la Clave (5 puntos)

Cuando cambia la clave utilizada para generar el keystream, el flujo de bytes pseudoaleatorios cambia completamente.

Esto ocurre porque la clave se convierte en un seed mediante SHA-256, por lo que incluso una pequeña modificación en la clave produce un keystream totalmente diferente.

### Ejemplo

```python
mensaje = "Hola mundo"

clave1 = "mi_clave"
clave2 = "mi_clave_modificada"

c1 = cifrar_stream(mensaje, clave1)
c2 = cifrar_stream(mensaje, clave2)

print("Cipher con clave1:", c1.hex())
print("Cipher con clave2:", c2.hex())
print("Son iguales:", c1 == c2)
```

### Resultado esperado

Los ciphertexts serán completamente distintos.

### Conclusión

Una pequeña variación en la clave genera un keystream diferente, lo que cambia totalmente el resultado del cifrado. Esto es deseable en términos de seguridad.

---

## 2.2 Reutilización del Keystream (5 puntos)

Reutilizar el mismo keystream para cifrar dos mensajes diferentes es una vulnerabilidad grave.

Si:

```
C1 = M1 ⊕ KS  
C2 = M2 ⊕ KS  
```

Entonces un atacante puede calcular:

```
C1 ⊕ C2 = M1 ⊕ M2
```

Esto elimina el keystream y expone información sobre los mensajes originales.

### Ejemplo

```python
m1 = "Ataque al amanecer"
m2 = "Defensa al anochecer"

clave = "misma_clave"

c1 = cifrar_stream(m1, clave)
c2 = cifrar_stream(m2, clave)

xor_cipher = bytes(a ^ b for a, b in zip(c1, c2))

print("C1 XOR C2:", xor_cipher)
```

### Análisis

El resultado es el XOR de los mensajes originales.

Si un atacante conoce parte de uno de los mensajes, puede recuperar información del otro.

### Conclusión

Nunca se debe reutilizar el mismo keystream con diferentes mensajes.
En sistemas reales se usan nonces o IVs únicos.

---

## 2.3 Longitud del Keystream (5 puntos)

### Keystream más corto que el mensaje

Si el keystream es más corto y se reutiliza cíclicamente, se convierte en un cifrado tipo Vigenère, lo que introduce patrones repetitivos y vulnerabilidades estadísticas.

### Keystream igual al mensaje

Es el caso correcto para un stream cipher.
Cada byte del mensaje se cifra con un byte único del keystream.

### Keystream más largo que el mensaje

No afecta negativamente la seguridad, simplemente sobran bytes no utilizados.

### Conclusión

El keystream debe tener exactamente la misma longitud que el mensaje y no reutilizarse.

---

## 2.4 Consideraciones Prácticas (5 puntos)

En un entorno real de producción se deben considerar al menos los siguientes aspectos:

1. **PRNG criptográficamente seguro**
   No usar `random`. Se debe usar un generador seguro como ChaCha20 o AES-CTR.

2. **Uso de nonce o IV único**
   Cada cifrado debe usar un nonce distinto para evitar reutilización del keystream.

3. **Protección de la clave**
   La clave debe almacenarse de forma segura y derivarse mediante funciones como PBKDF2, Argon2 o scrypt.

4. **Autenticación del mensaje**
   Un stream cipher por sí solo no protege contra modificaciones.
   Debe combinarse con un MAC o usar un modo autenticado (ej. ChaCha20-Poly1305).

---

# Parte 3 – Análisis de Seguridad del Stream Cipher

## 3.1 Seguridad del Generador Pseudoaleatorio

El sistema implementado utiliza `random.Random`, que está basado en el algoritmo **Mersenne Twister**.

Aunque es determinístico y útil para propósitos educativos, **no es criptográficamente seguro**.

### Problemas principales:

* Puede predecirse si se conocen suficientes salidas.
* No está diseñado para aplicaciones de seguridad.
* Es vulnerable a ataques de reconstrucción de estado interno.

### Impacto

Si un atacante logra predecir el keystream, puede descifrar todos los mensajes cifrados con esa clave.

---

## 3.2 Ataque por Reutilización del Keystream

Si se usa la misma clave sin ningún valor adicional (nonce/IV), el keystream será idéntico.

Esto permite el ataque:

```
C1 ⊕ C2 = M1 ⊕ M2
```

Esto elimina completamente el keystream del cálculo.

### Consecuencia

* Un atacante puede recuperar información parcial.
* Si conoce uno de los mensajes, puede recuperar el otro.
* Se rompe la confidencialidad.

---

## 3.3 Sensibilidad a la Clave

El uso de SHA-256 para derivar el seed introduce el efecto avalancha:

* Cambios mínimos en la clave generan cambios grandes en el keystream.
* Esto es positivo desde el punto de vista criptográfico.

Sin embargo:

* No hay protección contra ataques de fuerza bruta.
* Si la clave es débil, el sistema es vulnerable.

---

## 3.4 Ausencia de Autenticación

El sistema implementado solo cifra datos, pero **no protege contra modificaciones**.

Un atacante podría:

* Alterar bits del ciphertext.
* Cambiar el mensaje descifrado sin conocer la clave.

Esto se debe a que el cifrado XOR es completamente maleable.

Ejemplo:

Si un atacante cambia un bit en el ciphertext, ese mismo bit cambiará en el mensaje descifrado.

---

## 3.5 Comparación con Implementaciones Reales

En producción, un sistema seguro debería:

* Usar un generador criptográficamente seguro.
* Usar un nonce único por mensaje.
* Incluir autenticación (MAC o modo autenticado).
* Derivar claves con funciones resistentes a fuerza bruta.

Ejemplos reales:

* ChaCha20
* AES en modo CTR con autenticación (GCM)
* ChaCha20-Poly1305

---
