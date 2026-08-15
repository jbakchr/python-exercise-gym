"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 01 - Creating Your First Dataclass

A dataclass is a simple way to create classes whose
main purpose is storing data.

The @dataclass decorator automatically generates
useful methods such as __init__(), allowing us to
focus on modelling data rather than writing
boilerplate code.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str


def main():
    person = Person("Alice")
    print(person)


if __name__ == "__main__":
    main()