# 衡量函数需要计算函数的运行时间，通常使用 timeit 模块来测量代码的执行时间。以下是一个示例，展示如何使用 timeit 模块来衡量函数的运行时间：
# class timeit.Timer(stmt='pass', setup='pass', timer=<default_timer>, globals=None)
from timeit import Timer

# l1 = [1,2]
# l2 = [3, 4]
# li = l1+l2

# li = [i for i in range(10000)]
# li = list(range(10000))
def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li = li + [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10001))

timer1 = Timer('t1()',"from __main__ import test1")
print("t1- append: ", timer1.timeit(number=1000))
timer2 = Timer('t2()',"from __main__ import test2")
print("t2- concatenation: ", timer2.timeit(number=1000))
timer3 = Timer('t3()',"from __main__ import test3")
print("t3- list comprehension: ", timer3.timeit(number=1000))
timer4 = Timer('t4()',"from __main__ import test4")
print("t4- list constructor: ", timer4.timeit(number=1000))