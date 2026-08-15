"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 08 - Comparing Dataclass Objects

Dataclasses automatically generate an __eq__()
method.

This allows two dataclass objects to be compared
using ==. If all field values are equal, the
objects are considered equal.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str


def main():
    user_one = User(
        "alice",
        "alice@example.com",
    )

    user_two = User(
        "alice",
        "alice@example.com",
    )

    print(user_one == user_two)


if __name__ == "__main__":
    main()