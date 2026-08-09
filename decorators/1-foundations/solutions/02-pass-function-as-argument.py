"""
Exercise 02 - Pass Function as Argument

The goal of this exercise is to understand that functions
can be passed to other functions just like any other value.

This concept is one of the fundamental building blocks
behind decorators.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


def run(action):
    """
    Execute the function that was passed in.

    Parameters
    ----------
    action : function
        The function to execute.
    """
    action()


# Pass the function object into run().
#
# Notice:
# We pass say_hello itself, not say_hello().
#
# Correct:
#     run(say_hello)
#
# Incorrect:
#     run(say_hello())
#
# The incorrect version executes the function immediately
# before run() receives it.
run(say_hello)


# ------------------------------------------------------------------
# Additional experiments
# ------------------------------------------------------------------


def say_goodbye():
    """Print a farewell message."""
    print("Goodbye!")


print("\nRunning another function:")
run(say_goodbye)


def say_name():
    """Print a name."""
    print("Jonas")


print("\nRunning a third function:")
run(say_name)


def run_twice(action):
    """Execute the supplied function two times."""
    action()
    action()


print("\nRunning the same function twice:")
run_twice(say_hello)