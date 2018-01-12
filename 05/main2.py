class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} {}'.format(self.name, self.age)

    def work(self):
        print('员工 {} work'.format(self.name))


# 继承
class Programmer(Employee):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    # 重写
    def work(self):
        print('程序员 {} work'.format(self.name))


if __name__ == '__main__':
    e1 = Employee('tom', 20)
    e1.work()
    e2 = Programmer('jack', 30, 'java')
    e2.work()
