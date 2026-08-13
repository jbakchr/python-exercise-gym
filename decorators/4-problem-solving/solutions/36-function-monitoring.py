"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 36 - Function Monitoring

Applications often need usage information to understand
which features are being used most frequently.

A decorator can automatically track function usage
without placing counting logic inside every function.
"""

usage_counts = {}


def monitor(func):
    def wrapper(*args, **kwargs):
        usage_counts[func.__name__] = (
            usage_counts.get(func.__name__, 0) + 1
        )

        return func(*args, **kwargs)

    return wrapper


@monitor
def generate_report():
    print("Generating report...")


@monitor
def export_data():
    print("Exporting data...")


@monitor
def create_user():
    print("Creating user...")


def show_usage():
    for function_name, count in usage_counts.items():
        print(f"{function_name}: {count} calls")


def main():
    generate_report()
    generate_report()
    generate_report()

    export_data()

    create_user()
    create_user()

    print()

    show_usage()


if __name__ == "__main__":
    main()