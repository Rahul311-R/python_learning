import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%d-%m-%Y %H:%M:%S"))

birt = datetime.date(2026,1,31)
print(birt)