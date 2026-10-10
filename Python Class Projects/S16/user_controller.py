from user import User
from user_service import UserService


class UserController:
    def __init__(self):
        self.__service = UserService()

    def save(
            self,
            name,
            family,
            national_id,
            birth_date,
            phone_number,
            username,
            password,
            locked,
            role
    ):
        try:
            user = User(
                name,
                family,
                national_id,
                birth_date,
                phone_number,
                username,
                password,
                locked,
                role
            )

            self.__service.save(user)

            return True, f"Info : {user} Saved"

        except ValueError as error:
            return False, f"Error : {error}"

    def get_all(self):
        try:
            users = self.__service.get_all()

            return True, users

        except Exception as error:
            return False, f"Error : {error}"