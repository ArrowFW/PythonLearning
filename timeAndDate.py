from datetime import datetime
now = datetime.now()
print(now.strftime("The current year: %Y and year %y weekday %a %A month %b %B dayofmonth %d %D"))
#local datetime
print(now.strftime("The local date and time: %c local date :%x localtime: %X"))
#time
print()
print(now.strftime("current time: %I:%M:%S:%p"))
print(now.strftime("current(24 hours) time: %H:%M"))
