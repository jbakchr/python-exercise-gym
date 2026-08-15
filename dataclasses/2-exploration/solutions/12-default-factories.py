"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 12 - Default Factories

Dataclasses use default_factory when a field
needs a new object for every instance.

This is commonly used for mutable values
such as lists, dictionaries, and sets.

Each dataclass object receives its own
separate value created by the factory.
"""

from dataclasses import dataclass, field


@dataclass
class ShoppingCart:
    items: list[str] = field(default_factory=list)


def main():
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()

    cart1.items.append("Laptop")

    print(cart1)
    print(cart2)


if __name__ == "__main__":
    main()