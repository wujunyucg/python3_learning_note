# 对象持久化
### 文本文件
```python
list = [1,2,3]
with open('data_list.txt', 'w') as f:
    f.write(str(list))
    
with open('data_list.txt', 'r') as f:
    result = f.renad() # 字符串
list2 = eval(result) # 可转化为list
```
### pickle
```python
import pickle
list = [1,2,3]
with open('data_list.txt', 'wb') as f:
    s = pickle.dump(list)
    p = pickle.loads(s)
    pickle.dump(list, f)
    list2 = pickle.load(f)
```

### shelve
```python
import shelve
list = [1,2,4]
student={'name': 'wu', 'age': 2}
db = shelve.open('shelve_student')
db['s'] = student
db['l'] = list
del db['l']
db.close()
```