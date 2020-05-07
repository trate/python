# exercise 5
# coding=utf-8

my_list = [7, 5, 3, 3, 2]

answer = int(input("Введите число рейтинга: "))

i = 0
for v in my_list:
    if answer <= v:
        i += 1
my_list.insert(i, answer)
print(my_list)
