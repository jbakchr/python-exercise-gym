"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 17 - Type Inference

Type inference allows type checkers to determine
types automatically based on assigned values.

Explicit annotations are not always necessary
when the intended type is already obvious from
the code.
"""


def main():
    name = "Alice"
    age = 30
    is_active = True

    users = ["Alice", "Bob", "Charlie"]

    print(name)
    print(age)
    print(is_active)
    print(users)


if __name__ == "__main__":
    main()