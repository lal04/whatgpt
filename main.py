from src.whatsapp import whatsapp
from src.apigpt import apigpt
from src.chat_threads import chat_threads
import time

def main():
    hilo='lista 5'

    if chat_threads().check_existence(hilo) is False:
        chat_threads().add_thread_id(hilo)
    else:
        print('ya existe')


    # wtp=whatsapp()

    # condicion=True
    # while condicion:

    #     listaChats=wtp.check_messages()
    #     wtp.reply_message(listaChats)

    #     if input('fin si deseas detener el proceso')== 'fin':
    #         condicion=False
    

        
    # wtp.log_out()
    


if __name__ == '__main__':
    main()