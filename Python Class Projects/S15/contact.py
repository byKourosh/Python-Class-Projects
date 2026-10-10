class Contact:
    def __init__(self, name, family_name, number, relation):
        self.name = name
        self.family_name = family_name
        self.number = number
        self.relation = relation

    def __get_number(self):
        return self.__number

    def __set_number(self, number):
        if number.isdigit():
            self.__number = number
        else:
            raise ValueError("Invalid phone number")

    number = property(__get_number, __set_number)

    def __str__(self):
        return f"{self.name} {self.family_name} - {self.number} - {self.relation}"


contact1 = Contact(
    "Ali",
    "Alipour",
    "09123456789",
    "Friend"
)

print(contact1)