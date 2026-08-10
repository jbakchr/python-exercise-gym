"""
Exercise 01 - Functions Are Objects

Functions in Python are first-class objects.

This means they can be assigned to variables,
passed around, and called through different references.
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


# Assign the function to a new variable.
greet = say_hello

# Call the function through the new variable.
greet()