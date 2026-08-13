"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 38 - Secure Operations

Some application features should only be available
to users with the appropriate permissions.

A decorator can enforce authorization rules
consistently while keeping security checks
separate from business logic.
"""


def requires_role(required_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print("Access denied.")
                return

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


@requires_role("admin")
def delete_user(user_role):
    print("Deleting user...")


@requires_role("manager")
def reset_password(user_role):
    print("Resetting password...")


def main():
    delete_user("admin")
    delete_user("guest")

    print()

    reset_password("manager")
    reset_password("guest")


if __name__ == "__main__":
    main()