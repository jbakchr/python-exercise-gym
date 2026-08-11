"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 16 - Reusable Decorators

A reusable decorator can be applied to many
different functions without modification.

Flexible wrappers make it possible for one
decorator to add the same behavior across
multiple functions.
"""


def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper


@announce
def greet(name):
    return f"Hello {name}"


@announce
def add(a, b):
    return a + b


@announce
def create_user(name):
    return {"name": name}


def main():
    print(greet("Alice"))
    print(add(2, 3))
    print(create_user("Alice"))


if __name__ == "__main__":
    main()