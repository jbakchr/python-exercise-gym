"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 14 - Any

Any allows a value to be treated as having
no specific type.

It can be useful when type information is
unknown or intentionally flexible, but it
also removes many of the benefits provided
by more precise type annotations.
"""

from typing import Any


def display_value(value: Any) -> None:
    print(value)


def main():
    display_value("hello")
    display_value(42)
    display_value(3.14)
    display_value(["a", "b", "c"])
    display_value({"name": "Alice"})


if __name__ == "__main__":
    main()