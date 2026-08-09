"""
Exercise 05 - Wrap a Function

The goal of this exercise is to combine everything learned
so far into a simple wrapping mechanism.

This is the first exercise that closely resembles the
structure of a real decorator.

Concepts used:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """
    Receive a function, create a wrapper around it,
    and return the wrapper.
    """

    def wrapper():
        """
        Execute the wrapped function.
        """
        func()

    return wrapper


# Wrap the function.
#
# The returned value is the wrapper function.
wrapped_hello = wrap(say_hello)

print("Calling wrapped_hello():")
wrapped_hello()


# ------------------------------------------------------------------
# Additional experiments
# ------------------------------------------------------------------


def say_goodbye():
    """Print a farewell message."""
    print("Goodbye!")


wrapped_goodbye = wrap(say_goodbye)

print("\nCalling wrapped_goodbye():")
wrapped_goodbye()


print("\nCalling wrapped_hello() again:")
wrapped_hello()


# Stretch Goal Example
def wrap_with_message(func):
    """
    Add behavior before executing the function.
    """

    def wrapper():
        print("Calling function...")
        func()

    return wrapper


announced_hello = wrap_with_message(say_hello)

print("\nStretch Goal:")
announced_hello()


# Demonstrating the execution flow.
print("\nUnderstanding the flow:")
print("say_hello --> wrap() --> wrapper --> execution")
