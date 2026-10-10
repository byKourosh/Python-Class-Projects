class Lesson:
    def __init__(self, code, name, unit):
        self.__code = code
        self.name = name
        self.unit = unit

    def __get_code(self):
        return self.__code

    def __get_unit(self):
        return self.__unit

    def __set_unit(self, unit):
        if isinstance(unit, int) and unit in [1, 2, 3, 5]:
            self.__unit = unit
        else:
            raise ValueError("Invalid Unit !!!")

    code = property(__get_code)
    unit = property(__get_unit, __set_unit)

    def __str__(self):
        return f"{self.code} - {self.name} - {self.unit}"


lesson1 = Lesson(381841, "Python", 3)

print(lesson1)