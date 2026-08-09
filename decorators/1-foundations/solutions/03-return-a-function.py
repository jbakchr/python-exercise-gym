"""
Exercise 03 - Return a Function

The goal of this exercise is to understand that functions
can return other functions.

This is another important building block behind decorators.

A decorator eventually returns a new function (often called
a wrapper), so understanding this concept first makes
decorators much easier to understand later.
"""


def create_greeter():
    """
    Create and return a greeting function.
    """

    def greet():
        """Print a greeting."""
        print("Hello!")

    # Return the function object itself.
    #
    # Notice:
    # We use:
    #     return greet
    #
    # NOT:
    #     return greet()
    #
    # Returning greet() would execute the function immediately
    # and return its result instead of returning the function.
    return greet


# Call create_greeter().
#
# This returns the nested greet() function.
my_greeter = create_greeter()


# Execute the returned function.
my_greeter()


# ------------------------------------------------------------------
# Additional experiments
# ------------------------------------------------------------------

print("\nCalling the returned function again:")
my_greeter()


def create_farewell():
    """
    Create and return a farewell function.
    """

    def goodbye():
        print("Goodbye!")

    return goodbye


farewell = create_farewell()

print("\nCalling a different returned function:")
farewell()


print("\nInspecting returned function objects:")
print(my_greeter)
print(farewell)