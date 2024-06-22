# Printing function execution

# Basic concept
def double(x):
    print('The double function was called!')
    return x * 2

def square(x):
    print('The square function was called!')
    return x * x

def greet(name):
    print('The greet function was called!')
    print(f'Hello, {name}')


answer = double(square(10))
greet("Vy")

# Auto print
def double(x):
    return x * 2

def square(x):
    return x * x

def greet(name):
    print(f'Hello, {name}')

def create_spy(func, func_name):
    def spy_func(arg):
        print(f"The {func_name} function was called!")
        return func(arg)
    return spy_func

double_spy = create_spy(double, 'double')
square_spy = create_spy(square, 'square')
greet_spy = create_spy(greet, 'greet')

answer = double_spy(square_spy(10))
greet_spy('Vy')

# 2nd pathway

def create_spy(func_name):
    def inner(func):
        def spy_func(arg):
            print(f"The {func_name} function was called!")
            return func(arg)
        return spy_func
    return inner

@create_spy('Double')
def double(x):
    return x * 2

@create_spy('Square')
def square(x):
    return x * x

@create_spy('Greet')
def greet(name):
    print(f'Hello, {name}')

answer = double_spy(square_spy(10))
greet_spy('Vy')

