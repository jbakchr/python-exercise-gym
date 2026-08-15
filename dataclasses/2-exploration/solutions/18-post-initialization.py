"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 18 - Post Initialization

The __post_init__ method runs automatically
after the dataclass-generated __init__
method finishes.

It can be used to adjust, normalize, or
prepare field values immediately after
object creation.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str

    def __post_init__(self):
        self.username = self.username.strip().lower()


def main():
    user = User("  Alice  ")

    print(user)


if __name__ == "__main__":
    main()