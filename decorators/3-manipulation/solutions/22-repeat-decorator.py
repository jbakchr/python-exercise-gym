"""
Exercise 22 - Repeat Decorator

Goal:
Build a reusable decorator that can execute a function
multiple times automatically.

This solution demonstrates:

- Decorator factories
- Nested functions
- Wrappers
- Loops
- Reusable behavior
"""

def repeat(times):
    """Repeat execution of a function a specified number of times."""

    def decorator(func):

        def wrapper():
            for _ in range(times):
                func()

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


@repeat(5)
def show_line():
    print("-" * 20)


print("Greeting Example")
greet()

print("\nSeparator Example")
show_line()