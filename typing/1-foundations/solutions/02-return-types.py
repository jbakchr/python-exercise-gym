"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 02 - Return Types

Return type annotations describe the kind of value a
function gives back to its caller.

Together, parameter annotations and return annotations
form a clear contract for how a function should be used.
"""


def greet(name: str) -> str:
    return f"Hello, {name}"


def double(number: int) -> int:
    return number * 2


def apply_discount(price: float) -> float:
    return price * 0.9


def is_adult(age: int) -> bool:
    return age >= 18


def main():
    greeting = greet("Alice")
    doubled = double(10)
    discounted_price = apply_discount(20.0)
    adult_status = is_adult(21)

    print(greeting)
    print(doubled)
    print(discounted_price)
    print(adult_status)


if __name__ == "__main__":
    main()