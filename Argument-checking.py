

def second_arg_not_zero(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print(f'The second arg cannot be zero for the function {func.__name__}')
            return
        
        return func(*args, **kwargs)
    return wrapper

def args_are_same_length(func):
    def wrapper(*args, **kwargs):
        if len(args[0]) != len(args[1]):
            print(f'The first two args must be the same length in function {func.__name__}')
            return
        return func(*args, **kwargs)
    return wrapper

def first_two_args_are_lists(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], list) or not isinstance(args[1], list):
            print(f'The first two arguments of {func.__name__} must be lists!')
            return
        return func(*args, **kwargs)
    return wrapper

@second_arg_not_zero
def divide(x, y):
    return x/y
@first_two_args_are_lists
@args_are_same_length
def add_elements(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

print(add_elements([1, 2, 3], 2))