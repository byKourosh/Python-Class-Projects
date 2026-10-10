from user_controller import UserController


controller = UserController()


def save_user():
    print("===== SAVE USER =====")

    name = input("Name : ")
    family = input("Family : ")
    national_id = input("National ID : ")
    birth_date = input("Birth Date : ")
    phone_number = input("Phone Number : ")
    username = input("Username : ")
    password = input("Password : ")
    locked = input("Locked : ")
    role = input("Role : ")

    success, message = controller.save(
        name,
        family,
        national_id,
        birth_date,
        phone_number,
        username,
        password,
        locked,
        role
    )

    print(message)


def show_users():
    print("===== USERS =====")

    success, users = controller.get_all()

    if success:
        for user in users:
            print(user)

    else:
        print(users)


save_user()