# 3rd example
import datetime

def double(x):
    return x * 2

def square(x):
    return x * x

def greet(name):
    print(f'Hello, {name}')

def test_function(func, *args):
    start = datetime.datetime.now()
    func(*args)
    end = datetime.datetime.now()
    total_time = end - start
    print(f'The function executed in {total_time} milliseconds')

test_function(double, 10)
test_function(square, 3)
test_function(greet, "Vy")

# 4th example
import datetime

def add_performance_watch(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        total_time = end - start
        print(f'The {func.__name__} function executed in {total_time}')
        return result
    return inner

@add_performance_watch
def double(x):
    return x * 2

@add_performance_watch
def square(x):
    return x * x

@add_performance_watch
def greet(name):
    print(f'Hello, {name}')


answer = double(square(12))
greet("Vy")