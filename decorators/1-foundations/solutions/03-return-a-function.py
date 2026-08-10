"""
Exercise 03 - Return a Function

Functions can be created inside other functions and
returned as values.

This is one of the fundamental building blocks behind
decorators.
"""


def create_greeter():
    """Create and return a greeting function."""

    def greet():
        """Print a greeting."""
        print("Hello!")

    return greet


# Store the returned function in a variable.
my_greeter = create_greeter()

# Execute the returned function.
my_greeter()