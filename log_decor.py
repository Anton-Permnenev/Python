__author__ = 'ASUS'
import logging

def log(filename):
    def decor(func):
        def new_func(*argc, **argv):
            func(*argc, **argv)
            logging.basicConfig(level = logging.INFO ,filename =filename)
            logging.info(func.__name__)
        return new_func
    return decor
@log ("mylog.txt")
def sum(a):
    a+=9
    print(a)


sum(5)