class Home:
    homes = []

    def __init__(self, address, owner, rooms, parking):
        self.address = address
        self.owner = owner
        self.rooms = rooms
        self.parking = parking

    def __get_rooms(self):
        return self.__rooms

    def __set_rooms(self, rooms):
        if isinstance(rooms, int) and rooms > 0:
            self.__rooms = rooms
        else:
            raise ValueError("Invalid rooms")

    def __get_parking(self):
        return self.__parking

    def __set_parking(self, parking):
        if isinstance(parking, int) and parking >= 0:
            self.__parking = parking
        else:
            raise ValueError("Invalid parking")

    rooms = property(__get_rooms, __set_rooms)
    parking = property(__get_parking, __set_parking)

    def __str__(self):
        return f"{self.address} - {self.owner} - {self.rooms} rooms - {self.parking} parking"

    def add_home(self):
        for home in Home.homes:
            if (
                home.address == self.address
                and home.owner == self.owner
                and home.rooms == self.rooms
                and home.parking == self.parking
            ):
                print("Home already exists")
                return

        Home.homes.append(self)
        print("Home added successfully")


while True:
    print("1. Add Home")
    print("2. Show Homes")
    print("0. Exit")

    try:
        action = int(input("What would you like to do?: "))

        if action == 1:
            address = input("Enter Home's Address: ")
            owner = input("Enter Owner's Name: ")
            rooms = int(input("Enter Number of Rooms: "))
            parking = int(input("Enter Amount of Parking Spaces: "))

            home = Home(address, owner, rooms, parking)
            home.add_home()

        elif action == 2:
            for home in Home.homes:
                print(home)

        elif action == 0:
            break

        else:
            print("Invalid Input")

    except ValueError as error:
        print(error)