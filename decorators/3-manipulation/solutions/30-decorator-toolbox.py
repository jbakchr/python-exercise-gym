"""
Exercise 30 - Decorator Toolbox

Goal:
Combine multiple decorators to build a practical,
reusable solution.

This solution demonstrates:

- Decorator composition
- Validation
- Call counting
- Timing
- Logging
- Separation of concerns
"""


import time


def count_calls(func):
    """Track how many times a function is called."""

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count

        count += 1

        print(
            f"{func.__name__} has been called "
            f"{count} time(s)"
        )

        return func(*args, **kwargs)

    return wrapper


def validate_positive(func):
    """Allow only positive numeric values."""

    def wrapper(*args, **kwargs):
        amount = args[0]

        if amount <= 0:
            print("Validation Failed")
            print("Value must be positive")

            return None

        return func(*args, **kwargs)

    return wrapper


def timer(func):
    """Measure execution time."""

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print(
            f"{func.__name__} took "
            f"{end_time - start_time:.4f} seconds"
        )

        return result

    return wrapper


def log_calls(filename):
    """Log function activity."""

    def decorator(func):

        def wrapper(*args, **kwargs):
            with open(filename, "a") as file:
                file.write(
                    f"{func.__name__} called\n"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@count_calls
@log_calls("app.log")
@validate_positive
@timer
def purchase(amount):
    """Process a purchase."""

    time.sleep(1)

    print(
        f"Processing purchase: {amount}"
    )


print("=== Valid Purchase ===")

purchase(100)

print()

print("=== Invalid Purchase ===")

purchase(-50)

print()

print("=== Another Valid Purchase ===")

purchase(250)

print()

print("Check app.log")