"""
Exercise 26 - Cache Decorator

Goal:
Build a reusable decorator that stores and reuses
previously calculated results.

This solution demonstrates:

- Decorators
- Flexible wrappers
- State management
- Closures
- Dictionaries
- Performance optimization
- Return values
"""


def cache(func):
    """Store and reuse previously calculated results."""

    cache_store = {}

    def wrapper(*args):
        if args in cache_store:
            print("Using cached result")
            return cache_store[args]

        print("Calculating...")

        result = func(*args)

        cache_store[args] = result

        return result

    return wrapper


@cache
def square(number):
    return number * number


@cache
def multiply(a, b):
    return a * b


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Example 1

print(square(5))
print()

print(square(5))
print()

print(square(5))
print()


# Example 2

print(multiply(3, 4))
print()

print(multiply(3, 4))
print()


# Example 3

print(fibonacci(10))
print()

print(fibonacci(10))