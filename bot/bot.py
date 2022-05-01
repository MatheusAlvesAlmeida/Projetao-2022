from datetime import datetime, timedelta
import requests
import json
import time
import re

from config import get_telegram_token, ubs_name, message_timeout
from db_interface import DbFunctions
import speeches

class TelegramBot:
    def __init__(self):
        self.token = get_telegram_token()

        print("Starting bot...")
        print("token: ", self.token)
        print("UBS name: ", ubs_name)
        print("message timeout: ", message_timeout)

        self.url_base = f'https://api.telegram.org/bot{self.token}/'
        self.specialty_repo = ["Odontologia", "Pediatria", "Oftalmologia", "Urologia", "Ginecologia"]
        self.sleep_time = 3

        self.db = DbFunctions()

    def start(self):
        print("Started!")
        while(True):
            result = []
            while len(result) == 0:
                # Sleeps for some seconds before checking again
                time.sleep(self.sleep_time)
                result = self.get_last_update_result()

            update_id = int(result[-1]["update_id"])
            chat_id = result[-1]["message"]["chat"]["id"]
            message_unix_date = result[-1]["message"]["date"]
            now_unix_date = int(time.time())

            if (now_unix_date - message_unix_date) <= (self.sleep_time * 2):
                print("Serving user with chat_id:", chat_id)
                update_id = self.general_flux(update_id, chat_id)
                time.sleep(self.sleep_time)

    def general_flux(self, update_id: int, chat_id: str):
        self.responder(speeches.greetings_speech.format(ubs_name), chat_id)
        result, update_id = self.get_next_message_result(update_id, chat_id)
        if len(result) == 0:
            return update_id
        next_message = result[0]
        cadastro_sus = next_message["message"]["text"]
        user = self.db.get_user(cadastro_sus)
    
        if (len(user) == 0):
            # Register new user

            user["cadastro_sus"] = cadastro_sus

            self.responder(speeches.register_speech['hello'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            user["name"] = next_message["message"]["text"]
            
            self.responder(speeches.register_speech['gender'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            user["gender"] = next_message["message"]["text"].strip().lower()
        
            if (user["gender"] == "1" or user["gender"] == "masculino"):
                user["gender"] = "MASCULINO"
            elif (user["gender"] == "2" or user["gender"] == "feminino"):
                user["gender"] = "FEMININO"
            elif (user["gender"] == "3" or user["gender"] == "prefiro nao informar"):
                user["gender"] = "NAO INFORMADO"
            else:
                user["gender"] = "OUTRO"
            
            #CPF
            self.responder(speeches.register_speech['CPF'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            cpf = next_message["message"]["text"]
            user["CPF"] = re.sub('[^0-9]','', cpf)
            #RG
            self.responder(speeches.register_speech['RG'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            rg = next_message["message"]["text"]
            user["RG"] = re.sub('[^0-9]','', rg)
            #DATA_N
            self.responder(speeches.register_speech['birth'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            user["birth"] = next_message["message"]["text"]
            #CEP
            self.responder(speeches.register_speech['address_cep'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            cep = next_message["message"]["text"]
            user["CEP"] = re.sub('[^0-9]','', cep)
            #Numero
            self.responder(speeches.register_speech['address_street_number'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            street_number = next_message["message"]["text"]
            user["address_number"] = re.sub('[^0-9]','', street_number)
            #END
            self.responder(speeches.register_speech['phone'], chat_id)
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            phone_number = next_message["message"]["text"]
            user["phone_number"] = re.sub('[^0-9]','', phone_number)

            register_result = self.db.register_user(user)

            if register_result:
                self.responder(speeches.register_speech['success'], chat_id)
            else:
                self.responder(speeches.register_speech['failure'], chat_id)
                return update_id

        # Already registered

        greetings_text = speeches.users_speech['hello'].format(user["name"])
        self.responder(greetings_text, chat_id)
        result, update_id = self.get_next_message_result(update_id, chat_id)
        if len(result) == 0:
            return update_id
        next_message = result[0]
        option = next_message["message"]["text"]
        
        user_infos = {
            "cadastro_sus": user["cadastro_sus"],
            "name": user["name"],
            "gender": user["gender"],
            "phone_number": user["phone_number"],
            "cep": user["CPF"],
            "address_number": user["address_number"]
        }

        if option == "1":
            update_id = self.make_appointment_flux(update_id, chat_id, user_infos)
        elif option == "2":
            update_id = self.cancel_appointment_flux(update_id, chat_id, user_infos)
        elif option == "3":
            update_id = self.check_appointment_flux(update_id, chat_id, user_infos)
        elif option == "4":
            self.responder(speeches.users_speech['acs_notified'], chat_id)
            # TODO notify ACS someway
            # AcsFunctions.notify_acs_contact(user_infos)
        elif option == "5":
            self.responder(speeches.users_speech['end'], chat_id)
        else:
            self.responder(speeches.users_speech['invalid'], chat_id)
        
        return update_id
    
    def make_appointment_flux(self, update_id: int, chat_id: str, user_infos: dict):
        """
        """
        self.responder(speeches.appointment_speech['specialty'], chat_id)
        specialties_string, specialties_dict = self.getSpecialtyOptions()
        self.responder(specialties_string, chat_id)
        found = False
        while(not found):
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return
            next_message = result[0]
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

        self.responder(speeches.appointment_speech['user_confirmation'].format(chosen_specialty, ubs_name), chat_id)
        result, update_id = self.get_next_message_result(update_id, chat_id)
        if len(result) == 0:
            return update_id
        next_message = result[0]
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
            user_infos["chat_id"] = chat_id

            self.db.register_pending_appointment(user_infos)
            self.responder(speeches.appointment_speech['apointment_ending'], chat_id)
            # TODO if the ACS confirms or not the appointment, we need to user speech in
            # appointment_speech['acs_confirmation'] or appointment_speech['acs_denial']
        
        return update_id

    def cancel_appointment_flux(self, update_id: int, chat_id: str, user_infos: dict):
        """
        """
        self.responder(speeches.cancel_speech['appointment'], chat_id)

        appointments_string, appointments_dict = self.get_all_appointments(
            user_infos["cadastro_sus"]
        )

        self.responder(appointments_string, chat_id)

        found = False
        while(not found):
            result, update_id = self.get_next_message_result(update_id, chat_id)
            if len(result) == 0:
                return update_id
            next_message = result[0]
            appointment_number = next_message["message"]["text"]
            if appointment_number.isnumeric():
                appointment_number = int(appointment_number)
                if appointment_number in appointments_dict:
                    (appointment, is_appointment_confirmed) = appointments_dict[appointment_number]
                    found = True
                else:
                    self.responder(speeches.error_speech['invalid_number'], chat_id)
            else:
                self.responder(speeches.error_speech['only_numbers'], chat_id)

        user_infos["chosen_specialty"] = appointment["specialty"]
        user_infos["chosen_date"] = appointment["date_hour"]
        user_infos["chat_id"] = chat_id

        self.responder(speeches.cancel_speech['user_confirmation'].format(
            user_infos["chosen_specialty"], ubs_name, user_infos["chosen_date"],
        ), chat_id)
        result, update_id = self.get_next_message_result(update_id, chat_id)
        if len(result) == 0:
            return update_id
        next_message = result[0]
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
            if is_appointment_confirmed:
                self.db.register_cancel_appointment_order(user_infos)
            else:
                # TODO check if this feature is really necessary.
                self.db.cancel_unconfirmed_appointment(user_infos)
            
            self.responder(speeches.cancel_speech["acs_notified"], chat_id)
        
        return update_id

    def check_appointment_flux(self, update_id: int, chat_id: str, user_infos: dict):
        """
        """
        confirmed_appointments_list, pending_appointments_list = (
            self.db.get_next_appointments_from_user(
                user_infos["cadastro_sus"]
            )
        )
        self.responder(speeches.check_appointment_speech['confirmed'], chat_id)
        
        confirmed_output = ""
        for count, item in enumerate(confirmed_appointments_list):
            index = count + 1
            confirmed_output += (str(index) + " - " + str(item["chosen_specialty"]) + " - " + str(item["date_hour"]) + "\n")
        
        self.responder(confirmed_output, chat_id)

        self.responder(speeches.check_appointment_speech['pending'], chat_id)
        
        pending_output = ""
        for count, item in enumerate(pending_appointments_list):
            index = count + 1
            pending_output += (str(index) + " - " + str(item["chosen_specialty"]) + "\n")

        self.responder(pending_output, chat_id)

        return update_id
        
    def get_next_message_result(self, update_id: int, chat_id: str):
        """
        get the next message the of a given chat.
        In case of the next message being from another user, ask for them to try again in a few minutes, and wait again for
        expected one.
        """
        update_id += 1
        link_requisicao = f'{self.url_base}getUpdates?timeout={message_timeout}&offset={update_id}'
        result = json.loads(requests.get(link_requisicao).content)["result"]
        if len(result) == 0:
            update_id -= 1
            return result, update_id # timeout

        message_chat_id = result[0]["message"]["chat"]["id"]

        if "text" not in result[0]["message"]:
            self.responder(speeches.no_text_speech, message_chat_id)
            return [], update_id # message without text

        while message_chat_id != chat_id:
            self.responder(speeches.wait_speech, message_chat_id)

            update_id += 1
            link_requisicao = f'{self.url_base}getUpdates?timeout={message_timeout}&offset={update_id}'

            result = json.loads(requests.get(link_requisicao).content)["result"]
            if len(result) == 0:
                update_id -= 1
                return result, update_id # timeout
            
            message_chat_id = result[0]["message"]["chat"]["id"]

            if "text" not in result[0]["message"]:
                self.responder(speeches.no_text_speech, message_chat_id)
                return [], update_id # message without text

        return result, update_id

    def get_last_update_result(self):
        """
        Get the last update object received globally.
        """
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        return json.loads(requests.get(link_requisicao).content)["result"]

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

    def get_all_appointments(self, cadastro_sus: str):
        """
        returns a string informing all appointments of a given cadastro_sus
        and a dict linking the index numbers on the string to each appoitment object.
        """
        confirmed_appointments_list, pending_appointments_list = (
            self.db.get_next_appointments_from_user(
                cadastro_sus
            )
        )

        dict_output = {}
        string_output = ""

        index = 1
        for item in confirmed_appointments_list:
            dict_output[index] = (item, True)
            string_output += (str(index) + " - " + str(item["specialty"]) + " - " + str(item["date_hour"]) + "\n")
            index += 1

        for item in pending_appointments_list:
            dict_output[index] = (item, False)
            string_output += (str(index) + " - " + str(item["specialty"]) + " - " + str(item["date_hour"]) + "\n")
            index += 1

        return string_output, dict_output