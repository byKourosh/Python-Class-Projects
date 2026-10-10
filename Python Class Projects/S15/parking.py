class Car:
    def __init__(self, name, color, plate_number):
        self.name = name
        self.color = color
        self.plate_number = plate_number

    def __get_plate_number(self):
        return self.__plate_number

    def __set_plate_number(self, plate_number):
        if plate_number:
            self.__plate_number = plate_number
        else:
            raise ValueError("Invalid plate number")

    plate_number = property(__get_plate_number, __set_plate_number)

    def __str__(self):
        return f"{self.name} - {self.color} - {self.plate_number}"


car1 = Car("BMW", "Black", "12A345")

print(car1)