# CIFRADOS – Laboratorio de Block Ciphers

<a id="readme-top"></a>

---

## 📌 Nota importante

Ludwin hice algunos cambios con los nombres de los archivos y en la organización del proyecto para cumplir con la estructura del lab.

---

## 📜 Descripción

Implementación práctica de cifrados por bloques utilizando:

* DES en modo ECB con padding manual PKCS#7
* 3DES en modo CBC con IV aleatorio
* AES-256 en modos ECB y CBC aplicado a imágenes

El laboratorio demuestra diferencias prácticas entre modos de operación y fortalezas de cada algoritmo.

---

## ✨ Parte 1 – Implementación

## 🖥️ Ejecución de la parte 1

### 1️⃣ Activar entorno virtual

```bash
venv\Scripts\activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar pruebas y generación de resultados

```bash
python -m pytest -s
```

---

## 📂 Estructura del Proyecto

```
cifrados/
│
├── src/
│   ├── des_cipher.py
│   ├── tripledes_cipher.py
│   ├── aes_cipher.py
│   └── utils.py
│
├── tests/
│   └── test_ciphers.py
│
├── images/
│   ├── original.png
│   ├── aes_ecb.png
│   └── aes_cbc.png
│
├── txt/
│   ├── des.txt
│   └── 3des.txt
│
├── requirements.txt
└── README.md
```

---

## 📦 Dependencias

* Python 3.12
* PyCryptodome
* Pillow
* Pytest

---

# 🧠 Parte 2 – Análisis Teórico

---

El desarrollo completo de la Parte 2 se encuentra en:

📓 `parte2_analysis.ipynb`