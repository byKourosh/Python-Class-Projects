class Lesson:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def __str__(self):
        return f"{self.name} - {self.units} units"


lesson1 = Lesson("Mathematics", 3)
lesson2 = Lesson("Artificial Intelligence", 5)
lesson3 = Lesson("Robotics", 1)

print(lesson1)
print(lesson2)
print(lesson3)