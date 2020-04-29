# exercise 4
user_number = int(input("Введите целое положительное число: "))
n = user_number
max_digit = -1

while n > 0:
    r = n % 10
    n = n // 10
    if r > max_digit:
        max_digit = r
print(f"Максимальная цифра в числе {user_number}: {max_digit}")

