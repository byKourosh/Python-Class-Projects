class Car:
    def __init__(self, name, color, plate_number):
        self.name = name
        self.color = color
        self.plate_number = plate_number

    def __str__(self):
        return f"{self.name} - {self.color} - {self.plate_number}"


car1 = Car("BMW", "Black", "12A345")
car2 = Car("Pride", "White", "45B678")

print(car1)
print(car2)