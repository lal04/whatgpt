class chat_threads:
    def __init__(self):
        pass
    def check_existence(self,thread_id):
        # Abre el archivo en modo lectura
        with open('chat_threads.txt', 'r') as file:
            # Lee todas las líneas del archivo y las guarda en una lista
            lines = file.readlines()

        # Elimina los caracteres de salto de línea de cada línea
        list_thread = [line.strip() for line in lines]
        if thread_id in list_thread:
            return True
        return False
    def add_thread_id(self, thread_id):
         with open("chat_threads.txt", "a") as archivo:
            # Añadir datos al final del archivo
            archivo.write(f"\n{thread_id}")
        
        
