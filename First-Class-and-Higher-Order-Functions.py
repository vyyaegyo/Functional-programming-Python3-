# Functions can be assigned to variables

def add_numbers(x, y):
    return x + y
my_function = add_numbers
print(my_function(2, 5))

def load_data_real():
    print('Loading data from a third party api...')
    return [100, 200, 300]
def load_data_fake():
    return [1, 2, 3]

mode = 'PROD'

load_data = load_data_real if mode == 'PROD' else load_data_fake
data = load_data()
print(data)

# Functions can be passed as arguments to other functions
def subtract_numbers(x, y):
    return x - y
def combine_10_and_11(func):
    return func(10, 11)

print(combine_10_and_11(subtract_numbers))

# Functions can also return values from other functions
def create_printer():
    name = "Vy"  # closure
    def say_hello():
        print(f"Hello from inside another function, {name}!")

    return say_hello

printer = create_printer()
printer()

def create_printer(name):
    def say_hello():
        print(f"Hello from inside another function, {name}!")

    return say_hello

printer = create_printer("Shaun")
printer()
printer_1 = create_printer("Vy")
printer_1()

