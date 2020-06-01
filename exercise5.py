# exercise 5
numbers = "3 4 8 7 1"
try:
    with open("exercise5.txt", "w") as f:
        f.write(numbers)
except IOError:
    print("Ошибка ввода-вывода!")

# open to count the sum of the numbers
amount = 0
try:
    with open("exercise5.txt", "r") as f:
        content = f.read()
except IOError:
    print("Ошибка ввода-вывода!")

for el in content.split():
    amount += int(el)

print(f"Сумма: {amount}")
