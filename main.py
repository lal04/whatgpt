from src.whatsapp import whatsapp
from src.apigpt import apigpt
import time

def main():

    apigpt().asistente()

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