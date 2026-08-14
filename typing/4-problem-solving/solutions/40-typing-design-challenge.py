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
Exercise 40 - Typing Design Challenge

Typing can be used to model data, define contracts,
and create clear boundaries between application
components.

Combining multiple typing techniques helps create
maintainable and understandable software systems.
"""


class AppConfig(TypedDict):
    environment: str


class Repository(Protocol):
    def get_message(self) -> str:
        ...


class InMemoryRepository:
    def get_message(self) -> str:
        return "Hello from the repository"


class ApplicationService:
    def __init__(
        self,
        repository: Repository,
        config: AppConfig,
    ) -> None:
        self.repository = repository
        self.config = config

    def run(self) -> str:
        return self.repository.get_message()


def load_config() -> AppConfig:
    return {
        "environment": "development",
    }


def main():
    config = load_config()

    repository = InMemoryRepository()

    service = ApplicationService(
        repository=repository,
        config=config,
    )

    result = service.run()

    print(result)


if __name__ == "__main__":
    main()