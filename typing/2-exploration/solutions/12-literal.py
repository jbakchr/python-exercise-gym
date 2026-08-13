"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 12 - Literal

Literal allows a type annotation to restrict values
to a specific set of allowed choices.

This makes code easier to understand and helps
communicate valid options to developers and
type-checking tools.
"""

from typing import Literal


def display_status(
    status: Literal["pending", "approved", "rejected"]
) -> None:
    print(f"Status: {status}")


def main():
    display_status("pending")


if __name__ == "__main__":
    main()