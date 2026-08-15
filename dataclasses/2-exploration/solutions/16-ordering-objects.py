"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 16 - Ordering Objects

Dataclasses can automatically generate
comparison methods when order=True is used.

Objects are compared using the fields
defined in the dataclass, in the order
those fields appear in the class definition.
"""

from dataclasses import dataclass


@dataclass(order=True)
class Product:
    price: float
    name: str


def main():
    product1 = Product(
        price=10.0,
        name="Mouse",
    )

    product2 = Product(
        price=20.0,
        name="Keyboard",
    )

    print(product1 < product2)
    print(product1 > product2)


if __name__ == "__main__":
    main()