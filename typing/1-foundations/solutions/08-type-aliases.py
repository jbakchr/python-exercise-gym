"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 08 - Type Aliases

Type aliases allow complex type annotations to be
given meaningful names.

They improve readability, reduce repetition, and help
communicate intent throughout a codebase.
"""

UserName = str
UserRecord = dict[str, str]
UserList = list[dict[str, str]]


def create_username(name: UserName) -> UserName:
    return name


def create_user(name: UserName) -> UserRecord:
    return {"name": name}


def get_first_user(users: UserList) -> UserRecord:
    return users[0]


def count_users(users: UserList) -> int:
    return len(users)


def main():
    username = create_username("Alice")

    user = create_user(username)

    users = [
        {"name": "Alice"},
        {"name": "Bob"},
    ]

    first_user = get_first_user(users)
    user_count = count_users(users)

    print(username)
    print(user)
    print(first_user)
    print(user_count)


if __name__ == "__main__":
    main()