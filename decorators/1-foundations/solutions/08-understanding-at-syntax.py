"""
Exercise 08 - Understanding @ Syntax

The goal of this exercise is to understand that the
@decorator syntax is simply a shortcut.

These two approaches are equivalent:

    greet = wrap(greet)

and

    @wrap
    def greet():
        ...

There is no magic involved.
Python simply performs the assignment automatically.
"""


def wrap(func):
    """
    A simple wrapper that adds behavior
    before and after function execution.
    """

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


# ============================================================
# Part 1 - Manual Wrapping
# ============================================================

print("=== Manual Wrapping ===")


def say_hello():
    """Print a greeting."""
    print("Hello!")


# Manual decoration.
#
# Python:
#     say_hello = wrap(say_hello)
#
# receives the original function,
# creates a new wrapper function,
# and assigns the wrapper back to the name.
say_hello = wrap(say_hello)

say_hello()


# ============================================================
# Part 2 - @ Syntax
# ============================================================

print("\n=== @ Syntax ===")


@wrap
def say_goodbye():
    """Print a farewell message."""
    print("Goodbye!")


say_goodbye()


# ============================================================
# Equivalent Example
# ============================================================

print("\n=== Equivalent Example ===")


def greet_manual():
    print("Manual version")


greet_manual = wrap(greet_manual)


@wrap
def greet_decorated():
    print("Decorated version")


greet_manual()
greet_decorated()


# ============================================================
# Multiple Decorated Functions
# ============================================================

print("\n=== Multiple Decorated Functions ===")


@wrap
def welcome():
    print("Welcome!")


@wrap
def thank_you():
    print("Thank you!")


welcome()
thank_you()


# ============================================================
# Demonstrating What @ Actually Does
# ============================================================

print("\n=== What @ Does Behind The Scenes ===")

print(
    """
This:

    @wrap
    def my_function():
        pass

is equivalent to:

    def my_function():
        pass

    my_function = wrap(my_function)
"""
)