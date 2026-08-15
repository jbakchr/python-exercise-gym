"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 05 - Accessing Attributes

Dataclass fields become object attributes.

After creating a dataclass object, values can be
accessed using dot notation.

This is one of the primary ways dataclasses are used
to model and work with structured data.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


def main():
    person = Person("Alice", 30)

    print(person.name)
    print(person.age)


if __name__ == "__main__":
    main()