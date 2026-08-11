"""
Exercise 08 - Understanding @ Syntax

Decorator syntax is a shortcut for manually wrapping a function.

These two approaches are equivalent:

    say_hello = wrap(say_hello)

and:

    @wrap
    def say_hello():
        ...
"""


def wrap(func):
    """Create and return a wrapper function."""

    def wrapper():
        """Execute code before and after the wrapped function."""
        print("Before")
        func()
        print("After")

    return wrapper


# ------------------------------------------------------------------
# Part 1: Manual Wrapping
# ------------------------------------------------------------------


def say_hello():
    """Print a greeting."""
    print("Hello!")


say_hello = wrap(say_hello)

say_hello()


# ------------------------------------------------------------------
# Part 2: Decorator Syntax
# ------------------------------------------------------------------


@wrap
def say_hello_decorated():
    """Print a greeting."""
    print("Hello!")


say_hello_decorated()
