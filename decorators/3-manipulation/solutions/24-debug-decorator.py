"""
Exercise 24 - Debug Decorator

Goal:
Build a reusable debugging decorator that displays
function calls, arguments, and return values.

This solution demonstrates:

- Decorators
- Flexible wrappers
- *args
- **kwargs
- Return values
- Debugging utilities
"""


def debug(func):
    """Display information about function calls."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Returned: {result}")
        print()

        return result

    return wrapper


@debug
def add(a, b):
    return a + b


@debug
def greet(name, excited=False):
    if excited:
        return f"Hello {name}!"

    return f"Hello {name}"


@debug
def calculate_area(width, height):
    return width * height


# Example 1

result = add(3, 5)

print(f"Final Result: {result}")
print()


# Example 2

message = greet("Jonas", excited=True)

print(f"Final Result: {message}")
print()


# Example 3

area = calculate_area(width=10, height=5)

print(f"Final Result: {area}")