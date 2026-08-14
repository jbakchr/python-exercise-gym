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
Exercise 38 - Service Layer Refactoring

Protocols allow services to depend on contracts
instead of concrete implementations.

This reduces coupling and makes applications
easier to maintain, test, and extend.
"""


class UserRepository(Protocol):
    def add(self, name: str) -> None:
        ...

    def get(self, index: int) -> str:
        ...


class InMemoryUserRepository:
    def __init__(self) -> None:
        self.users: list[str] = []

    def add(self, name: str) -> None:
        self.users.append(name)

    def get(self, index: int) -> str:
        return self.users[index]


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, name: str) -> None:
        self.repository.add(name)

    def get_user(self, index: int) -> str:
        return self.repository.get(index)


def main():
    repository = InMemoryUserRepository()

    service = UserService(repository)

    service.create_user("Alice")

    user = service.get_user(0)

    print(user)


if __name__ == "__main__":
    main()