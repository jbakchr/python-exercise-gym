"""
Solution Guidelines
- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Protocol, TypedDict


"""
Exercise 39 - Designing a Type-Safe Architecture

Typing can be used to define clear contracts
between application layers.

Typed configuration, repositories, and services
help create maintainable and understandable
software architectures.
"""


class AppConfig(TypedDict):
    environment: str


class UserRepository(Protocol):
    def add(self, name: str) -> None:
        ...

    def get(self, index: int) -> str:
        ...


class InMemoryRepository:
    def __init__(self) -> None:
        self.users: list[str] = []

    def add(self, name: str) -> None:
        self.users.append(name)

    def get(self, index: int) -> str:
        return self.users[index]


class UserService:
    def __init__(
        self,
        repository: UserRepository,
        config: AppConfig,
    ) -> None:
        self.repository = repository
        self.config = config

    def create_user(self, name: str) -> None:
        self.repository.add(name)

    def get_user(self, index: int) -> str:
        return self.repository.get(index)


def load_config() -> AppConfig:
    return {
        "environment": "development",
    }


def main():
    config = load_config()

    repository = InMemoryRepository()

    service = UserService(
        repository=repository,
        config=config,
    )

    service.create_user("Alice")

    user = service.get_user(0)

    print(user)


if __name__ == "__main__":
    main()