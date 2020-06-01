# exercise 3
sum = 0
employee = []
line_number = 0

try:
    with open("exercise3.txt") as f_obj:
        for line in f_obj:
            salary = int(line.split()[1])
            if int(salary) < 20000:
                employee.append(line.split()[0])
            sum += salary
            line_number += 1
except:
    print("Произошла ошибка ввода-вывода!")

print("Сотрудники, чей доход меньше 20000 рублей:")
for e in employee:
    print(e)
print((f"Средний доход: {sum / line_number} рублей"))
