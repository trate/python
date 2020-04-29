# exercise 2
time_user = int(input("Введите время в секундах: "))
time_minutes = time_user // 60
time_sec = time_user - time_minutes * 60
time_hours = time_minutes // 60
time_minutes = time_minutes - time_hours * 60

print("Время: %02d:%02d:%02d" % (time_hours, time_minutes, time_sec))
