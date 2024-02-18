import datetime
from datetime import date

year = int(input())
month = int(input())
day = int(input())
year2 = int(input())
month2 = int(input())
day2 = int(input())
x = date(year, month, day)
y = date(year2, month2, day2)

print("Delta:", abs(x.year - y.year) * 52 * 7 * 24 * 60 * 60 + abs(x.month - y.month) * 30 * 24 * 60 * 60 + abs(x.day - y.day) * 24 * 60 * 60)