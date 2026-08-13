"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 10 - Build a Typed Utility

This exercise combines the typing concepts learned
throughout the Foundations stage.

The utility uses type aliases, collections, Optional
values, parameter annotations, and return annotations
to create a small typed user directory.
"""

from typing import Optional


UserName = str
UserRecord = dict[str, str]
UserList = list[UserRecord]


def create_user(name: UserName, email: str) -> UserRecord:
    return {
        "name": name,
        "email": email,
    }


def find_user(users: UserList, name: UserName) -> Optional[UserRecord]:
    for user in users:
        if user["name"] == name:
            return user

    return None


def count_users(users: UserList) -> int:
    return len(users)


def get_user_names(users: UserList) -> list[UserName]:
    names = []

    for user in users:
        names.append(user["name"])

    return names


def main():
    users = [
        create_user("Alice", "alice@example.com"),
        create_user("Bob", "bob@example.com"),
        create_user("Charlie", "charlie@example.com"),
    ]

    found_user = find_user(users, "Bob")
    user_count = count_users(users)
    user_names = get_user_names(users)

    print(users[0])
    print(user_count)
    print(user_names)
    print(found_user)


if __name__ == "__main__":
    main()