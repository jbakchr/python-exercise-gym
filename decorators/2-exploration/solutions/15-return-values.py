"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 15 - Return Values

Decorators can accidentally discard return values.

A wrapper must return the result of the wrapped
function if the original behavior should be
preserved.
"""


def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper


@announce
def add(a, b):
    return a + b



result = add(2, 3)
print(result)
