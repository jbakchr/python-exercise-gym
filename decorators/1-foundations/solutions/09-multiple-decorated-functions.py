"""
Exercise 09 - Multiple Decorated Functions

The goal of this exercise is to understand that a single
decorator can be reused across multiple functions.

This demonstrates one of the biggest benefits of decorators:

    Reuse.

Instead of adding the same behavior to many functions,
we can add it once in a decorator and apply it wherever
it is needed.
"""


def announce(func):
    """
    A simple decorator that adds behavior before
    and after a function executes.
    """

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@announce
def say_hello():
    """Print a greeting."""
    print("Hello!")


@announce
def say_goodbye():
    """Print a farewell."""
    print("Goodbye!")


@announce
def say_welcome():
    """Print a welcome message."""
    print("Welcome!")


if __name__ == "__main__":
    print("=== Reusing One Decorator ===")

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

    print("\n=== Additional Decorated Function ===")

    say_thanks()

    # --------------------------------------------------------------
    # Changing the decorator affects all decorated functions
    # --------------------------------------------------------------

    def status(func):
        """
        Alternative decorator implementation.
        """

        def wrapper():
            print("Starting...")
            func()
            print("Finished.")

        return wrapper

    @status
    def process_data():
        print("Processing data...")

    @status
    def save_results():
        print("Saving results...")

    print("\n=== Different Decorator ===")

    process_data()

    print()

    save_results()

    # --------------------------------------------------------------
    # Stretch Goal Example
    # --------------------------------------------------------------

    def announce_with_name(func):
        """
        Display the function name before and after execution.
        """

        def wrapper():
            print(f"Before calling {func.__name__}")
            func()
            print(f"After calling {func.__name__}")

        return wrapper

    @announce_with_name
    def greet_user():
        print("Hello, Jonas!")

    print("\n=== Stretch Goal ===")

    greet_user()