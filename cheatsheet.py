from functools import wraps
import time

def watch_func(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        process_time =  time.time() - start
        print(f"{func.__name__}は{process_time}秒かかりました")
        return result
    return wrapper

from contextlib import contextmanager

@contextmanager
def watch(name):
    start = time.time()
    yield
    process_time =  time.time() - start
    print(f"{name}は{process_time}秒かかりました")