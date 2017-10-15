from datetime import date, datetime,timedelta   #调用python内置处理日期函数
today = date.today()
print("output:today:{0!s}".format(today))   #输出今天的年月日
print("output:{0!s}".format(today.year))   #输出年.year函数
print("output:{0!s}".format(today.month))   #输出月份.month函数
print("output:{0!s}".format(today.day))   #输出日期
current_datetime = datetime.today()   #利用datetime输出今天的日期，包括时分秒
print("output:{0!s}".format(current_datetime))
one_day = timedelta(days = -1)   #days = -1，在timedelta中可以直接对日期处理进行加减
yesterday = today + one_day
print("output:yesterday:{0!s}".format(yesterday))
eight_hours = timedelta(hours = -8)
print("output:{0!s} {1!s}".format(eight_hours.days,eight_hours.seconds))