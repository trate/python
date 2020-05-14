# exercise 5
# coding=utf-8
def my_func():
    work = True
    s = 0
    while work:
        nums = input("Input the numbers that are separated using spaces('s' to stop): ").split()
        for v in nums:
            if v == 's':
                work = False
                break
            else:
                s += int(v)
        print(s)


my_func()
