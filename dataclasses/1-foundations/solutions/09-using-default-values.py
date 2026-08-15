"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 09 - Using Default Values

Dataclass fields can be given default values.

When a value is not provided during object
creation, the dataclass automatically uses
the field's default value.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    active: bool = True


def main():
    user = User("alice")

    print(user)


if __name__ == "__main__":
    main()