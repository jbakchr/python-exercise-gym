"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 11 - Default Values Revisited

Dataclass fields can have default values.

When an object is created, Python uses the default
value only if no value is provided for that field.

If a value is supplied during object creation,
the supplied value overrides the default.
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    role: str = "member"
    active: bool = True


def main():
    user1 = User("alice")
    user2 = User("bob", "admin")
    user3 = User("charlie", "moderator", False)

    print(user1)
    print(user2)
    print(user3)


if __name__ == "__main__":
    main()