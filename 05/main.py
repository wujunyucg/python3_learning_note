class Book:
    # 静态变量
    count = 0

    # 类方法
    @staticmethod
    def cls_method():
        print('class method')

    # 构造器
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def print_info(self):
        print(self.title)

    # 类似 toString 不等于; 调试控制台用
    def __repr__(self):
        return '图书 {}'.format(self.title)

    # toString
    def __str__(self):
        return 'title: {}, price: {}, author: {}'.format(self.title, self.price, self.author)

    # 析构函数  del(object)
    def __del__(self):
        pass

    @property
    def age(self):
        return 2

    @age.setter
    def age(self, value):
        raise AttributeError('禁止赋值年龄')

    @age.deleter
    def age(self):
        raise AttributeError('禁止删除 age')


book = Book('math', 30, 'wu')  # 实例化
book.name = "math"
book.print_info()
print(book)
print(book.age)
# del (book)
