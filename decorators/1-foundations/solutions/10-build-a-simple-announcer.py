"""
Exercise 10 - Build a Simple Announcer

Foundations Capstone

The goal of this exercise is to combine everything learned
throughout the Foundations section into a reusable decorator.

Concepts used:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions
- Decorator syntax (@)
- Reusable decorators

This is the first complete decorator utility built in the
Decorators topic.
"""

from datetime import datetime


def announce(func):
    """
    Announce when a function starts and finishes.

    The decorator displays the function name before and
    after execution.
    """

    def wrapper():
        print(f"Starting {func.__name__}...")
        func()
        print(f"Finished {func.__name__}.")

    return wrapper


@announce
def say_hello():
    """Print a greeting."""
    print("Hello!")


@announce
def say_goodbye():
    """Print a farewell message."""
    print("Goodbye!")


@announce
def say_welcome():
    """Print a welcome message."""
    print("Welcome!")


if __name__ == "__main__":
    print("=== Simple Announcer ===\n")

    say_hello()

    print()

    say_goodbye()

    print()

    say_welcome()

    # --------------------------------------------------------------
    # Additional experiments
    # --------------------------------------------------------------

    @announce
    def say_thanks():
        print("Thanks!")

    print("\n=== Additional Decorated Function ===\n")
    say_thanks()

    # --------------------------------------------------------------
    # Multiple statements inside a decorated function
    # --------------------------------------------------------------

    @announce
    def run_report():
        print("Loading data...")
        print("Generating report...")
        print("Saving results...")

    print("\n=== Multi-Step Function ===\n")
    run_report()

    # --------------------------------------------------------------
    # Stretch Goal Example
    # --------------------------------------------------------------

    def announce_with_timestamp(func):
        """
        Announce function execution with a timestamp.
        """

        def wrapper():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{timestamp}]")
            print(f"Starting {func.__name__}...")

            func()

            print(f"Finished {func.__name__}.")

        return wrapper

    @announce_with_timestamp
    def deploy_application():
        print("Deploying application...")

    print("\n=== Stretch Goal ===\n")
    deploy_application()