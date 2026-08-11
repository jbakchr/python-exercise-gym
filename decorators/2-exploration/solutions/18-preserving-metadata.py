"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 18 - Preserving Metadata

Decorators can hide information about the
original function.

functools.wraps copies important metadata from
the wrapped function to the wrapper.
"""

from functools import wraps


def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper


@announce
def greet(name):
    """Return a greeting."""
    return f"Hello {name}"


def main():
    print(greet.__name__)
    print(greet.__doc__)


if __name__ == "__main__":
    main()