from src.whatsapp import whatsapp
from src.apigpt import apigpt
from src.chat_threads import chat_threads as ct


def main():
    texto_original=b'hola'
    valor=ct().check_existence(texto_original)
    if valor[0]:
        print('esta en la lista')
    else:
        ct().add_thread_id(texto_original)
        print('lo agregamos por que no se encontro')


    # wtp=whatsapp()

    # condicion=|rue
    # while condicion:

    #     listaChats=wtp.check_messages()
    #     wtp.reply_message(listaChats)

    #     if input('fin si deseas detener el proceso')== 'fin':
    #         condicion=False
    

        
    # wtp.log_out()
    


if __name__ == '__main__':
    main()