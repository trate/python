# exercise 3
# coding=utf-8
def my_func(n1, n2, n3):
    nums = [n1, n2, n3]
    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)
    return max1 + max2


print(my_func(2, 3, 4))
