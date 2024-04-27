from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
 # Cargar las variables de entorno desde el archivo .env
load_dotenv()
# Obtener la clave de cifrado desde las variables de entorno
clave = os.getenv("CLAVE_AES")
# Crear un objeto de cifrado
cipher_suite = Fernet(clave)
def verificar(texto):
    try:
        listDecifraso=[]
        with open('chat_threads.txt', 'r') as file:
            # Lee todas las líneas del archivo y las guarda en una lista
            lines = file.readlines()
            # Elimina los caracteres de salto de línea de cada línea
            list_thread = [line.strip() for line in lines]
            for i in list_thread:
                #eliminamos la 'b' y las colillas "'" 
                i = i.replace("'", "")[1:]
                #convertimos a bytes el texto cifrado
                # Descifrar el texto
                texto_descifrado = cipher_suite.decrypt(i.encode())
                #convertimos de bytes a cadena de texto
                listDecifraso.append(texto_descifrado.decode())

        if texto  in listDecifraso:
            return True,''
        else:
            return False, texto
    except:
        print('chat_theads esta vacio')
        return False,''

def agrega(texto):
    # Cifrar el texto
    texto_cifrado = cipher_suite.encrypt(texto.encode())
    # Abrir el archivo en modo de agregado ('a')
    with open('chat_threads.txt', 'a') as archivo:
        # Escribir contenido al final del archivo
        archivo.write(f'{texto_cifrado}\n')
texto_original='hola'
valor=verificar(texto_original)
print(valor)

if valor[0]:
    print('esta en la lista')
else:
    agrega(texto_original)
    print('lo agregamos por que no se encontro')




