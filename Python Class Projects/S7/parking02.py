cars = []

while True:
    print("1.Add Car")
    print("2.Parking's List")
    print("3.Amount of Cars")
    print("0.Exit")
    print("-" * 25)

    action = int(input("What would You like to do?: "))
    print("-" * 25)

    if action == 1:
        name = input("Enter Your Car's Model: ")
        color = input("Enter Your Car's Color: ")
        plate = input("Enter Your Car's Plate Number: ")

        used_plates = [car["plate number"] for car in cars]

        if plate in used_plates:
            print("This plate number has already been used.")
        else:
            cars.append({
                "name": name,
                "color": color,
                "plate number": plate
            })
            print("Car added successfully")

        print("-" * 25)

    elif action == 2:
        print(cars)
        print("-" * 25)

    elif action == 3:
        print(f"There are/is {len(cars)} car(s) in the parking lot.")
        print("-" * 25)

    elif action == 0:
        break

    else:
        print("Invalid Input")
        print("-" * 25)