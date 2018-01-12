## 语句与表达式
### 赋值语句
基本赋值
序列赋值
扩展序列解包赋值 a,b,*c='asdd'
多目标赋值 a=b=0
参数化赋值

### 表达式
#### 打印
```python
print(url1, url2, url3, sep='|')
print(url1, url2, url3, sep='|' ,file=open('result.txt', 'w'))
```

### 流程控制
#### if
```python
if score > 7:
    print()
elif score > 9:
    print()
else:
    print()
# 三元
result = 'yes' if score >=60 else 'no'

lambda x: print(x)
operation = {
    'add': add # 函数
    'sub': lambda x: print(x)
}
operation.get('add')(10)

if not x:
    pass
```

#### while
```python
while True:
    ...
    break
    continue
    pass
else:
    pass
name = input('请输入:')


```
#### for
```python
range(0,101,2)
for x in range(1,10):
    pass
fox x in list:
    pass

# 序号
s = 'asdfasdfhsj'
for idx,item in enumerate(s):
    pass
```
### 迭代
```python
for x in [1,2,3]
for x in (1,2,3)
for x in {'a':1, 'b':'z'}

f = open(file)
for line in f:
    pass
# 迭代协议
f.__next__()
next(f)
# 迭代工具
# 迭代器对象
# 可迭代对象
iter(f) is f
```
```python
result = zip(['x','y','z'],[1,2,3])
# ('x',1)
# ('y',2)

def double_number(x):
    return x*2
l=[1,2,3,4,5]
result = list(map(double_number, l))
```
