"""
Exercise 02 - Pass Function as Argument

Functions can be passed to other functions just like
any other value.

This concept is one of the fundamental building blocks
behind decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def run(action):
    """Execute the function that was received."""
    action()


# Pass the function into run().
# Notice that we pass the function itself,
# not the result of calling the function.
run(say_hello)