# Fibonacci numbers form a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1

cached_results = {}

def fib(x):
    if x in cached_results:
        return cached_results[x]
    else:
        new_result = 1 if x <= 1 else fib(x - 1) + fib(x - 2)
        cached_results[x] = new_result
        print(cached_results)
        return new_result

print(fib(20))


# Multi-arg-memoization

def memoize(func):
    results ={}

    def memoized(*args):
        arg_str = str(args)

        if arg_str in results:
            print('Found previously cached result!')
            return results[arg_str]
        else:
            print('Calculating new result...')
            new_result = func(*args)
            results[arg_str] = new_result
            return new_result
        return memoized
    return memoize

@memoize
def add(x + y + z):
    return x + y + z

print(add(1, 2, 3))