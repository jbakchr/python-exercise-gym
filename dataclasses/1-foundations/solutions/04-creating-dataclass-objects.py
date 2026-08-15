"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 04 - Creating Dataclass Objects

A dataclass defines the structure of an object.

Once a dataclass has been defined, multiple objects
can be created from it, each containing its own data.
"""

from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    year: int


def main():
    car_one = Car(
        "Toyota",
        "Corolla",
        2022,
    )

    car_two = Car(
        "Ford",
        "Focus",
        2020,
    )

    print(car_one)
    print(car_two)


if __name__ == "__main__":
    main()