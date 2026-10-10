from user_data_manager import UserDataManager


class UserService:
    def __init__(self):
        self.__data_manager = UserDataManager()

    def save(self, user):
        users = self.__data_manager.get_all()

        for old_user in users:

            if old_user.name == user.name:
                raise ValueError("Name already exists")

            if old_user.family == user.family:
                raise ValueError("Family already exists")

            if old_user.national_id == user.national_id:
                raise ValueError("National ID already exists")

        self.__data_manager.save(user)

    def get_all(self):
        return self.__data_manager.get_all()