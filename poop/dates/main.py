import datetime


date = datetime.date(2023, 10, 1)
today = datetime.date.today()
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S")
print(now)
print(today)
print(date)