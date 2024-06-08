import os

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print(greet("Alice"))
    print("Addition result:", add(5, 3))
    print("Subtraction result:", subtract(5, 3))
    print("Division result:", divide(5, 3))

if __name__ == "__main__":
    main()
