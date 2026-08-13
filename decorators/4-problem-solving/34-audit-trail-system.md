# Exercise 34 - Audit Trail System

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31 - Slow API Calls
✅ 32 - Rate Limited Service
✅ 33 - Expensive Calculations

➡️ Current Problem Solving Exercise

⬜ 35 - Production Debugging
⬜ 36 - Function Monitoring
⬜ 37 - Data Validation Pipeline
⬜ 38 - Secure Operations
⬜ 39 - Background Task Tracking
⬜ 40 - Decorator Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Logging Decorators
Function Arguments
Function Metadata
Reusable Utilities
Decorator Composition
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A company has developed an internal financial system.

Employees can perform sensitive operations such as:

- Creating invoices
- Processing refunds
- Transferring funds

Management wants a record of these actions so that
important operations can be reviewed later.

Currently, developers manually add logging statements
inside individual functions, resulting in duplicated
and inconsistent code.
```

Example:

```text
A refund is issued for customer 123.

Several weeks later, the finance team wants to know:

- Who performed the action?
- Which operation was executed?
- When did it happen?
```

The team wants a reusable solution that automatically records important activity.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Record when a monitored function is executed
- Display the function name
- Display information about the operation being performed
- Continue returning the original function result

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Place audit logging code inside every function
- Change the behaviour of the wrapped functions
- Require developers to manually record actions

---

## Example Usage

The completed solution should support behaviour similar to:

```python
create_invoice("customer-123", 500)

process_refund("customer-456", 200)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
AUDIT: create_invoice called

Creating invoice...

AUDIT: process_refund called

Processing refund...
```

Important operations should automatically generate audit records.

The original functions should continue working normally.

---

## Constraints

Consider the following constraints:

- Multiple functions may require auditing
- Future sensitive operations may be added later
- The auditing logic should remain separate from business logic

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def create_invoice(customer_id, amount):
    print(f"Creating invoice for {customer_id}")

    return {
        "customer_id": customer_id,
        "amount": amount,
    }


def process_refund(customer_id, amount):
    print(f"Processing refund for {customer_id}")

    return {
        "customer_id": customer_id,
        "amount": amount,
    }
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What information does management want to capture?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Logging Decorators
Function Metadata
Function Arguments
```

---

### Hint 3

Think about how a single solution could be applied to many important functions.

---

## Design Questions

As you work, consider:

1. Why did you choose your approach?
2. Were there alternative solutions?
3. What trade-offs exist?
4. Which previous exercises influenced your design?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- Several different functions use auditing
- Functions accept different arguments
- Additional sensitive operations are added later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about accountability and traceability in software systems?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Include timestamps in audit records
- Record function arguments
- Write audit information to a file
- Support different audit levels

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Financial systems
- Web services
- Enterprise software

Many organizations must maintain audit trails for security, compliance, accountability, and troubleshooting purposes. Developers often build reusable auditing mechanisms so important activity can be tracked without scattering logging code throughout the application.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The solution handles the important edge cases
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel prepared for more open-ended challenges

---

## Solution

See:

```text
solutions/34-audit-trail-system.py
```