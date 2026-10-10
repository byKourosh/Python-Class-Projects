contacts = []


def show_menu():
    options = [
        "1. Add Contact",
        "2. Show Contacts",
        "0. Exit"
    ]

    for option in options:
        print(option)

    print("-" * 25)


def get_name(contact):
    return contact["name"]


def format_contact(contact):
    return f"Name: {contact['name']} {contact['family name']} | Number: {contact['number']} | Relation: {contact['relation']}"


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
    sorted_contacts = sorted(contacts, key=get_name)
    contact_info = map(format_contact, sorted_contacts)

    print(list(contact_info))


while True:
    show_menu()

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