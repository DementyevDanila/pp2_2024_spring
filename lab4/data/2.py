import datetime
from datetime import date

x = date.today()

print("Yesterday:", x - datetime.timedelta(days = 1))
print("Today:", x)
print("Tomorrow:", x + datetime.timedelta(days = 1))