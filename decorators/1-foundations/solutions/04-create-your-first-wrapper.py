"""
Exercise 04 - Create Your First Wrapper

The goal of this exercise is to create your first wrapper function.

A wrapper is simply a function that calls another function.

This concept is extremely important because decorators
are built around wrapper functions.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrapper():
    """
    Wrap the say_hello() function.

    The wrapper acts as a middleman.
    Instead of calling say_hello() directly,
    we call wrapper(), which then calls say_hello().
    """
    say_hello()


# Execute the wrapper.
wrapper()


# ------------------------------------------------------------------
# Additional experiments
# ------------------------------------------------------------------

print("\nCalling the wrapper again:")
wrapper()


def say_goodbye():
    """Print a farewell message."""
    print("Goodbye!")


def goodbye_wrapper():
    """Wrap the say_goodbye() function."""
    say_goodbye()


print("\nUsing another wrapper:")
goodbye_wrapper()


def wrapper_twice():
    """Call the wrapped function twice."""
    say_hello()
    say_hello()


print("\nCalling the wrapped function twice:")
wrapper_twice()


# Stretch Goal Example
def announcing_wrapper():
    """
    Add behavior before the wrapped function.

    This begins to resemble what decorators do.
    """
    print("Starting...")
    say_hello()


print("\nStretch Goal:")
announcing_wrapper()