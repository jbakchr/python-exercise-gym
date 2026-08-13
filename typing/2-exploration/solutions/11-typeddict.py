"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 11 - TypedDict

TypedDict allows dictionaries to have a defined structure.

It helps describe which keys are expected and what
types of values those keys should contain.

TypedDict improves readability and communicates
the intended shape of dictionary data.
"""

from typing import TypedDict


class User(TypedDict):
    name: str
    age: int
    email: str


def display_user(user: User) -> None:
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Email: {user['email']}")


def main():
    user: User = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
    }

    display_user(user)


if __name__ == "__main__":
    main()