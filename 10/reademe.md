# 正则表达式
## 单字
. 除\n所有字符  
\d 数字 等于 [0-9]  
\D 非数字 等于 [^0-9]  
\s 空白字符 \t\n\r\f\v  
\S 非空白字符 [^\t\n\r\f\v]  
\w 字母数字字符 [a-zA-Z0-9_]  
\W 非字母数字字符 [^a-zA-Z0-9_]

## 批量备选
| yes|no  

## 量词
? 0或1次  
'*' 0或多次  
'+' 1或多次  
{3,5} 3-5次  
## 贪婪非贪婪
'.*?'
## 边界匹配
^ 行首  
$ 行尾
\b 单词边界  
\B 非单词边界  
\A 输入开头  
\Z 输入结尾 

# python 中
```python
import re
text = 'Tom is 8 years old.Mike is 25 years old'
pattern = re.compile('\d+')
pattern.findall(text)

re.findall('\d+', text)

p_name = re.compile('[A-Z]\w+')
p_name.findall(text)


pattern  = re.compile(r'<html>')
text = '<html><html>'
# 开头
pattern.match(text)
pattern.match(text, 1)
# 任意位置
pattern.search(text)
# 多个
it = pattern.finditer(text)
for m in it:
    print(m)
    
text = 'Tom is 8 years old.Mike is 25 years old'    
pattern = re.compile(r'(\d+).*?(\d+)')
# 匹配对象 matchobject
m = pattern.search(text)
#m.group() = m.group(0)
m.group(1) # 8
m.start(1) # 7 下标
m.end(1)
m.groups() # 返回元组
m.groupdict()

# \1 重用
# (?P<name>) 命名 m.group('name')
# 切割
m.split(text)
# 替换
m.sub(',', text)

re.purge() # 清理缓存
re.escape() # 逃逸字符
```
