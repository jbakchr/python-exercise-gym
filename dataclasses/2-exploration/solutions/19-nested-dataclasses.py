"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 19 - Nested Dataclasses

Dataclasses can contain other dataclass
objects as fields.

This allows larger data models to be built
from smaller, reusable components while
keeping related information organized.
"""

from dataclasses import dataclass


@dataclass
class Address:
    city: str
    country: str


@dataclass
class User:
    username: str
    address: Address


def main():
    address = Address(
        city="Copenhagen",
        country="Denmark",
    )

    user = User(
        username="alice",
        address=address,
    )

    print(user)
    print(user.address.city)


if __name__ == "__main__":
    main()