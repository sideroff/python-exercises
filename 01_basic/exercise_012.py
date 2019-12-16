import calendar
from datetime import date

cal = calendar.TextCalendar()

today = date.today()
print(cal.formatmonth(today.year, today.month))