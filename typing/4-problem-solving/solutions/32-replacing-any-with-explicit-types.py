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
Exercise 32 - Replacing Any with Explicit Types

Using Any hides important information about the
data being passed through an application.

Replacing Any with explicit types makes code easier
to understand, maintain, and validate.
"""


class User(TypedDict):
    name: str
    email: str


def get_user_display(data: User) -> str:
    name = data["name"]
    email = data["email"]

    return f"{name} ({email})"


def main():
    user: User = {
        "name": "Alice",
        "email": "alice@example.com",
    }

    print(get_user_display(user))


if __name__ == "__main__":
    main()