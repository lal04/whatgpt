
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.apigpt import apigpt
import re
from collections import deque

class whatsapp:
    def __init__(self) -> None:
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.gpt=apigpt()
        self.driver.get('https://web.whatsapp.com/')
        print('esperamos que a que inicie sesion con el QR')
        # Esperar a que la página esté completamente cargada (document.readyState)
        # Esperar hasta que un elemento esté visible
        WebDriverWait(self.driver,90).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/span[1]/div/div/div[2]/div[1]')))
       

    def check_messages(self):
        #pendiente de sacar el Try
        
        try:
            #lista de objetos de chats no leidos
            lisChats=[]
            # Encontrar todos los chats
            chats = self.driver.find_elements(By.CSS_SELECTOR, '.x10l6tqk.xh8yej3.x1g42fcv')

            # Iterar sobre cada chat
            for chat in chats:
                # Encontrar todos los spans con aria-label dentro del chat
                spans = chat.find_elements(By.CSS_SELECTOR, 'span[aria-label]')

                # Variable para indicar si hay mensajes no leídos en este chat
                mensajes_no_leidos = False
                
                # Iterar sobre cada span
                for span in spans:
                    # Verificar si el aria-label no está vacío y es diferente de ""
                    if span.get_attribute('aria-label') and "no" in span.get_attribute('aria-label'):
                        mensajes_no_leidos = True
                        n_mensajes=span.get_attribute('aria-label')
                        break  # Salir del bucle si encontramos un mensaje no leído
                
                # Si hay mensajes no leídos, hacer algo, por ejemplo, imprimir el nombre del chat
                if mensajes_no_leidos:
                    nombre_chat = chat.find_element(By.CSS_SELECTOR, 'span[title]').get_attribute('title')
                    print(f"Chat: {nombre_chat}")
                    print(n_mensajes)
                    lisChats.append(chat)
            return lisChats
        except Exception as e:
            print( f'error: {e}')
    def reply_message(self, lisChats):
        try:
            messages=deque(maxlen=10)
            for chat in lisChats:
                chat.click()
                # Encontrar todos los div con la clase "copyable-text"
                divs = self.driver.find_elements(By.CLASS_NAME, "copyable-text")
                # Iterar sobre cada div encontrado
                for div in divs:
                    # Obtener el valor del atributo "data-pre-plain-text" del div
                    header_message = div.get_attribute("data-pre-plain-text")
                    if header_message is not None:
                        rol=re.sub(r'\[[^\]]+\]|:\s*$','', header_message)
                        rol=rol.replace(' ','')
                        messages.append({"role":f"{rol}", "content":f"{div.text.replace("\n", " ")}"})
                print(self.gpt.reply(messages))        

        except Exception as e:
            print(f'error: {e}')

    
                
    def log_out(self):
        
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[6]/div').click()
        
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[6]/span/div/ul/li[12]/div').click()
        
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]/div/div').click()
