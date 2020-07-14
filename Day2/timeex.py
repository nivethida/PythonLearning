# -*- coding: utf-8 -*-

# str points to time, strptime

from datetime import datetime as dt

date_str = 'Mar/03/2020'

date_obj = dt.strptime(date_str, '%b/%d/%Y')
date_str2 = 'February-10-2020'

date_obj2 = dt.strptime(date_str, '%B-%d-%y')

print(date_obj)

print(date_obj.year)
print(date_obj.month)
print(date_obj.month)
print(date_obj.weekday)
print(date_obj.day)
print(date_obj.hour)
print(date_obj.minute)
print(date_obj.second)
print(date_obj.microsecond)
print(date_obj.timestamp())

print(date_obj2<date_obj1)

time_str4 = 'Feb-01-2019 13:45:46'

time_obj4 = dt.strptime(time_str, '%b-%d-%Y %H:%M:%S')