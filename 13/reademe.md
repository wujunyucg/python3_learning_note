# 函数高级
```python

# 函数可嵌套 可作为参数, 返回值
```

## 装饰器
```python
# 自定义
def p_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func(*args, **kwargs) + '</p>'
    return wrapper

@p_decorator
def get_text():
    return 'aaaa'
```

```python
class P:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return '<p>' + self.func(*args, **kwargs) + '</p>'


@P
def get_text():
    return 'aaaa'    
    
class Student:
    def __init__(self, name):
        self.name = name
        
    @p_decorator # 不能为 @P
    def get_name(self):
        return self.name.upper()        
```     
## 装饰器参数化
```python
def tags(tag)
    def p_decorator(func):
        def wrapper(*args, **kwargs):
            return tag + func(*args, **kwargs) + '</p>'
        return wrapper
    return p_decorator
```
