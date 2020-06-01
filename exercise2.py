# exercise 2
# coding=utf-8
word_number = 0
line_number = 0

try:
    with open("exercise2.txt") as f_obj:
        for line in f_obj:
            word_number += len(line.split())
            line_number += 1
except:
    print("Произошла ошибка ввода-вывода!")


print(f"В файле {line_number} строк и {word_number} слов.")