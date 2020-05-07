# exercise 6
# coding=utf-8
good_name = ''
cost = 0
amount = 0
measure = ""
goods = []

i = 1
while i < 4:
    good_name = input("Введите имя товара: ")
    cost = int(input("Введите стоимость товара: "))
    amount = int(input("Введите количество товара: "))
    measure = input("Введите единицу измерения товара: ")

    goods_properties = {"название": good_name, "цена": cost, "количество": amount, "ед": measure}
    goods_cortege = (i, goods_properties)
    goods.append(goods_cortege)
    i += 1

    print("-" * 50)

print(goods)



