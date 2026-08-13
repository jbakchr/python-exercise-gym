"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 19 - Self

Self represents the current class type.

It is useful when methods return the current
object, allowing type annotations to describe
that relationship clearly and accurately.
"""

from typing import Self


class User:
    def __init__(self, name: str):
        self.name = name

    def update_name(self, name: str) -> Self:
        self.name = name
        return self


def main():
    user = User("Alice")

    user.update_name("Bob")

    print(user.name)


if __name__ == "__main__":
    main()