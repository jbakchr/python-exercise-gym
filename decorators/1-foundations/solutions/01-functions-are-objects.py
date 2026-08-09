"""
Exercise 01 - Functions Are Objects

The goal of this exercise is to understand that functions
can be treated like other objects in Python.

They can be:

- Assigned to variables
- Passed around
- Called through different references
"""


def say_hello():
    """Print a greeting."""
    print("Hello!")


# Assign the function object to another variable.
#
# Notice:
# We DO NOT use parentheses here.
#
# Correct:
#     greet = say_hello
#
# Incorrect:
#     greet = say_hello()
#
# Using parentheses would execute the function immediately.
greet = say_hello


# Call the function using the new variable.
greet()


# ------------------------------------------------------------------
# Additional experiments
# ------------------------------------------------------------------

hello_again = say_hello

print("\nCalling through another variable:")
hello_again()

print("\nDo both variables reference the same function?")
print(greet is say_hello)

print("\nFunction object:")
print(say_hello)