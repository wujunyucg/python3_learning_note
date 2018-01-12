def learning(name, age, sex, end):
    pass


def learning2(name, age=20, sex='man', end='1'):
    # global x

    def nested():
        # nonlocal x
        pass

    return name


# 传 元组
def avg(score, *scores):
    print(sum(scores))
    print(type(scores))
    print(scores)


# 传 dict
def display(**employee):
    print(employee)


learning2(name='tom')
avg(2, 3, 4, 5, 6)
# 委托
avg2 = avg
avg2(1, 2, 3)
display(name='tome', age=20)
f = lambda name: print(name)
f2 = lambda x, y: x + y
f('tom')

# map(函数, 可迭代对象)
l = list(map(avg, [1, 2, 3, 4]))
print(l)


# filter
def even_number(x):
    return x % 2 == 0


res = list(filter(even_number, list(range(1, 21))))
print(res)
