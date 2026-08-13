"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 01 - Basic Parameter Types

Function parameters can be annotated with type hints.

Type hints communicate the kinds of values a function
expects to receive.

They improve code readability and serve as the foundation
for all future typing exercises.
"""


def greet(name: str):
    print(f"Hello, {name}")


def double(number: int):
    print(number * 2)


def show_price(price: float):
    print(price)


def show_status(active: bool):
    print(active)


def main():
    greet("Alice")
    double(10)
    show_price(19.99)
    show_status(True)


if __name__ == "__main__":
    main()