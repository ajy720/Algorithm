import datetime 

today = datetime.datetime.now() + datetime.timedelta(hours=9)

print(str(today)[:10])