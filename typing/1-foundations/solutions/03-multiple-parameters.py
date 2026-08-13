"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 03 - Multiple Parameters

Functions often require more than one piece of
information to perform their work.

Each parameter can have its own type annotation,
allowing the function signature to clearly describe
what inputs are expected and what output is returned.
"""


def create_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


def calculate_area(width: float, height: float) -> float:
    return width * height


def create_login_message(username: str, login_count: int) -> str:
    return f"{username} has logged in {login_count} times."


def can_purchase(age: int, has_permission: bool) -> bool:
    return age >= 18 and has_permission


def main():
    full_name = create_full_name("Alice", "Smith")
    area = calculate_area(3.0, 4.0)
    login_message = create_login_message("alice", 5)
    purchase_allowed = can_purchase(21, True)

    print(full_name)
    print(area)
    print(login_message)
    print(purchase_allowed)


if __name__ == "__main__":
    main()