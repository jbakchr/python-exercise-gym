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
Exercise 35 - Generic Repository Pattern

Generics allow a single class to work with multiple
types while preserving type information.

This makes it possible to build reusable components
without sacrificing type safety.
"""

T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get(self, index: int) -> T:
        return self.items[index]


def main():
    user_repository = Repository[str]()
    user_repository.add("Alice")

    product_repository = Repository[str]()
    product_repository.add("Laptop")

    user = user_repository.get(0)
    product = product_repository.get(0)

    print(user)
    print(product)


if __name__ == "__main__":
    main()