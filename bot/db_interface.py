from datetime import datetime
from config import database_url
import requests
import json

USER_COLLECTION = "pacientes"
PENDING_COLLECTION = "pendentes"
CONFIRMED_COLLECTION = "confirmados"
CONTACT_ORDER_COLLECTION = "pedidos_contato"

class DbFunctions:
    def __init__(self):
        self.db = DbConnection()

    def get_user(self, cadastro_sus: str) -> dict:
        """
        Returns all the information of the user whose cadastros_sus is the one passed as dict.
        If the user does not exist, returns an empty dict.
        """
        retrieved_data = self.db.getFilteredData(
            USER_COLLECTION, "cadastro_sus", cadastro_sus
        )

        if retrieved_data is not None:
            for key in retrieved_data:
                return retrieved_data[key]
    
        return {}

    def register_user(self, user_infos: dict):
        """
        Register new user.
        Checks if there is already someone with this cadastro_sus registered.
        """
        retrieved_data = self.db.getFilteredData(
            USER_COLLECTION, "cadastro_sus", user_infos["cadastro_sus"]
        )
        
        if retrieved_data is None:
            self.db.postData(USER_COLLECTION, user_infos)
            return True
        return False

    def get_next_appointments_from_user(self, cadastro_sus: str):
        """
        Receives the cadastro from the user.
        Returns 2 lists of dicts containing the confirmed appointments and the pending appointments,
        respectively.
        [
            {
                specialty: str,
                date_hour: datetime
            },
            ...
        ],
        [
            {
                specialty: str,
                date_hour: datetime
            },
            ...
        ]
        """
        confirmed_appointments_list = []
        pending_appointments_list = []

        retrieved_data = self.db.getFilteredData(
            CONFIRMED_COLLECTION, "cadastro_sus", cadastro_sus
        )
        if retrieved_data is not None:
            for key in retrieved_data:
                confirmed_appointments_list.append(
                    retrieved_data[key]
                )

        retrieved_data = self.db.getFilteredData(
            PENDING_COLLECTION, "cadastro_sus", cadastro_sus
        )
        if retrieved_data is not None:
            for key in retrieved_data:
                pending_appointments_list.append(
                    retrieved_data[key]
                )

        return confirmed_appointments_list, pending_appointments_list

    def register_pending_appointment(self, appointment_infos: dict):
        """
        register the appointment in the db.
        """
        appointment_infos["date_time"] = str(datetime.now())
        self.db.postData(PENDING_COLLECTION, appointment_infos)

    def register_contact_order(self, contact_order_infos: dict):
        """
        Register the intent of a user to contact an ACS about something.
        """
        contact_order_infos["date_time"] = str(datetime.now())
        self.db.postData(CONTACT_ORDER_COLLECTION, contact_order_infos)

class DbConnection:
    def __init__(self):
        self.db_url = database_url

    def getFilteredData(self, collection: str, filter_key: str, filter_pattern: str):
        request_link = self.db_url + f"/{collection}.json?orderBy=\"{filter_key}\"&equalTo=\"{filter_pattern}\""

        response = requests.get(request_link)
        data = json.loads(response.content)
        return data

    def getData(self, collection: str):
        request_link = self.db_url + f"/{collection}.json"

        response = requests.get(request_link)
        data = json.loads(response.content)
        return data

    def postData(self, collection: str, data: dict):
        requests.post(self.db_url + f"/{collection}.json", json=data)

# conn = DbConnection()

# response = conn.getFilteredData(USER_COLLECTION, "cadastro_sus", "234")
# print(response)