"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 06 - Lists and Collections

Collection type annotations describe both the type of
collection and the types of values stored inside it.

This helps communicate what data a function expects
and what data it returns.
"""


def count_names(names: list[str]) -> int:
    return len(names)


def get_first_score(scores: list[int]) -> int:
    return scores[0]


def count_permissions(permissions: set[str]) -> int:
    return len(permissions)


def create_coordinate(x: int, y: int) -> tuple[int, int]:
    return (x, y)


def main():
    total_names = count_names(["Alice", "Bob", "Charlie"])
    first_score = get_first_score([95, 88, 76])
    permission_count = count_permissions({"read", "write"})
    coordinate = create_coordinate(10, 20)

    print(total_names)
    print(first_score)
    print(permission_count)
    print(coordinate)


if __name__ == "__main__":
    main()