from sympy import Ge
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
import time
import json

import speeches
from user_repository import user_repository
from config import telegram_token

# def pretty(d, indent=0):
#     for key, value in d.items():
#         print('\t' * indent + str(key))
#         if isinstance(value, dict):
#             pretty(value, indent+1)
#         else:
#             print('\t' * (indent+1) + str(value))

class TelegramBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{telegram_token}/'
        self.user_repo = user_repository()


    def Iniciar(self):
        update_id = None
        last_message = self.get_last_message(update_id)
        update_id = int(last_message["update_id"])
        last_chat_id = last_message["message"]["chat"]["id"]

        self.responder(speeches.greetings_speech, last_chat_id)
        next_message, update_id = self.get_next_message(update_id)
        cadastro_sus = next_message["message"]["text"]

        already_registered = self.user_repo.check_if_user_exists(cadastro_sus) # TODO check against DB
    
        if (not already_registered):
            # Register new user
            self.responder(speeches.register_speech['hello'], last_chat_id)
            next_message, update_id = self.get_next_message(update_id)
            name = next_message["message"]["text"]
            
            self.responder(speeches.register_speech['gender'], last_chat_id)
            next_message, update_id = self.get_next_message(update_id)
            gender = next_message["message"]["text"].strip().lower()
        
            if (gender == "1" or gender == "masculino"):
                gender = "MASCULINO"
            elif (gender == "2" or gender == "feminino"):
                gender = "FEMININO"
            elif (gender == "3" or gender == "prefiro nao informar"):
                gender = "NAO INFORMADO"
            else:
                gender = "OUTRO"
            
            self.responder(speeches.register_speech['phone'], last_chat_id)
            next_message, update_id = self.get_next_message(update_id)
            phone_number = next_message["message"]["text"].strip()

            result = self.user_repo.register_new_user(cadastro_sus, name, gender, phone_number) # TODO call DB and register this
            if result:
                self.responder(speeches.register_speech['success'], last_chat_id)
            else:
                self.responder(speeches.register_speech['failure'], last_chat_id)

        # Already registered
        user = self.user_repo.get_user(cadastro_sus) # TODO call DB and get this
        name = user["name"]
        gender = user["gender"]
        phone_number = user["phone_number"]

        greetings_text = speeches.users_speech['hello'] % (name)
        self.responder(greetings_text, last_chat_id)
        next_message, update_id = self.get_next_message(update_id)
        option = next_message["message"]["text"]
        
        if option == "1":
            print("make_appointment")
            #make_appointment_flux()
        elif option == "2":
            print("re_appointment")
            #reappointment_flux()
        elif option == "3":
            print("cancel_appointment")
            #cancel_appointment_flux()
        elif option == "4":
            print("check_appointment")
            #check_appointment_flux()
        elif option == "5":
            self.responder(speeches.users_speech['acs_notified'], last_chat_id)
            # TODO notify ACS someway
        elif option == "6":
            self.responder(speeches.users_speech['end'], last_chat_id)
        else:
            self.responder(speeches.users_speech['invalid'], last_chat_id)
    
    # Obter mensagens
    def get_next_message(self, update_id: int):
        """
        get the next message the user will send from this update_id.
        """
        if update_id:
            update_id += 1
            link_requisicao = f'{self.url_base}getUpdates?timeout=100&offset={update_id}'
            resultado = json.loads(requests.get(link_requisicao).content)
            return resultado["result"][-1], update_id
        return None


    def get_last_message(self, update_id):
        """
        Get the last received message, from the given update_id.
        If None is passed as the update_id, returns the last message globally.
        """
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id}'
        resultado = json.loads(requests.get(link_requisicao).content)
        return resultado["result"][-1]

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)