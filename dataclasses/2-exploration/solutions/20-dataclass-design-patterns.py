"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 20 - Dataclass Design Patterns

Multiple dataclass features can be combined
to model realistic application data.

This example combines nested dataclasses,
optional fields, default factories, and
post-initialization processing into a
single reusable model.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    city: str
    country: str


@dataclass
class UserProfile:
    username: str
    address: Address
    email: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.username = self.username.strip().lower()


def main():
    address = Address(
        city="Copenhagen",
        country="Denmark",
    )

    user = UserProfile(
        username="  Alice  ",
        address=address,
    )

    print(user)


if __name__ == "__main__":
    main()