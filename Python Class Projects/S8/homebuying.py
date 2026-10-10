homes = []


def add_home():
    address = input("Enter Home's Address: ")
    owner = input("Enter Owner's Name: ")
    rooms = int(input("Enter Number of Rooms: "))
    parking = int(input("Enter Amount of Parking Spaces: "))

    homes.append({
        "address": address,
        "owner": owner,
        "rooms": rooms,
        "parking": parking
    })

    print("Home added successfully")


def show_homes():
    print(homes)


while True:
    print("1.Add Home")
    print("2.Show Homes")
    print("0.Exit")
    print("-" * 25)

    action = int(input("What would You like to do?: "))
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