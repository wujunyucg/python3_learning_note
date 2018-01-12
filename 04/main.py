import models
# from models import page as m_page
# from models import *
import a.product

# 重新载入 只认识模块
import importlib

importlib.reload(models)

# 搜索范围: 程序主目录 环境变量 标准库 扩展库

if __name__ == '__main__':
    print(a.product.X)
    # print(models.page)
    print('hello')
