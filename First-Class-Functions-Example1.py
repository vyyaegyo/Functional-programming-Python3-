# Example 1: Sale calculator

# Basic concept

def calculate_price_20(price):
    return price * 0.8

def calculate_price_10(price):
    return price * 0.9

def calculate_clearance_price(price):
    return price * 0.5

print(calculate_price_20(100))
print(calculate_price_10(100))
print(calculate_clearance_price(100))

# Apply first-class function
def create_sales_calculator(percent_discount):
    def calculator(price):
        return price * (1- (percent_discount / 100))
    
    return calculator
Twenty_percent_off = create_sales_calculator(20)
Ten_percent_off = create_sales_calculator(10)
Clearance_price = create_sales_calculator(50)

print(Twenty_percent_off(100))
print(Ten_percent_off(100))
print(Clearance_price(100))