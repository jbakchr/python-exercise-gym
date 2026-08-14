"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Literal, TypedDict


"""
Exercise 21 - Typed Configuration Data

TypedDict allows us to describe the expected
structure of dictionary-based data.

Literal allows us to restrict values to a
specific set of allowed options.

Together they help create safer and more
self-documenting configuration models.
"""


Environment = Literal[
    "development",
    "testing",
    "production",
]


class AppConfig(TypedDict):
    name: str
    environment: Environment
    debug: bool
    database_url: str


def get_database_url(config: AppConfig) -> str:
    return config["database_url"]


def main():
    config: AppConfig = {
        "name": "My App",
        "environment": "development",
        "debug": True,
        "database_url": "sqlite:///app.db",
    }

    print(get_database_url(config))


if __name__ == "__main__":
    main()