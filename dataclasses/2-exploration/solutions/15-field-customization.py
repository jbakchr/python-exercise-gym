"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 15 - Field Customization

The field() function allows individual
dataclass fields to be customized.

One common use is repr=False, which keeps
a field out of the automatically generated
string representation while still storing
the value on the object.
"""

from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str = field(repr=False)


def main():
    user = User(
        username="alice",
        password="secret123",
    )

    print(user)


if __name__ == "__main__":
    main()