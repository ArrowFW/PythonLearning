from datetime import date
from datetime import datetime
from datetime import timedelta



now = datetime.now()

print("Today is :", now)

print("one year from now:", str(now+timedelta(days=365)))
print("in two weeks three days:", str(now+timedelta(weeks=2, days=2)))
print()
t = datetime.now()-timedelta(weeks=1)

print("One week ago", str(t))

print()
print()

today = date.today()
print(today)
afd = date(today.year, 4, 1)
print(afd)
if afd < today:
    print("April fools days already went by:", ((today-afd).days))
    afd = afd.replace(year=today.year+1)
tafd = afd - today
print("It is :", tafd, "Until the Next April fools day")
