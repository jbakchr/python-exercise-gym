"""
Exercise 23 - Retry Decorator

Goal:
Build a reusable decorator that automatically retries
failed operations.

This solution demonstrates:

- Decorator factories
- Exception handling
- Retry logic
- Loops
- Reusable behavior
"""


def retry(max_attempts):
    """Retry a function when an exception occurs."""

    def decorator(func):

        def wrapper():
            for attempt in range(1, max_attempts + 1):
                try:
                    return func()

                except Exception as error:
                    print(f"Attempt {attempt} failed: {error}")

                    if attempt == max_attempts:
                        print("No retries remaining.")
                        raise

                    print("Retrying...")

        return wrapper

    return decorator


# Used to simulate temporary failures.
attempt_counter = 0


@retry(3)
def unstable_operation():
    """Fail twice before succeeding."""

    global attempt_counter

    attempt_counter += 1

    if attempt_counter < 3:
        raise ValueError("Temporary failure")

    return "Success"


result = unstable_operation()

print(result)