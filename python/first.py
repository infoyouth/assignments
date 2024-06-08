import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

result = add(5, 3)
print("Addition result:", result)

result = subtract(5, 3)
print("Subtraction result:", result)

result = multiply(5, 3)
print("Multiplication result:", result)

result = divide(5, 3)
print("Division result:", result)
