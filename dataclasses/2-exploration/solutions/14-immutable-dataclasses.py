"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 14 - Immutable Dataclasses

A dataclass can be made immutable by using
frozen=True.

After an object is created, its fields cannot
be reassigned.

This helps protect important data from
accidental modification.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Configuration:
    environment: str
    debug: bool


def main():
    config = Configuration(
        environment="production",
        debug=False,
    )

    print(config)

    config.debug = True


if __name__ == "__main__":
    main()