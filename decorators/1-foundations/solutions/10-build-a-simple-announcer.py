"""
Exercise 10 - Build a Simple Announcer

This exercise combines the key concepts learned
throughout the Foundations stage:

- Functions as objects
- Passing functions
- Returning functions
- Wrapper functions
- Decorator syntax
- Reusable decorators
"""


def announce(func):
    """Create and return an announcing wrapper."""

    def wrapper():
        """Announce the start and end of a function call."""
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
    """Print a farewell."""
    print("Goodbye!")


@announce
def say_welcome():
    """Print a welcome message."""
    print("Welcome!")


# Execute all decorated functions.
say_hello()
say_goodbye()
say_welcome()