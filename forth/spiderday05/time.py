import time
import datetime

t= time.time()

# 原始时间数据
print(t)
# 秒级时间戳
print(int(t))
# 毫秒级时间戳
print(int(round(t*1000)))
# 毫秒级时间戳，基于lambda
nowTime = lambda:int(round(t*1000))
print(nowTime())
# 日期格式化
time = datetime.datetime.now()
print(time)
strftime = time.strftime('%Y-%m-%d %H:%M:%S')




