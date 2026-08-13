"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 05 - Union Types

Union allows a value to be one of several valid types.

This is useful when a function intentionally supports
multiple kinds of input while still clearly describing
its expected contract.
"""

from typing import Union


def format_user(identifier: Union[int, str]) -> str:
    return f"User: {identifier}"


def calculate_tax(amount: Union[int, float]) -> float:
    return amount * 1.20


def create_label(value: Union[int, str]) -> str:
    return f"Value: {value}"


def get_discount(customer_type: Union[str, int]) -> str:
    return "Standard Discount"


def main():
    user = format_user("alice")
    taxed_amount = calculate_tax(100)
    label = create_label(42)
    discount = get_discount("standard")

    print(user)
    print(taxed_amount)
    print(label)
    print(discount)


if __name__ == "__main__":
    main()