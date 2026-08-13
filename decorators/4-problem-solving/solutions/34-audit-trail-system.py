"""
Solution Guidelines

- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

"""
Exercise 34 - Audit Trail System

Important operations often need to be recorded
for accountability and traceability.

A decorator can automatically create audit records
without placing logging code inside every function.
"""


def audit(func):
    def wrapper(*args, **kwargs):
        print(f"AUDIT: {func.__name__} called")

        return func(*args, **kwargs)

    return wrapper


@audit
def create_invoice(customer_id, amount):
    print(f"Creating invoice for {customer_id}")

    return {
        "customer_id": customer_id,
        "amount": amount,
    }


@audit
def process_refund(customer_id, amount):
    print(f"Processing refund for {customer_id}")

    return {
        "customer_id": customer_id,
        "amount": amount,
    }


def main():
    invoice = create_invoice("customer-123", 500)
    print(invoice)

    print()

    refund = process_refund("customer-456", 200)
    print(refund)


if __name__ == "__main__":
    main()