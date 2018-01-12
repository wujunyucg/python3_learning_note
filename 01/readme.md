### 变量无类型约束
```
#变量类型
type(var)
#内存地址
id(var)

isinstance(1,int)

a,b=1,2
b,a=a,b
```
类型取决于关联对象
PVM PGC
```
# is 判断地址是否相等
name is age
# == 判断字面相等
name == age

# 对象引用数
import sys
sys.getrefcount(var)
```

### 数据类型
#### 数字
int
```
int('42')+1
```
float
```
import math
import random
```
```
'{0}'.format(20)
# 小数点后两位 浮点展示
'{0:.2f}'.format(3.3333)

```
```
# 除去小数部分,类型保持精度高的
10//4
# 向下取整
math.floor()
# 向 0 取整
math.trunc()
# 四舍五入
round()

# 八进制
0o7
oct()
# 十六进制
0xF
hex()
# 二进制
0b1011
bin()
```
##### Decimal
```
import decimal
decimal.Decimal('1.1')+decimal.Decimal('2.2')
```
#####Fraction
#### 字符串
```
name='tom'
name[0]
len(name)
name*8
path=r'fsa\a\sfda\\dfs'
for c in s:
    print(c)
    print(c ,end=" ")
s[0:4] #只有 0-3
s[-1] #最后一个
s[:] #从头到尾
s[::2] #步长为 2
s[::-1] # 翻转

ord('C')
chr(99)
# 不能原位改变
s=s.replace('e','a')

url.startwith('http') # True False
url.endwith('cn')
url.find('cn') #返回位置 不区分大小写
if x in url:
    pass

'name:{0},age:{1}'.format(d[0],d[1])
'{name}=>{age}'.format(name='tom', age='20')

a,b,c='uke'
#扩展序列解包赋值
a,b,*c='asdfa'
```
#### 列表: list
```
list = [1,2,3]
list = [1, 5,'asd',[12,45]]
len(list)
list[0]
```
```
list = list('dsfasgf')
s = ''.join(list)
s = '|'.join(list)
url.split(',') #返回一个list
[x,y,x]=[1,2,3]
[1,2,3]+[4,5,6]
's' in list

result=[]
result.append('s')

l1 = [i**2 for i in list] # 列表推导
['ccc']*3 # ['ccc','ccc','ccc']

list.extend([1,2,3]) #连接
list.sort()
list.reverse()
list.pop()
del(list[0])
list.index('a')
list.count('q')
l2=l1.copy()
```
#### 字典表: dict(HashTable)
```
d={'name': 'tome','age': 20}
d['name'] #可能会抛异常
d.get('name')
d.get('name', 'tom') # 默认值
d['score'] = 20

emp = dict(name='Mike', age=20)
len(d)
emp.update({'department': 'ss'})
emp.pop('name')
for k in emp.keys():
    print(k)
for v in emp.values():
    print(v)
emp.items() # 返回元组
for k,v in emp.items():
    print('{}=>{}'.format(k,v))

# 可以嵌套
# 排序
ks = list(emp.keys()).sort()

ks = emp.keys()
for k in sorted(ks)
    print(k)
```
#### 元组: tuple
```
t=(1,2,3,4)
t[1]
# 不支持原位修改
# 可嵌套
(1,2)+(3,4) #合并
.index()
.count()

```
```
from collections import namedtuple
Employee = namedtuple('Employee',['name','age','score'])
jerry = Employee('Jerry', age = 30 , score=99)
```
#### 文件: file
```
file = open(filename, mode)
# mode r,w,a,b,+
open(filename, mode, encoding='utf8')
file.write()
file.read()
file.readline()
file.readlines() #返回list
file.close()

with open(filename) as f:
    pass

# pickle 存取对象 序列化
import pickle
f=open('datafile.pkl', 'wb')
pickle.dump(emp, f)
f=open('datafile.pkl', 'rb')
emp1 = pickle.load(f)
```
#### 集合: set
#### 布尔
#### 空: None
#### 程序单元
##### 函数: function
##### 模块
##### 类: class