"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Callable, TypeVar


"""
Exercise 27 - Typed Data Processor

Callable can be combined with TypeVar
to create reusable processing utilities.

The processor function defines how a
value should be transformed, while the
processing utility handles execution.

This pattern allows transformations to
remain reusable and type-safe.
"""


T = TypeVar("T")

Processor = Callable[[T], T]


def to_uppercase(value: str) -> str:
    return value.upper()


def process(value: T, processor: Processor[T]) -> T:
    return processor(value)


def main():
    print(process("alice", to_uppercase))


if __name__ == "__main__":
    main()