# json
```python
import json

def json_basic():
    data = {
        'id':1,
        'name': '李',
        'age':20
    }
    json_str = json.dumps(data) # 变为 json 格式字符串
    print(json_str)
    json_data = json.loads(json_str)
    
    with open('data.json', 'w') as f
        json.dump(data, f)
        data = json.load(f)
```

# excel
```python
import xlrd
def xl_read():
    book = xlrd.open_workbook('data.xls')
    for sheet in book.sheets():
        print(sheet.name)
        
    sheet = book.sheet_by_name('sheet1')
    print(sheet.nrows)
    for i in range(sheet.nrows):
        print(sheet.row_values(i))
```