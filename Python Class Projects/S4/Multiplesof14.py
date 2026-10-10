total = 0
count = 0

for num in range(100, 999, 2):
    if num % 7 == 0:
        print(num)
        total+=num
        count += 1
average = total / count
print(f"The average is {average}")