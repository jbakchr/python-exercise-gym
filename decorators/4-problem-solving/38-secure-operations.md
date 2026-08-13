# Exercise 38 - Secure Operations

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
✅ 37 - Data Validation Pipeline

➡️ Current Problem Solving Exercise

⬜ 39 - Background Task Tracking
⬜ 40 - Decorator Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Permission Decorators
Decorator Factories
Function Arguments
State Management
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A company maintains an internal administration system.

The application contains sensitive operations such as:

- Deleting users
- Resetting passwords
- Viewing confidential data

Currently, every function performs its own permission checks.

As the application grows, permission logic is becoming
duplicated and difficult to maintain.
```

Example:

```text
Some functions allow access only to administrators.

Others require managers.

Developers repeatedly write similar permission checks
throughout the codebase.
```

The development team wants a reusable solution that prevents unauthorized users from performing sensitive operations.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Restrict access to sensitive functions
- Verify whether a user has the required role
- Display a message when access is denied
- Allow authorized users to execute the function normally

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Duplicate permission-checking logic inside every function
- Allow unauthorized users to perform restricted actions
- Mix authorization concerns with business logic

---

## Example Usage

The completed solution should support behaviour similar to:

```python
delete_user("admin")

delete_user("guest")

reset_password("manager")

reset_password("guest")
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Deleting user...
```

And:

```text
Access denied.
```

Authorized users should be allowed to execute the operation.

Unauthorized users should be prevented from executing it.

---

## Constraints

Consider the following constraints:

- Different functions may require different roles
- Additional secure operations may be added later
- Authorization logic should remain separate from business logic

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def delete_user(user_role):
    print("Deleting user...")


def reset_password(user_role):
    print("Resetting password...")
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What rule must be enforced before a function executes?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Permission Decorator
Decorator Factories
State Management
```

---

### Hint 3

Different functions may require different permissions.

Think about how a reusable solution might support that.

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

- A user has the required role
- A user does not have the required role
- Different functions require different permissions
- Additional protected functions are added later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about separating security concerns from business logic?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Support multiple allowed roles
- Log failed access attempts
- Raise exceptions instead of displaying messages
- Support configurable permission levels

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Administrative systems
- Web services
- Enterprise software

Most applications contain features that should only be accessible to certain users. Developers frequently implement authorization systems that separate permission checks from business logic, making applications easier to maintain and secure.

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
solutions/38-secure-operations.py
```