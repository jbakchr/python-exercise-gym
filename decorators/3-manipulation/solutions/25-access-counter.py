"""
Exercise 25 - Access Counter

Goal:
Build a reusable decorator that tracks how many
times a function has been called.

This solution demonstrates:

- Decorators
- Flexible wrappers
- State management
- Closures
- Function call tracking
- Return values
"""


def count_calls(func):
    """Count and display how many times a function is called."""

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count

        count += 1

        print(
            f"{func.__name__} has been called "
            f"{count} time(s)"
        )

        return func(*args, **kwargs)

    return wrapper


@count_calls
def greet(name):
    return f"Hello {name}"


@count_calls
def add(a, b):
    return a + b


@count_calls
def calculate_area(width, height):
    return width * height


# Example 1

print(greet("Jonas"))
print()

print(greet("Jonas"))
print()

print(greet("Jonas"))
print()


# Example 2

print(add(2, 3))
print()

print(add(10, 20))
print()


# Example 3

print(calculate_area(width=5, height=10))
print()

print(calculate_area(width=8, height=4))