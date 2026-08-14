"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Protocol


"""
Exercise 28 - Service Interface Design

Protocols define a contract that
describes expected behavior.

Classes that provide the required
methods satisfy the protocol and can
be used interchangeably.

This allows applications to depend on
interfaces rather than implementations.
"""


class UserService(Protocol):
    def get_username(self) -> str:
        ...


class DatabaseUserService:
    def get_username(self) -> str:
        return "alice"


def display_username(service: UserService) -> None:
    print(service.get_username())


def main():
    service = DatabaseUserService()
    display_username(service)


if __name__ == "__main__":
    main()