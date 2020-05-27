# exercise 5
from functools import reduce

even_num = [el for el in range(100, 1001) if not el % 2]


def my_func(n1, n2):
    return n1 * n2


print(reduce(my_func, even_num))
