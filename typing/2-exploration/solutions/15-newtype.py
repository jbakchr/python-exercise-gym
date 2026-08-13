"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 15 - NewType

NewType allows a type to be given a new,
more meaningful identity while retaining
the behavior of its underlying type.

This helps communicate intent and makes
it easier to distinguish values that
represent different concepts.
"""

from typing import NewType


UserId = NewType("UserId", int)


def display_user(user_id: UserId) -> None:
    print(f"User ID: {user_id}")


def main():
    user_id = UserId(123)

    display_user(user_id)


if __name__ == "__main__":
    main()