"""
Exercise 06 - Before Execution

The goal of this exercise is to learn that a wrapper function
can execute code before the wrapped function runs.

This is one of the most common patterns used in decorators.

Concepts used:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions
- Adding behavior before execution
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """
    Receive a function and return a wrapper that
    performs additional work before the function runs.
    """

    def wrapper():
        """
        Execute code before calling the wrapped function.
        """
        print("Starting...")
        func()

    return wrapper


# Wrap the function.
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


def wrap_with_more_messages(func):
    """
    Execute several actions before calling the function.
    """

    def wrapper():
        print("Preparing...")
        print("Starting...")
        func()

    return wrapper


verbose_hello = wrap_with_more_messages(say_hello)

print("\nMultiple pre-execution messages:")
verbose_hello()


# ------------------------------------------------------------------
# Stretch Goal Example
# ------------------------------------------------------------------


def wrap_with_function_name(func):
    """
    Display the function name before execution.
    """

    def wrapper():
        print(f"Starting {func.__name__}...")
        func()

    return wrapper


named_hello = wrap_with_function_name(say_hello)

print("\nStretch Goal:")
named_hello()