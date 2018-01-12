# 字符与编码

```python
s.encode('ASCII')
s.encode('UTF-8')
b1 = b'\xe4\xbc'
b1.decode('utf-8')
```
```python
bytes('abc','ascii')
bytes([34,44,56,78])
s1 = 'abc'
ba = bytearray(s1,'utf8')
ba.decode('utf8')
```
## BOM 处理: 字节顺序标记
```python
open('data.txt', 'r', encoding='utf-8-sig')

open('data.txt', 'w' encoding='utf-8-sig').write('')
```