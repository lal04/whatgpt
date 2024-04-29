from src.whatsapp import whatsapp
from src.apigpt import apigpt
from src.chat_threads import chat_threads as ct


def main():
    

    wtp=whatsapp()

    wtp.check_messages()
    
        
    wtp.log_out()
    


if __name__ == '__main__':
    main()