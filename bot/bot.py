from click import confirm
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
from datetime import datetime, timedelta


import speeches
from user_repository import user_repository
from config import telegram_token
from acs_inteface import AcsFunctions
from db_interface import DbFunctions
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
        self.specialty_repo = ["Odontologia", "Pediatria", "Oftalmologia", "Urologia", "Ginecologia"]

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
        
        user_infos = {
            "cadastro_sus": cadastro_sus,
            "name": name,
            "gender": gender,
            "phone_number": phone_number
        }

        if option == "1":
            print("make_appointment")
            self.make_appointment_flux(update_id, last_chat_id, user_infos)
        elif option == "2":
            print("re_appointment")
            self.remake_appointment_flux(update_id, last_chat_id, user_infos)
        elif option == "3":
            print("cancel_appointment")
            self.cancel_appointment_flux(update_id, last_chat_id, user_infos)
        elif option == "4":
            print("check_appointment")
            self.check_appointment_flux(update_id, last_chat_id, user_infos)
        elif option == "5":
            self.responder(speeches.users_speech['acs_notified'], last_chat_id)
            # TODO notify ACS someway
            AcsFunctions.notify_acs_contact(user_infos)
        elif option == "6":
            self.responder(speeches.users_speech['end'], last_chat_id)
        else:
            self.responder(speeches.users_speech['invalid'], last_chat_id)
    
    def make_appointment_flux(self, update_id: int, chat_id: str, user_infos: dict):
        """
        """
        self.responder(speeches.appointment_speech['specialty'], chat_id)
        specialties_string, specialties_dict = self.getSpecialtyOptions()
        self.responder(specialties_string, chat_id)
        found = False
        while(not found):
            next_message, update_id = self.get_next_message(update_id)
            specialty_number = next_message["message"]["text"]
            if specialty_number.isnumeric():
                specialty_number = int(specialty_number)
                if specialty_number in specialties_dict:
                    chosen_specialty = specialties_dict[specialty_number]
                    found = True
                else:
                    self.responder(speeches.error_speech['invalid_number'], chat_id)
            else:
                self.responder(speeches.error_speech['only_numbers'], chat_id)
        
        self.responder(speeches.appointment_speech['date_time'], chat_id)
        dates_string, dates_dict = self.getDatesOptions(chosen_specialty)
        self.responder(dates_string, chat_id)
        found = False
        while(not found):
            next_message, update_id = self.get_next_message(update_id)
            date_number = next_message["message"]["text"]
            if date_number.isnumeric():
                date_number = int(date_number)
                if date_number in dates_dict:
                    chosen_date = dates_dict[date_number]
                    found = True
                else:
                    self.responder(speeches.error_speech['invalid_number'], chat_id)
            else:
                self.responder(speeches.error_speech['only_numbers'], chat_id)

        self.responder(speeches.appointment_speech['user_confirmation'], chat_id)
        next_message, update_id = self.get_next_message(update_id)
        confirmation = next_message["message"]["text"].strip().lower()
        repeat = True
        while (repeat):
            if confirmation == "1" or confirmation == "sim":
                confirmation = True
                repeat = False
            elif confirmation == "2" or confirmation == "nao":
                confirmation = False
                repeat = False
            else:
                self.responder(speeches.error_speech['invalid_number'], chat_id)

        if confirmation:
            user_infos["chosen_specialty"] = chosen_specialty
            user_infos["chosen_date"] = chosen_date
            user_infos["chat_id"] = chat_id

            # Pass all the collected information (in the user_infos) to the ACS,
            # including the chat_id, so that when the ACS confirms or not the
            # appointment, we can send a message to this user
            AcsFunctions.notify_acs_appointment(user_infos)
            self.responder(speeches.appointment_speech['apointment_ending'], chat_id)

    def remake_appointment_flux(update_id: int):
        """
        """
    
    def cancel_appointment_flux(update_id: int):
        """
        """

    def check_appointment_flux(self, update_id: int, chat_id: str, user_infos: dict):
        """
        """
        confirmed_appointments_list, pending_appointments_list = (
            DbFunctions.get_next_appointments_from_user(
                user_infos["cadastro_sus"]
            )
        )
        self.responder(speeches.check_appointment_speech['confirmed'], chat_id)
        
        confirmed_output = ""
        for count, item in enumerate(confirmed_appointments_list):
            index = count + 1
            confirmed_output += (str(index) + " - " + str(item) + "\n")
        
        self.responder(confirmed_output, chat_id)

        self.responder(speeches.check_appointment_speech['pending'], chat_id)
        
        pending_output = ""
        for count, item in enumerate(pending_appointments_list):
            index = count + 1
            pending_output += (str(index) + " - " + str(item) + "\n")
        
        self.responder(pending_output, chat_id)
        
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

    def getSpecialtyOptions(self):
        """
        returns a formatted string containing the list of specialties offered by the UBS
        and a dict where each specialty is linked to its position in the list, so that the bot can
        interpret each option
        """
        string_output = ""
        dict_output = {}
        for count, item in enumerate(self.specialty_repo):
            index = count + 1
            string_output += (str(index) + " - " + item + "\n")
            dict_output[index] = item
        
        return string_output, dict_output

    def getDatesOptions(self, specialty: str):
        """
        returns a formatted string containing the next 10 free slots of the chosen specialty offered by the UBS
        and a dict where each date-time is linked to its position in the list, so that the bot can
        interpret each option
        """
        string_output = ""
        dict_output = {}
        # TODO get from DB
        # free_dates = DbFunctions.get_next_free_slots_for_specialty(specialty)
        free_dates = []
        for i in range(10):
            free_dates.append(datetime.today() + timedelta(days=1))

        for count, item in enumerate(free_dates):
            index = count + 1
            string_output += (str(index) + " - " + str(item) + "\n")
            dict_output[index] = item
        
        return string_output, dict_output

 