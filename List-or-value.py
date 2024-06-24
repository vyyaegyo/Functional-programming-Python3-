def list_or_value(func):
    def wrapper(arg):
        if isinstance(arg, list):
            return list(map(func, arg))
        else:
            return func(arg)
        
    return wrapper

@list_or_value
def double(x):
    return x * 2

@list_or_value
def minus_one(x):
    return x -1

numbers = [1, 2, 3, 4, 5]

print(double(numbers))
print(minus_one(numbers))