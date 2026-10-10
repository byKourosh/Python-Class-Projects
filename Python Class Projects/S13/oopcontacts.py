class Contact:
    def __init__(self, name, family_name, number, relation):
        self.name = name
        self.family_name = family_name
        self.number = number
        self.relation = relation

    def __str__(self):
        return f"{self.name} {self.family_name} - {self.number} - {self.relation}"


contact1 = Contact("Kourosh", "Irandost", "09121234567", "Friend")
contact2 = Contact("Sara", "Tehrani", "09123456789", "Friend")

print(contact1)
print(contact2)