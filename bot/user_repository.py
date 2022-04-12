class user_repository():
    def __init__(self):
        self.user_repository = {}
        self.user_repository["123456"] = {
            "name": "André Luiz",
            "gender": "MASCULINO",
            "phone_number": "2345678"
        }

    def check_if_user_exists(self, cadastro_sus):
        exists = cadastro_sus in self.user_repository
        return exists

    def register_new_user(self,
        cadastro_sus: str, name: str, gender: str, telephone_number: str
    ):
        self.user_repository[cadastro_sus] = {
            "name": name,
            "gender": gender,
            "phone_number": telephone_number
        }
        return True

    def get_user(self, cadastro_sus: str):
        return self.user_repository[cadastro_sus]