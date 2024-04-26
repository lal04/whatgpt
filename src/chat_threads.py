from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
class chat_threads:
    def __init__(self):
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()
        # Obtener la clave de cifrado desde las variables de entorno
        self.clave = os.getenv("CLAVE_AES")
        # Verificar si la clave está presente
        if self.clave is None:
            raise ValueError("La clave de cifrado no está definida en el archivo .env")
        # Crear un objeto de cifrado
        self.cipher_suite = Fernet(self.clave.encode())
        
    def check_existence(self,thread_id):
        
        with open('chat_threads.txt', 'r') as file:
            # Lee todas las líneas del archivo y las guarda en una lista
            lines = file.readlines()

        # Elimina los caracteres de salto de línea de cada línea
        list_thread = [line.strip() for line in lines]
        print(list_thread)
        #lista_textos_decifrados = [self.cipher_suite.decrypt(texto_cifrado) for texto_cifrado in list_thread]
        #print(lista_textos_decifrados)
        if thread_id in list_thread:
            
            return True
        
        else:
            # Cifrar el texto
            cifrado= self.cipher_suite.encrypt(thread_id.encode())
            # Abre el archivo en modo lectura
            return False,cifrado
    def add_thread_id(self, thread_id):
         with open("chat_threads.txt", "a") as archivo:
            # Añadir datos al final del archivo
            thread_id=thread_id[1]
            print(type(thread_id))
            archivo.write(f"\n{thread_id}")
        
        
