evens = 0
odds = 0
num = None

while num != 0:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        evens += num
    else:
        odds += num
total = evens + odds #extra
print(f"Even numbers total:{evens}")
print(f"Odd numbers total:{odds}")
print(f"numbers total:{total}") #extra