"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 17 - Sorting Dataclass Instances

When order=True is enabled, dataclass
objects can be sorted using Python's
built-in sorting tools.

Sorting uses the same comparison rules
generated for the dataclass and compares
fields in the order they are defined.
"""

from dataclasses import dataclass


@dataclass(order=True)
class Product:
    price: float
    name: str


def main():
    products = [
        Product(25.0, "Keyboard"),
        Product(10.0, "Mouse"),
        Product(100.0, "Monitor"),
    ]

    print("Before sorting:")
    print(products)

    products.sort()

    print("After sorting:")
    print(products)


if __name__ == "__main__":
    main()