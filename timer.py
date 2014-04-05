__author__ = 'ASUS'
import time
def timer(func):
    def new_func(*argc, **argv):
        t1=time.time()
        func(*argc, **argv)
        t2=time.time()
        print(t2-t1)
    return new_func

@timer
def func(a):
    for i in range(100000000):
        a+=9
    print(a)


func(5)