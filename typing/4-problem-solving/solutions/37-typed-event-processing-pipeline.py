"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 37 - Typed Event Processing Pipeline

TypedDict and Literal can be used together to model
different event structures safely.

By combining multiple event types into a union,
Python can narrow types based on event values and
provide better type checking when processing data.
"""

from typing import Literal, TypedDict


class UserRegisteredEvent(TypedDict):
    type: Literal["user_registered"]
    username: str


class PaymentReceivedEvent(TypedDict):
    type: Literal["payment_received"]
    amount: float


Event = UserRegisteredEvent | PaymentReceivedEvent


def process_event(event: Event) -> None:
    if event["type"] == "user_registered":
        print(f"Creating account for {event['username']}")

    elif event["type"] == "payment_received":
        print(f"Processing payment: {event['amount']}")


def main() -> None:
    events: list[Event] = [
        {
            "type": "user_registered",
            "username": "jonas",
        },
        {
            "type": "payment_received",
            "amount": 100.0,
        },
    ]

    for event in events:
        process_event(event)


if __name__ == "__main__":
    main()