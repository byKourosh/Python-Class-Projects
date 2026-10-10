class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def save(self):
        print("Save:", self.name, self.family)