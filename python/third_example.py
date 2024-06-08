def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fib_series.append(b)
        return fib_series

if __name__ == "__main__":
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
    print(f"Prime numbers less than {n}: {[i for i in range(n) if is_prime(i)]}")
    print(f"Fibonacci series of length {n}: {fibonacci(n)}")

