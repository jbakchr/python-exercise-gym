"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 37 - Data Validation Pipeline

Applications often need to validate incoming data
before processing it.

A decorator can enforce validation rules consistently
across multiple functions while keeping validation
logic separate from business logic.
"""


def validate_not_empty(func):
    def wrapper(value):
        if value == "":
            print("Validation failed.")
            return

        return func(value)

    return wrapper


@validate_not_empty
def create_user(name):
    print(f"Creating user: {name}")


@validate_not_empty
def update_email(email):
    print(f"Updating email: {email}")


def main():
    create_user("Alice")
    create_user("")

    print()

    update_email("alice@example.com")
    update_email("")


if __name__ == "__main__":
    main()