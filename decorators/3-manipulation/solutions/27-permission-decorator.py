"""
Exercise 27 - Permission Decorator

Goal:
Build a reusable decorator that controls access
to protected functions.

This solution demonstrates:

- Decorators
- Flexible wrappers
- Conditional execution
- Access control
- Return values
"""


current_user_is_admin = False


def requires_admin(func):
    """Allow execution only for administrators."""

    def wrapper(*args, **kwargs):
        if current_user_is_admin:
            print("Access Granted")

            return func(*args, **kwargs)

        print("Access Denied")

    return wrapper

@requires_admin
def delete_user(username):
    print(f"Deleting {username}")


@requires_admin
def view_audit_log():
    print("Viewing audit log")


print("=== Non-Admin User ===")

delete_user("alice")
print()

view_audit_log()
print()


print("=== Admin User ===")

current_user_is_admin = True

delete_user("alice")
print()

view_audit_log()
