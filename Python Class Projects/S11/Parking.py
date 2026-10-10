cars = []


def show_menu():
    options = [
        "1. Add Car",
        "2. Parking's List",
        "3. Amount of Cars",
        "0. Exit"
    ]

    for option in options:
        print(option)

    print("-" * 25)


def add_car():
    name = input("Enter Your Car's Model: ")
    color = input("Enter Your Car's Color: ")
    plate = input("Enter Your Car's Plate Number: ")

    used_plates = list(map(lambda car: car["plate number"], cars))

    if plate in used_plates:
        print("This plate number has already been used.")
    else:
        cars.append({
            "name": name,
            "color": color,
            "plate number": plate
        })

        print("Car added successfully")


def parking_list():
    sorted_cars = sorted(cars, key=lambda car: car["name"])

    car_info = map(
        lambda car: f"Model: {car['name']} | Color: {car['color']} | Plate: {car['plate number']}",
        sorted_cars
    )

    print(list(car_info))


def car_amount():
    print(f"There are/is {len(cars)} car(s) in the parking lot.")


while True:
    show_menu()

    action = int(input("What would You like to do?: "))
    print("-" * 25)

    if action == 1:
        add_car()

    elif action == 2:
        parking_list()

    elif action == 3:
        car_amount()

    elif action == 0:
        break

    else:
        print("Invalid Input")

    print("-" * 25)