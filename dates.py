from datetime import datetime

# my_time = datetime.datetime.now()
# print(my_time)
# print("-"*50)
# my_time2 = datetime.datetime.utcnow()
# print(my_time2)

my_day = datetime.now()
# print(f"Year: {my_day.year}")
# print(f"Month: {my_day.month}")
# print(f"Day: {my_day.day}")

day_latam = my_day.strftime("%d/%m/%Y")
print(day_latam)
day_usa = my_day.strftime("%m/%d/%Y")
print(day_usa)