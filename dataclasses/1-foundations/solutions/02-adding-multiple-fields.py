"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 02 - Adding Multiple Fields

A dataclass can contain multiple fields.

This allows related pieces of information to be grouped
together into a single object, making data easier to
organize and work with.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str


def main():
    person = Person(
        "Alice",
        30,
        "alice@example.com",
    )

    print(person)


if __name__ == "__main__":
    main()