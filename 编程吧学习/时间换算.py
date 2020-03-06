import datetime,time


print(datetime.datetime.today())
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.strptime('2018-6-9 23:58:50', '%Y-%m-%d %H:%M:%S'))
d1 = datetime.datetime.now()

print(d1.timetuple())
print('{}年{}月{}日{}时{}分{}秒'.format(d1.year,d1.month,d1.day,d1.hour,d1.minute,d1.second))

t1 = datetime.datetime(2020,1,24,00,00,00)



while True:
    t2 = datetime.datetime.now()

    t3 = t1 - t2

    day = t3.days
    hours,remainder = divmod(t3.seconds,3600)
    minutes,seconds = divmod(remainder,60)

    hour = t3.seconds//3600
    minute = t3.seconds%3600//60
    second = t3.seconds%3600%60
    print('{}天{}小时{}分钟{}秒'.format(day,hours,minutes,seconds))
    print('{}天{}小时{}分钟{}秒'.format(day,hour,minute,second))

    time.sleep(1)
