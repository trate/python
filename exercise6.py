# exercise 6
a = int(input("Введите результат пробежки в первый день в километрах: "))
b = int(input("Введите конечный результат: "))

# increase of the previous day result in percent
i = 10
count = 1

while a <= b:
    a = a + a * (i / 100)
    count += 1
print(f"На {count}-й день спортсмен достиг результата - не менее {b} км.")