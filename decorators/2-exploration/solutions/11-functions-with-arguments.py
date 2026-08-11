"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 11 - Functions With Arguments

Decorators often need to work with functions that
accept arguments.

A wrapper can receive arguments using *args and
forward them to the wrapped function.
"""


def announce(func):
    def wrapper(*args):
        print("Calling function...")
        func(*args)

    return wrapper


@announce
def greet(name):
    print(f"Hello {name}")


def main():
    greet("Alice")


if __name__ == "__main__":
    main()