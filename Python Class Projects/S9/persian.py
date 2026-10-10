from persian_tools import phone_number
from persian_tools.bank import card_number
from persian_tools import plate
from persian_tools import bill
from persian_tools import national_id


while True:

    print("\n1. شماره تلفن")
    print("2. کارت بانکی")
    print("3. پلاک ماشین")
    print("4. شناسه قبض / پرداخت")
    print("5. کد ملی")
    print("0. خروج")

    choice = input("انتخاب کنید: ")

    #phone number
    if choice == "1":
        phone = input("شماره تلفن را وارد کنید: ")

        if phone_number.validate(phone):
            data = phone_number.operator_data(phone)

            print("شماره درست است")
            print("اپراتور:", data["operator"])
            print("پایه:", data["base"])
            print("استان‌ها:", data["province"])
        else:
            print("شماره تلفن اشتباه است")

    # bank details
    elif choice == "2":
        card = input("شماره کارت را وارد کنید: ")

        if card_number.validate(card):
            data = card_number.bank_data(card)

            print("شماره کارت درست است")
            print("بانک:", data["persian_name"])
        else:
            print("شماره کارت اشتباه است")

    # car's plate
    elif choice == "3":
        car_plate = input("پلاک را وارد کنید: ")

        if plate.is_valid(car_plate):
            data = plate.get_info(car_plate)

            print("پلاک درست است")
            print("استان:", data["province"])
            print("نوع:", data["type"])
            print("دسته:", data["category"])
        else:
            print("پلاک اشتباه است")

    # bill
    elif choice == "4":
        bill_id = input("شناسه قبض را وارد کنید: ")
        payment_id = input("شناسه پرداخت را وارد کنید: ")

        data = bill.get_detail(
            bill_id=int(bill_id),
            payment_id=int(payment_id)
        )

        if data["is_valid"]:
            print("شناسه‌ها درست هستند")
            print("نوع قبض:", data["type"])
            print("مبلغ:", data["amount"], "تومان")
        else:
            print("شناسه قبض یا پرداخت اشتباه است")

    # national security number
    elif choice == "5":
        national = input("کد ملی را وارد کنید: ")

        if national_id.validate(national):
            data = national_id.find_place(national)

            print("کد ملی درست است")
            print("شهر:", data["city"])
            print("استان:", data["province"])
        else:
            print("کد ملی اشتباه است")

    # exit
    elif choice == "0":
        print("برنامه تمام شد")
        break

    else:
        print("گزینه اشتباه است")