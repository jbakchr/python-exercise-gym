"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 03 - Using Type Annotations

Dataclass fields use type annotations to describe the
kind of data each field is expected to store.

Type annotations help make data models easier to
understand and work naturally alongside dataclasses.
"""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int


def main():
    book = Book(
        "Python Basics",
        "Jane Smith",
        250,
    )

    print(book)


if __name__ == "__main__":
    main()