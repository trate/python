# exercise 5
income = int(input("Введите прибыль: "))
costs = int(input("Введите издержки: "))
profit = income - costs

if profit > 0:
    profitability = profit / income
    print(f"Ваша фирма получила прибыль: {profit} условных единиц.")
    print(f"Рентабельность вашей фирмы {profitability}")
    employees_number = int(input("Введите количество сотрудников в вашей компании: "))
    print(f"Прибыль фирмы в расчете на сотрудника: {profit / employees_number}")
else:
    print(f"Ваша фирма проработала себе в убыток: {profit} условных единиц")