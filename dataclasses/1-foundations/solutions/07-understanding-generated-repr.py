"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 07 - Understanding Generated __repr__

Dataclasses automatically generate a __repr__()
method.

When a dataclass object is printed, Python uses
this generated representation to display the
object's fields and values in a readable format.
"""

from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    director: str
    year: int


def main():
    movie = Movie(
        "Inception",
        "Christopher Nolan",
        2010,
    )

    print(movie)


if __name__ == "__main__":
    main()