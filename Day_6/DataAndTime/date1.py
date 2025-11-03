import datetime

now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))
bir = datetime.date(2026,1,31)

today = datetime.date.today()
dif = bir - today
print(dif)