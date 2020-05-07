# exercise 4
# coding=utf-8

answer = input("Введите строчку из нескольких слов, разделенных пробелами: ")
answer_list = answer.split()
print(answer_list)

i=0
for v in answer_list:
    # this check is not needed in python
    if len(v) > 10:
        print(i,v[:10])
    else:
        print(i,v)
    i += 1

# or using an enumerate function
print('=' * 10)
for i, v in enumerate(answer_list):
    print(i, v[:10])

