homes = []


def show_menu():
    options = [
        "1. Add Home",
        "2. Show Homes",
        "0. Exit"
    ]

    for option in options:
        print(option)

    print("-" * 25)


def format_home(home):
    return f"Address: {home['address']} | Owner: {home['owner']} | Rooms: {home['rooms']} | Parking: {home['parking']}"


def get_rooms(home):
    return home["rooms"]


def add_home():
    address = input("Enter Home's Address: ")
    owner = input("Enter Owner's Name: ")
    rooms = int(input("Enter Number of Rooms: "))
    parking = int(input("Enter Amount of Parking Spaces: "))

    new_home = {
        "address": address,
        "owner": owner,
        "rooms": rooms,
        "parking": parking
    }

    if new_home in homes:
        print("Home already exists")
        return

    homes.append(new_home)

    print("Home added successfully")


def show_homes():
    sorted_homes = sorted(homes, key=get_rooms)

    home_info = map(format_home, sorted_homes)

    print(list(home_info))


while True:
    show_menu()

    action = int(input("What would you like to do?: "))
    print("-" * 25)

    if action == 1:
        add_home()

    elif action == 2:
        show_homes()

    elif action == 0:
        break

    else:
        print("Invalid Input")

    print("-" * 25)