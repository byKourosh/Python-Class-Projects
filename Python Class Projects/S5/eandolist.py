even_numbers = []
odd_numbers = []

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break
    elif number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(f"The even numbers are: {even_numbers}")
print(f"The odd numbers are: {odd_numbers}")