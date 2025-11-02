def greet(name):
    return f"Hello, {name}! Welcome back."

def area_of_circle(radius):
    import math
    return math.pi * radius * radius

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
