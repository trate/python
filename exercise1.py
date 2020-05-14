# exercise 1
# coning=utf-8
def check_not_null(n):
    if n == 0:
        print("Деление на ноль!")
        return False
    return True


def division():
    """Division: function that makes a division)"""
    n1 = int(input("Введите первое число: "))
    n2 = int(input("Введите второе число: "))
    if check_not_null(n2):
        print(f"Результат: {n1 / n2}")
    else:
        exit(1)


division()
