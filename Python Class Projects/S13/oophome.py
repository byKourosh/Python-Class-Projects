class Home:
    homes = []

    def __init__(self, address, owner, rooms, parking):
        self.address = address
        self.owner = owner
        self.rooms = rooms
        self.parking = parking

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


home1 = Home("Tehran, Vanak", "Ali", 3, 1)
home2 = Home("Tehran, Tajrish", "Reza", 4, 2)

home1.add_home()
home2.add_home()

for home in Home.homes:
    print(home)