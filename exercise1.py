# exercise 1
str_list = []
while True:
    out = input("Введите строчку(пустая строка - завершение): ")
    if not out:
        break
    str_list.append(out + '\n')

try:
    out_f = open("out_file.txt", "w")
    out_f.writelines(str_list)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    out_f.close()
