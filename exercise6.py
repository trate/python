# exercise 6
# coding=utf-8
def capitalize_input(phrase):
    s = phrase

    def int_func():
        nonlocal s
        s = phrase.title()
        return s
    return int_func

print(capitalize_input('вова ест корову!')())
