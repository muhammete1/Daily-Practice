"""
31.05.2022

Decorator
"""
import time


def decorator(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        finish = time.time()
        print(f"The Process took {finish - start} second.")
    return wrapper


@decorator
def sum_(a,b):
    time.sleep(2)
    print("a + b:", a + b)


@decorator
def square_(a):
    time.sleep(1)
    print("Value of 'a':", a ** 2)


@decorator
def cube(lst):
    for i in lst:
        print(i ** 3)


# sum_(1,3)
square_(142345346345342342352342352343423425234325234)
# cube([1,2,3,4])