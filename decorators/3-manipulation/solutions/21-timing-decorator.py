"""
Exercise 21 - Timing Decorator

Goal:
Build a reusable decorator that measures how long a
function takes to execute.

This solution demonstrates:

- Basic decorators
- Wrappers
- Timing execution
- Returning original results
"""

import time


def timer(func):
    """Measure and display function execution time."""

    def wrapper():
        start_time = time.perf_counter()

        result = func()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"{func.__name__} took {elapsed_time:.4f} seconds")

        return result

    return wrapper


@timer
def process_data():
    """Simulate a slow operation."""
    time.sleep(1)
    return "Processing complete"


result = process_data()

print(result)