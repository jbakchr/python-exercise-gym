"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 32 - Rate Limited Service

Some external services only allow a limited number
of requests.

A decorator can be used to enforce request limits
without duplicating counting logic inside every
function.
"""


def rate_limit(max_calls):
    def decorator(func):
        call_count = 0

        def wrapper(*args, **kwargs):
            nonlocal call_count

            if call_count >= max_calls:
                print("Request limit exceeded.")
                return

            call_count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(max_calls=3)
def get_weather():
    print("Getting weather data...")


@rate_limit(max_calls=2)
def get_forecast():
    print("Getting forecast data...")


def main():
    get_weather()
    get_weather()
    get_weather()
    get_weather()

    print()

    get_forecast()
    get_forecast()
    get_forecast()


if __name__ == "__main__":
    main()