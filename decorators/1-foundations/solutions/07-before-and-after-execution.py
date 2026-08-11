"""
Exercise 07 - Before and After Execution

A wrapper can execute code before and after a
wrapped function runs.

This is one of the most common patterns used by
decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """Create and return a wrapper function."""

    def wrapper():
        """Execute code around the wrapped function."""
        print("Before")
        func()
        print("After")

    return wrapper


# Create a wrapped version of say_hello.
wrapped_hello = wrap(say_hello)

# Execute the wrapper.
wrapped_hello()