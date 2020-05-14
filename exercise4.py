# exercise 4
# coding=utf-8
def my_func(x, y):
    return 1 / float(x) ** abs(int(y))


print(my_func(1.24, -5))

def my_func2(x,y):
    for i in range(abs(int(y)) - 1):
        y *= y
    return 1 / y


print(my_func(1.24, -5))
