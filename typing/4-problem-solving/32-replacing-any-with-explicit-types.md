# Exercise 32 - Replacing Any with Explicit Types

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ Refactoring Untyped Configuration
➡️ Current Problem Solving Exercise

⬜ Type-Safe API Integration
⬜ Typed Validation System
⬜ Generic Repository Pattern
⬜ Plugin Interface Design
⬜ Typed Event Processing Pipeline
⬜ Service Layer Refactoring
⬜ Designing a Type-Safe Architecture
⬜ Typing Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
TypedDict
Type Aliases
Type Narrowing
Optional
Union
Function Annotations
Domain Modelling
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A legacy application contains functions that use Any
for nearly all inputs and outputs.

The original developers adopted Any because the
structure of the data was not clearly defined.

Over time the codebase has become difficult to
understand and maintain.

The team wants to replace Any with explicit,
meaningful types that better describe the actual
data being used throughout the application.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Remove all use of `Any`
- Define explicit types for user data
- Add meaningful type annotations to all functions
- Make the expected data structure clear from the code

Your solution should:

- Encourage readability
- Make the code easier to maintain

Your solution must not:

- Use `Any`
- Introduce unnecessary complexity

---

## Example Usage

The completed solution should support behaviour similar to:

```python
user = {
    "name": "Alice",
    "email": "alice@example.com"
}

display = get_user_display(user)

print(display)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
User data is represented by a clearly defined type.

Functions communicate their expected inputs and outputs
through type annotations.

The application behaves exactly as before while
providing stronger type safety and improved readability.
```

---

## Constraints

Consider the following constraints:

- Existing behaviour must remain unchanged
- User information always contains a name and email
- The solution should remain simple and easy to understand

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
from typing import Any


def get_user_display(data: Any) -> Any:
    name = data["name"]
    email = data["email"]

    return f"{name} ({email})"
```

---

## Hints

### Hint 1

Focus on the actual structure of the data rather than the current annotations.

---

### Hint 2

Think about whether the data has a fixed shape.

---

### Hint 3

The type system should communicate intent to future developers.

---

## Design Questions

As you work, consider:

1. Why is `Any` being used here?
2. What information is currently being hidden?
3. Which typing construct best represents the data?
4. How would another developer understand the expected input?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- Additional user fields are added later
- Another developer reads the function without documentation
- The application grows and more user-related functions are introduced

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. Why is excessive use of `Any` problematic?
2. What advantages do explicit types provide?
3. Which type definition did you choose and why?
4. How did the refactoring improve readability?
5. When might `Any` still be appropriate?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- User IDs
- Optional profile information
- Different user roles
- Shared type definitions across multiple functions

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Many real-world Python projects begin with little or no typing.

As applications grow, developers often replace `Any` with explicit domain models to improve readability, IDE support, static analysis, and long-term maintainability.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The solution contains no use of `Any`
- [ ] The data structure is clearly defined
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel prepared for more open-ended challenges

---

## Solution

See:

```text
solutions/32-replacing-any-with-explicit-types.py
```