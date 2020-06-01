#exercise 7
import json

# read file content
try:
    with open("exercise7.txt", "r") as f:
        content = f.readlines()
except IOError:
    print("Ошибка ввода-вывода!")

result = []
sum_profit = 0
average_dict = {}
profit_dict = {}
# count a number of the firms with a positive profit
has_profit = 0

for el in content:
    l = el.split()
    profit = int(l[2]) - int(l[3])
    profit_dict[l[0]] = profit
    if profit >= 0:
        sum_profit += profit
        has_profit += 1

average_dict["average_profit"] = sum_profit / has_profit
result.append(profit_dict)
result.append(average_dict)

# serialize to JSON
try:
    with open("exercise7_json.txt", "w") as f:
        json.dump(result, f)
except IOError:
    print("Ошибка ввода-вывода!")