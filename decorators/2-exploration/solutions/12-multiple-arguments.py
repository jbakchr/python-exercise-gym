"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 12 - Multiple Arguments

The *args parameter allows a decorator to receive
any number of positional arguments.

This makes it possible for a single decorator to
work with functions that accept different numbers
of arguments.
"""


def announce(func):
    def wrapper(*args):
        print("Calling function...")
        func(*args)

    return wrapper


@announce
def add(a, b):
    print(a + b)


def main():
    add(10, 20)


if __name__ == "__main__":
    main()