lessons = []

while True:
    print("1.Add a lesson")
    print("2.Print lesson list")
    print("3.Sum of university units")
    print("0.Exit")

    option = int(input("What would you like to do? (0-3): "))

    if option == 1:
        print("-" * 25)
        print("1.Mathematics - 3 units")
        print("2.Artificial Intelligence - 5 units")
        print("3.Software Engineering - 3 units")
        print("4.Database Systems - 3 units")
        print("5.Cybersecurity - 2 units")
        print("6.Robotics - 1 unit")
        print("0.Back")
        print("-" * 25)

        lesson_choice = int(input("What would you like to pick? (0-6): "))

        print("-" * 25)

        if lesson_choice == 1:
            lesson = {"name": "Mathematics", "units": 3}

        elif lesson_choice == 2:
            lesson = {"name": "Artificial Intelligence", "units": 5}

        elif lesson_choice == 3:
            lesson = {"name": "Software Engineering", "units": 3}

        elif lesson_choice == 4:
            lesson = {"name": "Database Systems", "units": 3}

        elif lesson_choice == 5:
            lesson = {"name": "Cybersecurity", "units": 2}

        elif lesson_choice == 6:
            lesson = {"name": "Robotics", "units": 1}

        elif lesson_choice == 0:
            continue

        else:
            print("Invalid Input")
            continue

        total_units = 0

        for lesson_in_list in lessons:
            total_units += lesson_in_list["units"]

        if total_units + lesson["units"] <= 17:
            lessons.append(lesson)
            print("Lesson added successfully!")
        else:
            print("You cannot add this lesson.")
            print("The maximum number of units is 17.")

        print("-" * 25)

    elif option == 2:
        print("Lesson List:")

        for lesson in lessons:
            print(lesson)

        print("-" * 25)

    elif option == 3:
        total_units = 0

        for lesson in lessons:
            total_units += lesson["units"]

        print("The total number of units is", total_units)
        print("-" * 25)

    elif option == 0:
        break

    else:
        print("-" * 25)
        print("Invalid Input")
        print("-" * 25)