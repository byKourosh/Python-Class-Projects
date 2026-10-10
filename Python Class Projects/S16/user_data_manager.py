class UserDataManager:
    def __init__(self):
        self.__user_list = []

    def save(self, user):
        self.__user_list.append(user)

    def get_all(self):
        return self.__user_list