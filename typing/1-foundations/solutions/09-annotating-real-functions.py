"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 09 - Annotating Real Functions

Real-world functions often combine multiple typing
concepts such as type aliases, collections, Optional
values, and return annotations.

These annotations make function signatures easier to
understand and help communicate developer intent.
"""

from typing import Optional


UserName = str
UserRecord = dict[str, str]
UserList = list[UserRecord]


def create_user(name: UserName) -> UserRecord:
    return {"name": name}


def find_user(users: UserList, name: UserName) -> Optional[UserRecord]:
    for user in users:
        if user["name"] == name:
            return user

    return None


def count_users(users: UserList) -> int:
    return len(users)


def get_user_names(users: UserList) -> list[str]:
    names = []

    for user in users:
        names.append(user["name"])

    return names


def main():
    users = [
        create_user("Alice"),
        create_user("Bob"),
        create_user("Charlie"),
    ]

    found_user = find_user(users, "Bob")
    user_count = count_users(users)
    usernames = get_user_names(users)

    print(users[0])
    print(found_user)
    print(user_count)
    print(usernames)


if __name__ == "__main__":
    main()