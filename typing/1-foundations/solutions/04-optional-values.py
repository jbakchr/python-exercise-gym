"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 04 - Optional Values

Sometimes a value may be available and sometimes it
may be missing.

Optional allows us to clearly communicate that a
function may return either a value of a specific type
or None.
"""

from typing import Optional


def get_middle_name(use_middle_name: bool) -> Optional[str]:
    if use_middle_name:
        return "Marie"

    return None


def get_discount_code(has_discount: bool) -> Optional[str]:
    if has_discount:
        return "SAVE10"

    return None


def get_manager(has_manager: bool) -> Optional[str]:
    if has_manager:
        return "Sarah"

    return None


def main():
    middle_name = get_middle_name(True)
    discount_code = get_discount_code(False)
    manager = get_manager(True)

    print(middle_name)
    print(discount_code)
    print(manager)


if __name__ == "__main__":
    main()