"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 17 - Function Metadata

Decorators replace the original function with
the wrapper function.

As a result, metadata such as __name__ may no
longer reflect information about the original
function.
"""


def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper


@announce
def greet():
    """Display a greeting."""
    print("Hello")



print(greet.__name__)