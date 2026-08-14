"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 30 - Build a Typing Toolbox

This exercise combines several typing concepts into a
small collection of reusable utilities.

The goal is to model structured data, create typed
functions, use generics, and define simple service
interfaces.
"""

from typing import Generic
from typing import Literal
from typing import TypeAlias
from typing import TypeVar
from typing import TypedDict


Environment: TypeAlias = Literal["dev", "test", "prod"]


class Config(TypedDict):
    app_name: str
    environment: Environment
    debug: bool


def is_valid_port(port: int) -> bool:
    return 1 <= port <= 65535


class User(TypedDict):
    id: int
    name: str


class UserSummary(TypedDict):
    id: int
    name: str


def summarize_user(user: User) -> UserSummary:
    return {
        "id": user["id"],
        "name": user["name"],
    }


T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


class UserService:
    def get_user(self, user_id: int) -> User:
        return {
            "id": user_id,
            "name": "Alice",
        }


def main() -> None:
    config: Config = {
        "app_name": "Typing Toolbox",
        "environment": "dev",
        "debug": True,
    }

    print(config)

    print(is_valid_port(8080))

    service = UserService()

    user = service.get_user(1)

    print(user)
    print(summarize_user(user))

    box = Box(42)

    print(box.get())


if __name__ == "__main__":
    main()