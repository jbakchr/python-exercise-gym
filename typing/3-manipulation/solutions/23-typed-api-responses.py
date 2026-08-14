"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Literal, TypedDict


"""
Exercise 23 - Typed API Responses

TypedDict can be used to model structured
API response data.

Nested TypedDict objects allow complex
response structures to be described clearly.

This makes API integrations easier to
understand and safer to work with.
"""


ApiStatus = Literal[
    "success",
    "error",
]


class UserData(TypedDict):
    id: int
    username: str
    email: str


class ApiResponse(TypedDict):
    status: ApiStatus
    data: UserData


def get_user_email(response: ApiResponse) -> str:
    return response["data"]["email"]


def main():
    response: ApiResponse = {
        "status": "success",
        "data": {
            "id": 1,
            "username": "alice",
            "email": "alice@example.com",
        },
    }

    print(get_user_email(response))


if __name__ == "__main__":
    main()