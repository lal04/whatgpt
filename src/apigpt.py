from openai import OpenAI
from dotenv import load_dotenv
import os
from collections import deque

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear una instancia de OpenAI con tu API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lista de mensajes, que tendra como maximo 4 elementos 
messages = deque(maxlen=4)

# Lista de mensajes, inicia sin un mensaje del sistema
messages.append({"role": "system", "content": "eres un asitente virtual"})
# Solicita al usuario ingresar una pregunta
print('"fin" para terminar la charla: ')
input_message = input('>')
print('======================================')
# Agrega la pregunta final del usuario para cerrar la conversación
messages.append({"role": "user", "content": input_message})

# Inicia el bucle para continuar la conversación hasta que el usuario escriba "fin"
while input_message != 'fin':
    # Genera una respuesta usando el modelo GPT-3.5 turbo
    completion = client.chat.completions.create(
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
