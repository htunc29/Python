from datetime import datetime,timedelta
# from datetime import date
# from datetime import time
# import datetime
result=dir(datetime)
simdi=datetime.now()
result=simdi.year
result=simdi.time()
result=simdi.minute
result=simdi.second
result=simdi.today()
result=datetime.ctime(simdi)
result=datetime.strftime(simdi,"%B")
t="15 April 2024 hour 10:12:30"
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)
birthday=datetime(2003,11,10,12,45,12)
print(birthday)
result=datetime.timestamp(birthday)
result=datetime.fromtimestamp(result)
result=simdi+timedelta(days=10)
print(result)