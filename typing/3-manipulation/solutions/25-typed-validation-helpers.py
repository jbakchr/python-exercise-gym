"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Callable


"""
Exercise 25 - Typed Validation Helpers

Callable can be used to describe the
expected signature of a function.

This allows validation helpers to work
with different validation functions while
remaining type-safe and reusable.

The validation helper does not need to
know how validation works. It simply
executes the validator provided to it.
"""


Validator = Callable[[str], bool]


def is_not_empty(value: str) -> bool:
    return len(value) > 0


def validate(value: str, validator: Validator) -> bool:
    return validator(value)


def main():
    print(validate("alice", is_not_empty))


if __name__ == "__main__":
    main()