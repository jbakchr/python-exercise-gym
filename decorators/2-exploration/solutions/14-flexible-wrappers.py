"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 14 - Flexible Wrappers

Some functions use positional arguments while
others use keyword arguments.

A flexible wrapper can handle both by accepting
*args and **kwargs and forwarding them to the
wrapped function.
"""


def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        func(*args, **kwargs)

    return wrapper


@announce
def create_account(username, active=True):
    print(f"{username} ({active})")



create_account("Alice", active=False)