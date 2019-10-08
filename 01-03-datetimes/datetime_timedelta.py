#!python3

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(t.days)
#4

print(t.seconds)
#36000

# print(t.hours)
#Traceback (most recent call last):
    #File "<pyshell#119>", line 1, in <module> t.hours
#AttributeError: 'datetime.timedelta' object has no attribute 'hours'

print(t.seconds / 60 / 60)
#10.0

print(t.seconds / 3600)
#10.0


#########

eta = timedelta(hours=6)

today = datetime.today()

print(today)
#datetime.datetime(2018, 2, 19, 14, 55, 19, 197404

print(today + eta)
#datetime.datetime(2018, 2, 19, 20, 55, 19, 197404)

print(str(today + eta))
#'2018-02-19 20:55:19.197404'