# Proyecto Cryptography

Este proyecto proporciona una implementación sencilla de cifrado y descifrado de texto utilizando la biblioteca Fernet de Python. El script permite al usuario ingresar un texto, lo cifra utilizando una clave generada aleatoriamente, guarda el texto cifrado en un archivo, lo descifra y finalmente guarda el texto descifrado en otro archivo.

## Características

- Cifrado seguro utilizando Fernet (implementación de cifrado simétrico)
- Generación aleatoria de claves criptográficas
- Almacenamiento de mensajes cifrados y descifrados en archivos
- Interfaz de consola simple para la entrada de texto

## Estructura de Archivos

```
proyecto_cryptography/
│
├── 1_cryptography.py    # Script principal de cifrado
│
└── archivos/            # Directorio creado automáticamente
    ├── cifrado.txt      # Archivo que contiene el texto cifrado
    └── descifrado.txt   # Archivo que contiene el texto descifrado
```

## Requisitos

- Python 3.6 o superior
- Biblioteca `cryptography`
- Microsoft Visual C++ Redistributable (para usuarios de Windows)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/proyecto_cryptography.git
   cd proyecto_cryptography
   ```

2. Crea un entorno virtual (recomendado):
   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install --upgrade pip setuptools wheel
   pip install cryptography
   ```

## Solución de Problemas

### Error de DLL al importar Rust

Si encuentras un error como `ImportError: DLL load failed while importing _rust: No se encontró el proceso especificado`, prueba estas soluciones:

1. Instala/actualiza Microsoft Visual C++ Redistributable:
   - Descarga e instala desde [aquí](https://aka.ms/vs/17/release/vc_redist.x64.exe)
   - Reinicia tu computadora

2. Si el problema persiste, intenta instalar una versión específica de cryptography:
   ```
   pip uninstall cryptography
   pip install cryptography==38.0.4
   ```

3. Asegúrate de que tienes todas las herramientas de construcción necesarias:
   ```
   pip install wheel setuptools msvc-runtime
   ```

## Uso

1. Ejecuta el script:
   ```
   python 1_cryptography.py
   ```

2. Introduce el texto que deseas cifrar cuando se te solicite.

3. El programa mostrará:
   - El texto original
   - El texto cifrado
   - El texto descifrado

4. Los archivos cifrado.txt y descifrado.txt se crearán en el directorio "archivos".

## Cómo Funciona

1. El script genera una clave criptográfica aleatoria
2. Convierte el texto ingresado a bytes y lo cifra
3. Guarda el texto cifrado en un archivo
4. Descifra el texto usando la misma clave
5. Guarda el texto descifrado en un archivo diferente


---

*Nota: Este proyecto es con fines educativos para demostrar conceptos básicos de criptografía. No se recomienda para aplicaciones que requieran seguridad crítica sin modificaciones adicionales.*