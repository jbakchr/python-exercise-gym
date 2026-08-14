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
Exercise 29 - Data Transformation Pipeline

Multiple processing functions can be
combined into a pipeline.

Each processor performs a single
transformation step.

TypeVar and Callable allow the pipeline
to remain reusable while preserving
type information.
"""


T = TypeVar("T")

Processor = Callable[[T], T]


def strip_whitespace(value: str) -> str:
    return value.strip()


def to_uppercase(value: str) -> str:
    return value.upper()


def run_pipeline(
    value: T,
    processors: list[Processor[T]],
) -> T:
    for processor in processors:
        value = processor(value)

    return value


def main():
    result = run_pipeline(
        "  alice  ",
        [
            strip_whitespace,
            to_uppercase,
        ],
    )

    print(result)


if __name__ == "__main__":
    main()