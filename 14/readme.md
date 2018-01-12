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


```python
import csv
def csv_writer():
    header = ['id', 'name', 'age']
    rows = [
        (1, 'tom', 23)
        (2, 'wu', 23)
        (3, 'li', 23)
    ]
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
        
def csv_writer_dict():
    header = ['id', 'name', 'age']
    rows = [
        {'id': 1, 'name': 'tom', 'age': 30}
        {'id': 2, 'name': 'li', 'age': 30}
        {'id': 3, 'name': 'wu', 'age': 30}
    ]  
    with open('data.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        writer.writerows(rows)      
```