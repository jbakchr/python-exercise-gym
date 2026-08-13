"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 35 - Production Debugging

When applications fail unexpectedly, developers need
visibility into function calls, arguments, return values,
and errors.

A decorator can provide reusable debugging information
without modifying every function.
"""


def debug(func):
    def wrapper(*args, **kwargs):
        arguments = ", ".join(str(arg) for arg in args)

        print(f"Calling {func.__name__}({arguments})")

        try:
            result = func(*args, **kwargs)
            print(f"Returned: {result}")

            return result

        except Exception as error:
            print(f"Error: {error}")
            raise

    return wrapper


@debug
def divide(a, b):
    return a / b


@debug
def calculate_discount(price, percentage):
    return price * (percentage / 100)


def main():
    divide(10, 2)

    print()

    calculate_discount(200, 15)

    print()

    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass


if __name__ == "__main__":
    main()