from openai import OpenAI
from dotenv import load_dotenv
import os
from collections import deque
class apigpt:
    def __init__(self) -> None:
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()
        # Crear una instancia de OpenAI con tu API Key
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Lista de mensajes, que tendra como maximo 4 elementos 
        messages = deque(maxlen=4)
        # Lista de mensajes, inicia sin un mensaje del sistema
        messages.append({"role": "system", "content": "eres un asitente virtual"})
        # Solicita al usuario ingresar una pregunta
        
    def reply(self, messages):
        completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                max_tokens=10,  # Número máximo de tokens en la respuesta
            )
        # Obtiene el contenido de la respuesta generada
        content = completion.choices[0].message.content
        # Obtiene el número total de tokens utilizados en esta consulta
        total_tokens = completion.usage.total_tokens
        print(f"Total de tokens utilizados: {total_tokens}")
        
        return content
 
    def asistente(self):
        # Definir una condición de salida del bucle
        exit_condition = False

        # Comienza el bucle de conversación
        while not exit_condition:
            # Crea un hilo de conversación en la versión beta de OpenAI dentro del bucle
            thread = self.client.beta.threads.create()

            # El usuario envía un mensaje
            user_input = input("Usuario: ")
            message = self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_input,
            )
            # Crea un nuevo run para esta interacción
            run = self.client.beta.threads.runs.create(
                assistant_id=os.getenv("ASSISTANT_ID"),
                thread_id=thread.id,
            )
            # Espera a que el run esté completo y obtén su estado
            run = self.client.beta.threads.runs.poll(
                run_id=run.id,
                thread_id=thread.id,
            )
            # Si el run se completó correctamente, se listan los mensajes en el hilo de conversación
            if run.status == "completed":
                messages = self.client.beta.threads.messages.list(thread_id=thread.id)

                for message in messages:
                    if message.role == "assistant":
                        print("Asistente:", message.content[0].text.value)

                # Verificar si el usuario quiere salir
                exit_condition = user_input.lower() == "salir"

                
                
    def none(self,messages):

        print('"fin" para terminar la charla: ')
        input_message = input('>')
        print('======================================')
        # Agrega la pregunta final del usuario para cerrar la conversación
        messages.append({"role": "user", "content": input_message})

        # Inicia el bucle para continuar la conversación hasta que el usuario escriba "fin"
        while input_message != 'fin':
            # Genera una respuesta usando el modelo GPT-3.5 turbo
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                max_tokens=100,  # Número máximo de tokens en la respuesta
            )

            
            # Obtiene el contenido de la respuesta generada
            content = completion.choices[0].message.content
            # Obtiene el número total de tokens utilizados en esta consulta
            total_tokens = completion.usage.total_tokens
            
            # Agrega la respuesta del modelo a la lista de mensajes como mensaje del usuario
            messages.append({"role": "assistant", "content": content})
            
            # Imprime la respuesta y el total de tokens utilizados
            print(f">{content}")
            print(f"Total de tokens utilizados: {total_tokens}")
            print('======================================')
            # Solicita al usuario una nueva pregunta para continuar la conversación
            input_message = input('>')
            print('======================================')
            messages.append({"role": "user", "content": input_message})


        # Finalmente, imprime la conversación completa (para ver los mensajes de usuario y asistente)
        print("Conversación completa")
