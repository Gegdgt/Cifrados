# Hashes y Firmas – Laboratorio

Gabriel García - 21352

---

## Descripción del proyecto

Este laboratorio consiste en la implementación de diferentes mecanismos de seguridad basados en funciones hash y criptografía. El objetivo principal es comprender cómo se utilizan los hashes para garantizar la integridad de archivos, proteger contraseñas y autenticar información.

Se trabajó con distintos algoritmos como MD5, SHA-1, SHA-256 y SHA3-256, comparando su comportamiento y seguridad. Además, se implementaron herramientas para verificar integridad de archivos, analizar contraseñas filtradas y preparar bases para autenticidad mediante firmas digitales.

El laboratorio se basa en un escenario donde una empresa distribuye software crítico y necesita protegerlo contra modificaciones maliciosas.

---

## Estructura del proyecto

Los ejercicios se encuentran separados en distintos archivos:

* **Parte 1 – Comparación de algoritmos**

  * `explorar_hashes.py`

* **Parte 2 – Verificación de contraseñas filtradas**

  * `verificar_passwords.py`

* **Parte 3 – Verificación de integridad**

  * `generar_manifiesto.py`
  * `verificar_paquete.py`

* **Parte 4 – Firma digital**

  * `generar_claves_rsa.py`
  * `firmar_manifiesto.py`

* **Parte 5 – Verificación de firma**

  * `verificar_firma.py`

---

## Instrucciones de instalación y uso

### Requisitos

* Python 3.x
* Librerías:

  * hashlib
  * requests
  * pycryptodome

Instalar dependencias:

```bash
pip install requests pycryptodome
```

---

## Ejecución

### Parte 1

```bash
python explorar_hashes.py
```

### Parte 2

```bash
python verificar_passwords.py
```

### Parte 3

Generar manifiesto:

```bash
python generar_manifiesto.py archivos/archivo1.txt archivos/archivo2.txt archivos/archivo3.txt archivos/archivo4.txt archivos/archivo5.txt
```

Verificar integridad:

```bash
python verificar_paquete.py
```

### Parte 4

Generar claves:

```bash
python generar_claves_rsa.py
```

Firmar manifiesto:

```bash
python firmar_manifiesto.py
```

### Parte 5

Verificar firma:

```bash
python verificar_firma.py
```

---

## Ejemplos de ejecución

### Parte 1

```
Bits distintos entre ambos hashes SHA-256: X
```

---

### Parte 2

```
admin → millones de filtraciones
123456 → millones de filtraciones
hospital → miles
medisoft2024 → bajo o 0
```

---

### Parte 3

```
[CORRECTO] archivo1.txt
[ALTERADO] archivo3.txt
```

---

### Parte 5

```
Firma valida: el manifiesto fue firmado correctamente
Firma invalida: el manifiesto fue modificado
```

---

## Parte 1 – Comparación de algoritmos

### Pregunta 1

¿Cuántos bits cambiaron entre los dos hashes SHA-256? ¿Qué propiedad demuestra esto?

Respuesta:
Cambiaron X bits entre ambos hashes. Esto demuestra el efecto avalancha, donde un cambio mínimo en la entrada genera una salida completamente diferente.

---

## Parte 5 – Verificación de autenticidad

### Pregunta

¿Por qué la firma es válida? ¿Qué sucede al ejecutar verificar_paquete.py?

Respuesta:
La firma es válida porque el archivo firmado (`SHA256SUMS.txt`) no ha sido modificado. La firma digital protege la integridad y autenticidad del manifiesto, no de los archivos individuales.

Al ejecutar `verificar_paquete.py`, se recalculan los hashes de los archivos reales. Si alguno fue modificado, el sistema lo detecta como alterado, aunque la firma del manifiesto siga siendo válida.