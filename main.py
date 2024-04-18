from src.whatsapp import whatsapp
import time

def main():
    wtp=whatsapp()

    condicion=True
    while condicion:

        listaChats=wtp.check_messages()
        wtp.reply_message(listaChats)
    

        
    wtp.log_out()
    


if __name__ == '__main__':
    main()