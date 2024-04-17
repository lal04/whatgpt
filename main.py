from src.whatsapp import whatsapp

def main():
    wtp=whatsapp()
    pendientes=wtp.check_messages()
    
    wtp.reply_message(pendientes)
    
    input('presione enter')
    wtp.log_out()
 


if __name__ == '__main__':
    main()