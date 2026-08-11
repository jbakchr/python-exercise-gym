"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 13 - Keyword Arguments

Decorators may need to work with functions that
receive keyword arguments.

A wrapper can collect keyword arguments using
**kwargs and forward them to the wrapped function.
"""


def announce(func):
    def wrapper(**kwargs):
        print("Calling function...")
        func(**kwargs)

    return wrapper


@announce
def create_user(name):
    print(f"Created user: {name}")



create_user(name="Alice")
