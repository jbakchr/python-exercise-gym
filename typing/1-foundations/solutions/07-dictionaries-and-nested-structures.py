"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 07 - Dictionaries and Nested Structures

Dictionary type annotations describe the types of keys
and values stored in a dictionary.

Type annotations can also be nested, allowing complex
data structures such as lists of dictionaries to be
described clearly and consistently.
"""


def get_user_age(user: dict[str, int]) -> int:
    return user["age"]


def count_settings(settings: dict[str, str]) -> int:
    return len(settings)


def get_first_user(users: list[dict[str, str]]) -> dict[str, str]:
    return users[0]


def create_server_config(host: str, port: int) -> dict[str, str | int]:
    return {
        "host": host,
        "port": port,
    }


def main():
    user_age = get_user_age({"age": 30})

    settings_count = count_settings(
        {
            "theme": "dark",
            "language": "en",
            "timezone": "UTC",
        }
    )

    first_user = get_first_user(
        [
            {"name": "Alice"},
            {"name": "Bob"},
        ]
    )

    server_config = create_server_config(
        "localhost",
        8000,
    )

    print(user_age)
    print(settings_count)
    print(first_user)
    print(server_config)


if __name__ == "__main__":
    main()