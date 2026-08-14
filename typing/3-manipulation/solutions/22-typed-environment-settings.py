"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Literal, NotRequired, TypedDict


"""
Exercise 22 - Typed Environment Settings

TypedDict can be used to model structured
configuration data.

Literal restricts values to a known set
of valid options.

Optional configuration fields make it
possible to represent settings that may
only exist in certain environments.
"""


Environment = Literal[
    "development",
    "testing",
    "production",
]


class EnvironmentSettings(TypedDict):
    environment: Environment
    debug: bool
    database_url: str
    monitoring_url: NotRequired[str]


def is_debug_enabled(settings: EnvironmentSettings) -> bool:
    return settings["debug"]


def main():
    development_settings: EnvironmentSettings = {
        "environment": "development",
        "debug": True,
        "database_url": "sqlite:///dev.db",
    }

    print(is_debug_enabled(development_settings))


if __name__ == "__main__":
    main()