"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 31 - Slow API Calls

Applications often need visibility into how long
operations take to execute.

A decorator can be used to measure execution time
without duplicating timing code inside every function.
"""

import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        elapsed = end - start

        print(f"{func.__name__} completed in {elapsed:.2f} seconds")

        return result

    return wrapper


@measure_time
def fetch_users():
    time.sleep(1)
    return ["Alice", "Bob"]


@measure_time
def fetch_orders():
    time.sleep(2)
    return ["Order 1", "Order 2"]


@measure_time
def fetch_products():
    time.sleep(0.5)
    return ["Laptop", "Keyboard"]


def main():
    users = fetch_users()
    orders = fetch_orders()
    products = fetch_products()

    print(users)
    print(orders)
    print(products)


if __name__ == "__main__":
    main()