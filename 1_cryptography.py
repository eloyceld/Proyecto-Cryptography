from cryptography.fernet import Fernet
import os

#  Generar una clave secreta
clave = Fernet.generate_key()
cipher = Fernet(clave)

# Solicitar texto
texto = input("\nDame un texto a cifrar: ")

# Crear directorio si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")

# Cifrar un mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")

mensaje_cifrado = cipher.encrypt(mensaje)
print("Mensaje Cifrado:", mensaje_cifrado)

# Guardar el mensaje cifrado en un archivo
with open("archivos/cifrado.txt", "wb") as file:
    file.write(mensaje_cifrado)

# Descifrar el mensaje
mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode()
print("Mensaje Descifrado:", mensaje_descifrado)

# Guardar el mensaje descifrado en un archivo diferente
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)
