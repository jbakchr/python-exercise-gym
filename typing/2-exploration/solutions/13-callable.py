"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 13 - Callable

Callable allows type annotations to describe
functions that can be passed as arguments.

A Callable annotation specifies both the
expected parameter types and the return type
of a function.
"""

from typing import Callable


def greet(name: str) -> str:
    return f"Hello, {name}"


def run_function(
    func: Callable[[str], str],
    name: str
) -> None:
    result = func(name)
    print(result)


def main():
    run_function(greet, "Alice")


if __name__ == "__main__":
    main()