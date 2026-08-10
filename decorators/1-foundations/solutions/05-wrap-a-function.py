"""
Exercise 05 - Wrap a Function

A function can receive another function, create a
wrapper around it, and return that wrapper.

This is the core pattern behind decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """Create and return a wrapper function."""

    def wrapper():
        """Execute the wrapped function."""
        func()

    return wrapper


# Create a wrapped version of say_hello.
wrapped_hello = wrap(say_hello)

# Execute the returned wrapper.
wrapped_hello()