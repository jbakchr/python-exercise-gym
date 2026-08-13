"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 40 - Decorator Design Challenge

Real applications often require multiple cross-cutting
concerns such as validation, caching, monitoring,
and authorization.

Decorators can be combined to solve these concerns
while keeping business logic clean and maintainable.
"""

import time


def validate_not_empty(func):
    def wrapper(value, *args, **kwargs):
        if value == "":
            print("Validation failed.")
            return

        return func(value, *args, **kwargs)

    return wrapper


def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cached_results:
            print("Using cached result")
            return cached_results[key]

        result = func(*args, **kwargs)
        cached_results[key] = result

        return result

    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.2f} seconds")

        return result

    return wrapper


def requires_role(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print("Access denied.")
                return

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


@validate_not_empty
def create_user(name):
    print(f"Creating user: {name}")


@cache
@measure_time
def generate_report(customer_id):
    print(f"Generating report for {customer_id}")

    time.sleep(1)

    return {
        "customer_id": customer_id,
        "score": 95,
    }


@requires_role("admin")
def delete_user(user_role):
    print("Deleting user...")


@measure_time
def calculate_statistics():
    print("Calculating statistics...")

    time.sleep(0.5)


def main():
    create_user("Alice")
    create_user("")

    print()

    print(generate_report("customer-123"))
    print(generate_report("customer-123"))

    print()

    delete_user("admin")
    delete_user("guest")

    print()

    calculate_statistics()


if __name__ == "__main__":
    main()