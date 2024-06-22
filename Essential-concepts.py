# Imperative vs. Declarative

# Imperative

numbers = [1, 2, 4, 5, 9303, 334, -193] 

def calculate_and_print_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total/ len(numbers)
    print(f'The average is: {average}')

# Declarative

def average(numbers):
    return sum(numbers)/ len(numbers)

print(f'The average is: {sum(numbers)/ len(numbers)}')