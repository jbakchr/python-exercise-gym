"""
Exercise 04 - Create Your First Wrapper

A wrapper function is a function that calls another function.

Wrappers are one of the fundamental building blocks
behind decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrapper():
    """Execute the wrapped function."""
    say_hello()


# Call the wrapper.
wrapper()