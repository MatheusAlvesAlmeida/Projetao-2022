class DbFunctions:
    
    @staticmethod
    def get_user(cadastro_sus: str):
        """
        Returns all the information of the user whose cadastros_sus is the one passed
        """
    
    @staticmethod
    def register_new_user(cadastro_sus: str, name: str, gender: str, phone_number: str):
        """
        Register new user
        """

    @staticmethod
    def get_next_appointments_from_user(cadastro_sus: str):
        """
        Receives the cadastro from the user.
        Returns 2 lists containing the confirmed appointments and the pending appointments,
        respectively.
        """
        confirmed_appointments_list = []
        pending_appointments_list = []

        return confirmed_appointments_list, pending_appointments_list

    @staticmethod
    def get_next_free_slots_for_specialty(specialty: str, amount: int = 10):
        """
        Receives an specialty and an option amount.
        Returns the next amount of free slots for the given specialty. 
        """