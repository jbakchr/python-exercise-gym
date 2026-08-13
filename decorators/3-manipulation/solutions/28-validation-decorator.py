"""
Exercise 28 - Validation Decorator

Goal:
Build a reusable decorator that validates
input before a function executes.

This solution demonstrates:

- Decorators
- Flexible wrappers
- Input validation
- Conditional execution
- Function arguments
- Return values
"""


def validate_positive(func):
    """Allow only positive numeric values."""

    def wrapper(*args, **kwargs):
        amount = args[0]

        if amount <= 0:
            print("Validation Failed")
            print("Value must be positive")

            return None

        return func(*args, **kwargs)

    return wrapper


@validate_positive
def withdraw(amount):
    print(f"Withdrawing {amount}")


@validate_positive
def add_points(points):
    print(f"Adding {points} points")


print("=== Valid Values ===")

withdraw(100)
print()

add_points(25)
print()


print("=== Invalid Values ===")

withdraw(-50)
print()

add_points(0)