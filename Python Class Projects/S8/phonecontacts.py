contacts = []


def add_contact():
    name = input("Enter First Name: ")
    family_name = input("Enter Family Name: ")
    number = input("Enter Phone Number: ")
    relation = input("Enter Relation (Mom, Dad, Friend...): ")

    contacts.append({
        "name": name,
        "family name": family_name,
        "number": number,
        "relation": relation
    })

    print("Contact added successfully")


def show_contacts():
    print(contacts)


while True:
    print("1.Add Contact")
    print("2.Show Contacts")
    print("0.Exit")
    print("-" * 25)

    action = int(input("What would You like to do?: "))
    print("-" * 25)

    if action == 1:
        add_contact()

    elif action == 2:
        show_contacts()

    elif action == 0:
        break

    else:
        print("Invalid Input")

    print("-" * 25)