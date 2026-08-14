"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Mini Project - Type-Safe Configuration Framework

Typing can be used to model application
configuration explicitly and safely.

By defining configuration structures with
TypedDict, Literal, and Optional fields,
developers can discover requirements through
type hints and reduce configuration errors.
"""

from typing import Literal, NotRequired, TypedDict


class DatabaseConfig(TypedDict):
    host: str
    port: int


class AppConfig(TypedDict):
    environment: Literal["development", "testing", "production"]
    debug: bool
    database: DatabaseConfig
    log_level: NotRequired[str]


def validate_configuration(config: AppConfig) -> bool:
    if config["database"]["port"] <= 0:
        return False

    return True


def display_configuration(config: AppConfig) -> None:
    print(f"Environment: {config['environment']}")
    print(f"Debug: {config['debug']}")
    print(
        f"Database: "
        f"{config['database']['host']}:"
        f"{config['database']['port']}"
    )

    if "log_level" in config:
        print(f"Log Level: {config['log_level']}")


def main() -> None:
    config: AppConfig = {
        "environment": "production",
        "debug": False,
        "database": {
            "host": "db.company.com",
            "port": 5432,
        },
        "log_level": "INFO",
    }

    if validate_configuration(config):
        display_configuration(config)
    else:
        print("Invalid configuration")


if __name__ == "__main__":
    main()