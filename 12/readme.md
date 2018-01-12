# 并发编程
```python
import time
time.sleep(1)
```
## _thread (不推荐使用)
```python
import _thread
def fun():
    pass
# 函数 参数
_thread.start_new_thread(fun, (4,))
# 只有一个同步原语(锁)
```
## threading
```python
import threading
def fun():
    pass
threads = []
t1 = threading.Thread(target=fun, args=(4,))
threads.append(t1)
t2 = threading.Thread(target=fun, args=(2,))
threads.append(t2)
for t in threads:
    t.start()
    
for t in threads:
    t.join()


class MyThread(threading.Thread):
    def __int__(self, func, args):
        super.__init__()
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)
```

## 锁
```python
import threading
import time
import random
egg = []
# def put_egg(n, lst):
#     for i in range(1, n+1):
#         time.sleep(random.randint(0, 2))
#         lst.append(i)

def main():
    thread = []
    for i in range(3):
        t = threading.Thread(target=put_egg, args=(5,egg))
        thread.append(t)
 
    for t in thread:
        t.start()
    for t in thread:
        t.join()
    print(egg)

lock = threading.Lock()
def put_egg(n, lst):
    lock.acquire()
    for i in range(1, n+1):
        time.sleep(random.randint(0, 2))
        lst.append(i)
    lock.release()
    
    
def put_egg(n, lst):
    with lock:
        for i in range(1, n+1):
            time.sleep(random.randint(0, 2))
            lst.append(i)
```

## 队列
### Queue
```python
import queue
q=queue.Queue()
q.put()
q.get()
q.task_done()

queue.Empty # 异常
```
### LifoQueue (stack)
### PriorityQueue

## 多进程
## multiprocessing
```python
import multiprocessing

p1 = multiprocessing.Process(target='', args=(4,))
p1.start()
p1.join()
```
## concurrent.future
### ThreadPoolExecutor
```python
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.submit(function, i)
    
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    executor.submit(function, i)
```