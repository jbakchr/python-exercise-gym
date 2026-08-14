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
Exercise 31 - Refactoring Untyped Configuration

Untyped configuration dictionaries can make applications
harder to understand and maintain.

Using TypedDict and other typing constructs helps define
the expected structure of configuration data and makes
errors easier to detect.
"""


class AppConfig(TypedDict):
    host: str
    port: int
    debug: bool
    environment: Literal["development", "testing", "production"]


def load_config() -> AppConfig:
    return {
        "host": "localhost",
        "port": 8080,
        "debug": True,
        "environment": "development",
    }


def main():
    config = load_config()

    print(f"Host: {config['host']}")
    print(f"Port: {config['port']}")
    print(f"Environment: {config['environment']}")


if __name__ == "__main__":
    main()