"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 10 - Building a Simple Data Model

Dataclasses are designed to model structured,
real-world data.

By combining fields, type annotations, generated
methods, and default values, dataclasses provide
a clean way to represent application objects.
"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    stock_quantity: int
    in_stock: bool = True


def main():
    product = Product(
        "Laptop",
        999.99,
        15,
    )

    print(product)
    print(product.name)
    print(product.price)


if __name__ == "__main__":
    main()