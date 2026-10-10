class User:
    def __init__(
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
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.locked = locked
        self.role = role

    def __get_national_id(self):
        return self.__national_id

    def __set_national_id(self, national_id):
        if national_id:
            self.__national_id = national_id
        else:
            raise ValueError("Invalid national ID")

    national_id = property(__get_national_id, __set_national_id)

    def __str__(self):
        return f"{self.name} {self.family} - {self.national_id}"