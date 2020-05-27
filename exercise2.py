# exercise 2
# coding=utf-8
my_list = [2, 6, 19, 24, 56, 7, 90, 5]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)