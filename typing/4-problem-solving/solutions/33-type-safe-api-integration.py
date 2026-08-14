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
Exercise 33 - Type-Safe API Integration

External API responses are often represented as
dictionaries.

Using TypedDict allows developers to clearly define
the expected structure of API data and create safer
interfaces between applications and external services.
"""


class UserResponse(TypedDict):
    id: int
    name: str
    email: str
    active: bool


def fetch_user() -> UserResponse:
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "active": True,
    }


def main():
    user = fetch_user()

    print(user["name"])
    print(user["email"])


if __name__ == "__main__":
    main()