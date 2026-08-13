"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 16 - NamedTuple

NamedTuple provides a way to create lightweight,
immutable data structures with named fields.

It combines the simplicity of tuples with the
readability of attribute access.
"""

from typing import NamedTuple


class User(NamedTuple):
    name: str
    age: int
    email: str


def main():
    user = User(
        "Alice",
        30,
        "alice@example.com",
    )

    print(f"Name: {user.name}")
    print(f"Age: {user.age}")
    print(f"Email: {user.email}")


if __name__ == "__main__":
    main()