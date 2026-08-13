"""
Exercise 29 - Logging Decorator

Goal:
Build a reusable decorator that records
function activity in a log file.

This solution demonstrates:

- Decorator factories
- Flexible wrappers
- File handling
- Function arguments
- Return values
- Reusable logging behavior
"""


def log_calls(filename):
    """Write function calls to a log file."""

    def decorator(func):

        def wrapper(*args, **kwargs):
            with open(filename, "a") as file:
                file.write(f"{func.__name__} called\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_calls("app.log")
def create_user(username):
    print(f"Creating user: {username}")


@log_calls("app.log")
def generate_report():
    print("Generating report")


@log_calls("app.log")
def delete_file(filename):
    print(f"Deleting file: {filename}")


create_user("jonas")
generate_report()
delete_file("report.txt")

print("\nDone. Check app.log")