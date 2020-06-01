# exercise 4
# coding=utf-8
try:
    f_obj = open("exercise4.txt", "r")
    content = f_obj.readlines()
except IOError:
    print("Ошибка ввода-вывода!")
finally:
    f_obj.close()


ru_words = ["Один", "Два", "Три", "Четыре"]
new_content = []
for i, l in enumerate(content):
    s = ''
    new_line = l.split()
    new_line[0] = ru_words[i]
    new_content.append(s.join(new_line) + '\n')

try:
    f_new = open("exercise4_new.txt", "w")
    f_new.writelines(new_content)
except IOError:
    print("Ошибка ввода-вывода!")
finally:
    f_new.close()
