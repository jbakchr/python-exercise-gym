"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Mini Project - Decorator Monitoring Toolkit

A reusable collection of decorators can help solve
common application concerns such as monitoring,
validation, authorization, and performance tracking.

This project demonstrates how multiple decorators
can work together while keeping business logic clean.
"""

import time


usage_counts = {}


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution time: {end - start:.2f} seconds")

        return result

    return wrapper


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


def requires_role(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print("Access denied.")
                return

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


def track_usage(func):
    def wrapper(*args, **kwargs):
        usage_counts[func.__name__] = (
            usage_counts.get(func.__name__, 0) + 1
        )

        return func(*args, **kwargs)

    return wrapper


@validate_not_empty
@track_usage
def create_user(name):
    print(f"Creating user: {name}")


@track_usage
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
@track_usage
def delete_user(user_role):
    print("Deleting user...")


@track_usage
def export_data():
    print("Exporting data...")


def show_usage():
    print("\nUsage Statistics")

    for function_name, count in usage_counts.items():
        print(f"{function_name}: {count} calls")


def main():
    create_user("Alice")
    create_user("")

    print()

    report = generate_report("customer-123")
    print(report)

    print()

    report = generate_report("customer-123")
    print(report)

    print()

    delete_user("admin")
    delete_user("guest")

    print()

    export_data()
    export_data()

    show_usage()


if __name__ == "__main__":
    main()
