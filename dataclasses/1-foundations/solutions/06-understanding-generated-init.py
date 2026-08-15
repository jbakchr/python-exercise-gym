"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 06 - Understanding Generated __init__

Dataclasses automatically generate an __init__()
method based on the fields defined in the class.

This allows objects to be created without manually
writing a constructor.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str


def main():
    user = User(
        "alice",
        "alice@example.com",
    )

    print(user.username)
    print(user.email)


if __name__ == "__main__":
    main()