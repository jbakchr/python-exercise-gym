"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import TypeVar


"""
Exercise 26 - Type Utility Functions

TypeVar allows a function to work with
multiple data types while preserving
type information.

Generic utility functions are a common
way to build reusable tools that remain
type-safe.
"""


T = TypeVar("T")


def identity(value: T) -> T:
    return value


def main():
    print(identity("hello"))
    print(identity(42))


if __name__ == "__main__":
    main()