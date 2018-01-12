# 小数格式化
```python
'{:f}'.format(3.16)
'{:+f}'.format(3.16)
'{:,.4f}'.format(3.16)
a=1.5
b=20
# 百分比
'{:.2%}'
import math
math.trunc()
math.floor()
math.ceil()
round()
```

# 随机数
```python
import random
list = [1,2,3]
random.choice(list)
random.sample(list, 3)
# 将顺序打乱
random.shuffle(list)


random.randint(1,10)
random.random()
random.getrandbits(5)
```

# 日期与时间
```python
import datetime
datetime.MAXYEAR #9999
datetime.MINYEAR #1
today = datetime.date.today()
today.year
today.weekday()
today.isoweekday()

birthday = datetime.date(2010, 3, 12)

t = datetime.time(12,45,32)
t.hour
t.minute

now = datetime.datetime.now()

s = '2018-3-15'
t = datetime.datetime.strptime(s, '%Y-%m-%d')

result = now.strftime('%Y/%m/%d')
```
# 时间差处理
```python
import datetime
d = datetime.datetime(2018, 5, 11, 22, 44)
t= datetime.datetime(2016,3,5,19,33,44)
diff = d - t # timedelta

t + datetime.timedelta(days=100)
```