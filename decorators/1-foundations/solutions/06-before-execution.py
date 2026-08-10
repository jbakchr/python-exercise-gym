"""
Exercise 06 - Before Execution

A wrapper can add behavior before a function runs.

This is one of the core ideas behind decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """Create and return a wrapper function."""

    def wrapper():
        """Execute code before the wrapped function."""
        print("Starting...")
        func()

    return wrapper


# Create a wrapped version of say_hello.
wrapped_hello = wrap(say_hello)

# Execute the wrapper.
wrapped_hello()