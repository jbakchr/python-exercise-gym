"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Generic, TypeVar


"""
Exercise 24 - Generic Container

TypeVar allows a type to be represented
by a placeholder.

Generic classes can then use that
placeholder to work with many different
types while preserving type information.

This makes reusable utilities safer and
more flexible.
"""


T = TypeVar("T")


class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


def main():
    string_container = Container("hello")
    number_container = Container(42)

    print(string_container.get_value())
    print(number_container.get_value())


if __name__ == "__main__":
    main()