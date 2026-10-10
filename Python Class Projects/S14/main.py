from person import Person
from account import Account
from check import Check
from card import Card
from saving import Saving


person1 = Person("Ali", "Alipour")

account1 = Account(1001, 5000000, "Tehran", person1)
check1 = Check(1002, 3000000, "Shiraz", person1, 100, 150)
card1 = Card(1003, 7000000, "Tehran", person1, "123456789")
saving1 = Saving(1004, 10000000, "Tabriz", person1, 18)

print(person1.name)
print(person1.family)

print(account1)
print(check1)
print(card1)
print(saving1)

person1.save()

account1.bardasht()
account1.variz()