"""
Exercise 09 - Multiple Decorated Functions

A single decorator can be applied to many different
functions.

This allows behavior to be written once and reused
throughout a program.
"""


def announce(func):
    """Create and return a wrapper function."""

    def wrapper():
        """Add behavior around the wrapped function."""
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


# Execute all decorated functions.
say_hello()
say_goodbye()
say_welcome()