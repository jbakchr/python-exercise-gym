"""
Solution Guidelines
- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import TypedDict


"""
Exercise 34 - Typed Validation System

Typed validation functions can make application code
safer and easier to understand.

Clearly defined input and output types help communicate
what data is expected and what data is considered valid.
"""


class User(TypedDict):
    name: str
    email: str


def is_valid_user(user: User) -> bool:
    return bool(user["name"]) and "@" in user["email"]


def main():
    user: User = {
        "name": "Alice",
        "email": "alice@example.com",
    }

    print(is_valid_user(user))


if __name__ == "__main__":
    main()