# exercise 1
# coding=utf-8
from sys import argv

script_name, work_hours, cost_hour, premium = argv

salary = lambda work_hours, cost_hour, premium: (int(work_hours) * int(cost_hour)) + int(premium)
print(f"Ваша зарплата: {salary(work_hours, cost_hour, premium)}")
