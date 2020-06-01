# exercise 6
# coding=utf-8
# read file content
try:
    with open("exercise6.txt", "r") as f:
        content = f.readlines()
except IOError:
    print("Ошибка ввода-вывода!")

# final dictionary
my_dict = {}

for el in content:
    el_list = el.split()
    numbers = []
    # n - number as a string
    for l in el_list:
        n = ''
        for s in l:
            if s.isdigit():
                n += s
        if n:
            numbers.append(int(n))
    my_dict[el_list[0][:len(el_list[0]) - 1]] = sum(numbers)


print(my_dict)