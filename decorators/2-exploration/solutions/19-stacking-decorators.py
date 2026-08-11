"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 19 - Stacking Decorators

Multiple decorators can be applied to the same
function.

Each decorator wraps the result of the previous
decorator, creating a chain of execution.

The order of decorators affects the final output.
"""

from functools import wraps


def before(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)

    return wrapper


def after(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@before
@after
def greet():
    print("Hello")


def main():
    greet()


if __name__ == "__main__":
    main()