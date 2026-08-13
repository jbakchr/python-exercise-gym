"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 33 - Expensive Calculations

Some operations take a long time to complete.

A decorator can store previously calculated results
and reuse them when the same inputs are provided again,
avoiding unnecessary work.
"""

import time


def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cached_results:
            print(f"Using cached result for {args[0]}")
            return cached_results[key]

        result = func(*args, **kwargs)
        cached_results[key] = result

        return result

    return wrapper


@cache
def generate_report(customer_id):
    print(f"Generating report for {customer_id}...")

    time.sleep(2)

    return {
        "customer_id": customer_id,
        "score": 95,
    }


def main():
    print(generate_report("customer-123"))
    print()

    print(generate_report("customer-123"))
    print()

    print(generate_report("customer-456"))
    print()

    print(generate_report("customer-123"))


if __name__ == "__main__":
    main()