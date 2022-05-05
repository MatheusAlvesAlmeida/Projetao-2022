from datetime import datetime
from config import firebase

class DbFunctions:
    def __init__(self):
        self.db = firebase.database()

    def get_user(self, cadastro_sus: str) -> dict:
        """
        Returns all the information of the user whose cadastros_sus is the one passed as dict.
        If the user does not exist, returns an empty dict.
        """
        response = (
            self.db.child("pacientes")
            .order_by_child("cadastro_sus")
            .equal_to(cadastro_sus)
            .limit_to_first(1)
            .get()
        )
        if (response.val() is None):
            return {}
        for user in response.each():
            return user.val()
    
    def get_all_users(self) -> list:
        """
        Returns a list of all the users.
        """
        response = self.db.child("pacientes").get()
        users_list = []

        if (response.val() is not None):
            for user in response.each():
                users_list.append(user.val())

        return users_list

    def register_user(self, user_infos: dict):
        """
        Register new user.
        Checks if there is already someone with this cadastro_sus registered.
        """
        if len(self.get_user(user_infos["cadastro_sus"])) == 0:
            self.db.child("pacientes").push(user_infos)
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

        response = (
            self.db.child("confirmados")
            .order_by_child("cadastro_sus")
            .equal_to(cadastro_sus)
            .limit_to_first(10)
            .get()
        )

        if (response.val() is not None):
            for appointment in response.each():
                confirmed_appointments_list.append(appointment.val())

        response = (
            self.db.child("pendentes")
            .order_by_child("cadastro_sus")
            .equal_to(cadastro_sus)
            .limit_to_first(10)
            .get()
        )

        if (response.val() is not None):
            for appointment in response.each():
                pending_appointments_list.append(appointment.val())

        return confirmed_appointments_list, pending_appointments_list

    def register_pending_appointment(self, appointment_infos: dict):
        """
        register the appointment in the db.
        """
        self.db.child("pendentes").push(appointment_infos)

    def register_cancel_appointment_order(self, appointment_infos: dict):
        """
        Register an appointment cancel order
        """
        self.db.child("cancelar").push(appointment_infos)

    def cancel_unconfirmed_appointment(user_appointment_infos: dict):
        """
        If an appointment is still unconfirmed, delete it directly from the DB.
        """
        # TODO implement