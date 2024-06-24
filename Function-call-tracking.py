def print_stats(func):
    def wrapper(*args, **kwargs):
        print(f'The function {func.__name__} was called with: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'It returned {result}')
        return result

    return wrapper

import datetime

def add_performance_watch(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        total_time = end - start
        stats = {
            'args': args,
            'kwargs': kwargs,
            'result': result,
            'total_time': total_time
        }
        print(stats)
        return result
    return inner

@add_performance_watch
@print_stats
def double(x):
    return x * 2

@add_performance_watch
@print_stats
def square(x):
    return x * x

@add_performance_watch
@print_stats
def add(x, y, z):
    return x + y + z

@add_performance_watch
@print_stats
def greet(name):
    print(f'Hello, {name}')

double(26)
square(10)
add(5, 10, 15)