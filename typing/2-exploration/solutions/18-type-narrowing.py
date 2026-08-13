"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 18 - Type Narrowing

Type narrowing occurs when Python can determine
that a value has become more specific than its
original annotation.

Checks such as isinstance() allow type checkers
to narrow a broader type into a more precise type
within a particular branch of code.
"""


def process(value: str | int) -> None:
    if isinstance(value, str):
        print(f"String value: {value}")
    else:
        print(f"Integer value: {value}")


def main():
    process("hello")
    process(42)


if __name__ == "__main__":
    main()