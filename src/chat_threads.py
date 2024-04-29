from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
import pickle
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
        self.cipher_suite = Fernet(self.clave)
        
    def check_existence(self,diccionario):
        try:
            listDecifrado=[]
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
                    texto_descifrado = self.cipher_suite.decrypt(i.encode())
                    #convertimos de bytes a cadena de texto
                    diccionario_recuperado = pickle.loads(texto_descifrado)
                    listDecifrado.append(diccionario_recuperado)
                    
            nombres = [diccionario['nombre'] for diccionario in listDecifrado]
            if diccionario['nombre']  in nombres:
                
                return True,''
            else:
                return False, diccionario
        except:
            print('chat_theads esta vacio')
            return False,''
    def add_thread_id(self, diccionario):
        #convertimos el diccionario a bytes
        bytes_diccionario = pickle.dumps(diccionario)
        # Cifrar el texto
        texto_cifrado = self.cipher_suite.encrypt(bytes_diccionario)
        # Abrir el archivo en modo de agregado ('a')
        with open('chat_threads.txt', 'a') as archivo:
            # Escribir contenido al final del archivo
            archivo.write(f'{texto_cifrado}\n')
            
    
        
        
