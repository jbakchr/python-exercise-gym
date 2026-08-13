"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 39 - Background Task Tracking

Long-running tasks are easier to monitor when
developers can see when they start, when they finish,
and how long they take to execute.

Decorators can be combined to add monitoring
behaviour while keeping business logic clean.
"""

import time


def log_task(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")

        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")

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


@log_task
@measure_time
def generate_monthly_report():
    print("Generating monthly report...")

    time.sleep(2)


@log_task
@measure_time
def backup_database():
    print("Backing up database...")

    time.sleep(1)


def main():
    generate_monthly_report()

    print()

    backup_database()


if __name__ == "__main__":
    main()