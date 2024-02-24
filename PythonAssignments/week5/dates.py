import datetime

week_6_date = datetime.date(2021, 10 , 4)
print(week_6_date)

# doesn't like leading zeros
#week_6_date = datetime.date(2021, 10 , 04)
#print(week_6_date)

date_today = datetime.date.today()
print(date_today)
print(date_today.day)
print(date_today.month)
print(date_today.year)

date_out_week = datetime.timedelta(days = 7)
print(date_today + date_out_week)
print(date_today - date_out_week)

my_date = datetime.datetime(2021, 10, 31, 12, 00, 30, 100)
print(my_date)
print(my_date.year)
print(my_date.month)
print(my_date.day)
print(my_date.hour)
print(my_date.minute)
print(my_date.second)
print(my_date.microsecond)

date_1=date_today.today()
date_2=datetime.datetime.now()
date_3=datetime.datetime.utcnow()
print(date_today)
print(date_1)
print(date_2)
print(date_3)

date_utc = datetime.datetime.utcnow()
print(date_utc)
date_central = date_utc.astimezone()
print(date_central)

# formatting
d1 = datetime.date.today()
d1 = d1.strftime("%d/%m/%Y")
print("d1 =", d1)

d2 = datetime.date.today()
d2 = d2.strftime("%B %d, %Y")
print("d2 =", d2)

# formats have to match
date_string = "10-31-2021 12:30:10"
date_date = datetime.datetime.strptime(date_string, "%m-%d-%Y %H:%M:%S")

date_string2 = "4-15-2019 11:20:10"
date_date2 = datetime.datetime.strptime(date_string2, "%m-%d-%Y %H:%M:%S")

print(date_date - date_date2)