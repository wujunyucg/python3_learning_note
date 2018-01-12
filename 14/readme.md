# 虚拟环境

# 读取 csv
```python
import csv
def csv_read():
    with open('data.csv') as f:
        reader = csv.reader(f)
        header  = next(reader)
        for row in reader:
            print(row)  # 每行列表
            
from collections import namedtuple
def csv_read_by_namedtuple():
    with open('data.csv') as f:
        reader = csv.reader(f)
        header  = next(reader)
        Row = namedtuple('Row', ['Id', 'name', 'age'])
        for r in reader:
            row = Row(*r)
            print(row)
                  
def csv_read_by_dict():
    with open('data.csv') as f:
        reader = csv.DictReader(f)   
        for row in reader:
            print(row)                    
```