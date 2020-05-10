from functools import *

class Sample:
    #  python 3.8 ~
    @singledispatchmethod
    def sum(self,a,b):
        print('default sum method')
        return a + b
    @sum.register
    def sum(self,a:int,b:int):
        print('int sum method')
        return a + b

def hoge_decorator(f):
    # 元の関数のdocstringを保持する
    @wraps(f)
    def hoge_wrapper(*args, **kwargs):
        """デコレータのDocstringだよ"""
        print("デコレータだよ")
        return f(*args, **kwargs)
    return hoge_wrapper

@hoge_decorator
def hoge_function():
    """デコってる関数のDocstringだよ"""
    print("これがデコってる関数だ！")

s = Sample()
s.sum(1,2)

hoge_function()
help(hoge_function)

l1 = [1, 2, 3]
l2 = [10, 20, 30]
from itertools import *
print(product(l1,l2))

def nested_for(first_iter, second_iter):
    for i in first_iter:
        for j in second_iter:
            pass
def nested_for2(first_iter, second_iter):
    for i in first_iter:
        for j in second_iter:
            yield i,j

def using_product(first_iter, second_iter):
    for i,j in product(first_iter, second_iter):
        pass
def using_product2(first_iter, second_iter):
    for i,j in nested_for2(first_iter, second_iter):
        pass
from timeit import timeit
timer = partial(timeit, number=10000, globals=globals())

time = timer("nested_for(range(100), range(100))")
print(time)
time = timer("using_product(range(100), range(100))")
print(time)
time = timer("using_product2(range(100), range(100))")
print(time)