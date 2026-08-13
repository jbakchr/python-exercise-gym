"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 20 - Advanced Annotation Patterns

Typing features become more powerful when
combined.

This exercise demonstrates how TypedDict,
Literal, and NewType can work together to
describe structure, valid values, and
domain-specific meaning.
"""

from typing import Literal, NewType, TypedDict


UserId = NewType("UserId", int)


class User(TypedDict):
    id: UserId
    name: str
    status: Literal["active", "inactive"]


def display_user(user: User) -> None:
    print(f"ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Status: {user['status']}")


def main():
    user: User = {
        "id": UserId(1),
        "name": "Alice",
        "status": "active",
    }

    display_user(user)


if __name__ == "__main__":
    main()
