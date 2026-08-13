# Exercise 37 - Data Validation Pipeline

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31 - Slow API Calls
✅ 32 - Rate Limited Service
✅ 33 - Expensive Calculations
✅ 34 - Audit Trail System
✅ 35 - Production Debugging
✅ 36 - Function Monitoring

➡️ Current Problem Solving Exercise

⬜ 38 - Secure Operations
⬜ 39 - Background Task Tracking
⬜ 40 - Decorator Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Validation Decorators
Function Arguments
Decorator Factories
Function Wrapping
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A Python application processes user registrations.

Several functions accept user-provided data such as:

- Names
- Email addresses
- Usernames

The development team has noticed that similar validation
checks appear throughout the codebase.

Different developers have implemented validation in
different ways, resulting in duplicated and inconsistent
logic.
```

Example:

```text
One function checks whether a name is empty.

Another function checks whether an email is empty.

A third function performs similar validation again.

The team wants a reusable solution that ensures
validation rules are applied consistently.
```

The development team wants validation to happen automatically before business logic runs.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Validate incoming data before a function executes
- Prevent invalid data from reaching business logic
- Provide feedback when validation fails
- Work across multiple functions

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Duplicate validation logic inside every function
- Allow invalid values to continue through the system
- Mix validation concerns with business logic

---

## Example Usage

The completed solution should support behaviour similar to:

```python
create_user("Alice")

create_user("")

update_email("alice@example.com")

update_email("")
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Creating user: Alice
```

And:

```text
Validation failed.
```

Invalid input should be rejected before the function executes.

Valid input should continue normally.

---

## Constraints

Consider the following constraints:

- Multiple functions may require validation
- Different validation rules may be needed in the future
- Validation should occur before business logic executes

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def create_user(name):
    print(f"Creating user: {name}")


def update_email(email):
    print(f"Updating email: {email}")
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What problem is duplicated throughout the application?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Validation Decorator
Decorator Factories
Function Arguments
```

---

### Hint 3

The validation logic should be reusable.

New functions should be able to benefit from the solution with minimal effort.

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

- An empty string is provided
- A function receives valid input
- Multiple functions use the validation solution
- New validation requirements are introduced later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about separating validation from business logic?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Validate multiple arguments
- Validate specific data types
- Support custom validation rules
- Raise exceptions instead of displaying messages

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Input validation is one of the most common concerns in software development. Applications frequently need to verify incoming data before processing it. Developers often build reusable validation systems to ensure consistency, improve maintainability, and reduce bugs caused by invalid input.

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
solutions/37-data-validation-pipeline.py
```