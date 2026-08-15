"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 13 - Optional Fields

Optional fields allow a dataclass attribute
to contain either a value or None.

This is useful when information may not be
available when an object is created.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    email: Optional[str] = None


def main():
    user1 = User("alice")
    user2 = User("bob", "bob@example.com")

    print(user1)
    print(user2)


if __name__ == "__main__":
    main()