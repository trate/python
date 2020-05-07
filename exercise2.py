# exercise 2
# coding=utf-8
answer_list = []
result_list = []

i = 0
j = 0

while i < 6:
    answer = int(input(f"Введите {i} числовой элемент списка: "))
    answer_list.append(answer)
    i += 1

print(f"Ваш лист: {answer_list}")

while j < len(answer_list):
    if j == len(answer_list) - 1:
        break
    answer_list[j], answer_list[j+1] = answer_list[j+1], answer_list[j]
    j += 2


print(f"Ваш новый лист: {answer_list}")


