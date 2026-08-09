"""
Exercise 07 - Before and After Execution

The goal of this exercise is to learn that a wrapper function
can execute code both before and after the wrapped function runs.

This is one of the most common patterns used in decorators.

Concepts used:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions
- Adding behavior before execution
- Adding behavior after execution
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def wrap(func):
    """
    Receive a function and return a wrapper that
    executes code before and after the function.
    """

    def wrapper():
        """
        Add behavior around the wrapped function.
        """
        print("Before")
        func()
        print("After")

    return wrapper


if __name__ == "__main__":
    # Wrap the function.
    wrapped_hello = wrap(say_hello)

    print("Calling wrapped_hello():")
    wrapped_hello()

    # --------------------------------------------------------------
    # Additional experiments
    # --------------------------------------------------------------

    def say_goodbye():
        """Print a farewell message."""
        print("Goodbye!")

    wrapped_goodbye = wrap(say_goodbye)

    print("\nCalling wrapped_goodbye():")
    wrapped_goodbye()

    print("\nCalling wrapped_hello() again:")
    wrapped_hello()

    # --------------------------------------------------------------
    # Experiment with different messages
    # --------------------------------------------------------------

    def wrap_with_status(func):
        """
        Display more descriptive messages.
        """

        def wrapper():
            print("Starting...")
            func()
            print("Finished.")

        return wrapper

    status_hello = wrap_with_status(say_hello)

    print("\nUsing status messages:")
    status_hello()

    # --------------------------------------------------------------
    # Stretch Goal Example
    # --------------------------------------------------------------

    def wrap_with_function_name(func):
        """
        Include the function name in the messages.
        """

        def wrapper():
            print(f"Starting {func.__name__}...")
            func()
            print(f"Finished {func.__name__}.")

        return wrapper

    named_hello = wrap_with_function_name(say_hello)

    print("\nStretch Goal:")
    named_hello()