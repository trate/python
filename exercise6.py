# exercise 6
from itertools import count, cycle

for el in count(8):
    if el > 1000:
        break
    else:
        print(el)

my_list = [2, 3, 19, 20, 21]
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1