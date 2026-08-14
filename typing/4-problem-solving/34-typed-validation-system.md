# Exercise 34 - Typed Validation System

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31. Refactoring Untyped Configuration
✅ 32. Replacing Any with Explicit Types
✅ 33. Type-Safe API Integration

➡️ Current Problem Solving Exercise

⬜ 35. Generic Repository Pattern
⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
TypedDict
Literal
Callable
Type Aliases
Generics
Protocols
Type Narrowing
Validation Helpers
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
An application receives data from multiple sources.

Some data comes from users.
Some comes from APIs.
Some comes from configuration files.

The current validation logic is scattered throughout
the codebase and implemented differently in each place.

Developers repeatedly write validation code such as:

- checking that strings are not empty
- checking minimum values
- checking required fields
- validating status values

The team wants a reusable validation system that is
easy to extend and provides clear validation results.
```

Example:

```python
if not username:
    raise ValueError("Username required")

if age < 18:
    raise ValueError("Age must be at least 18")

if status not in ["active", "inactive"]:
    raise ValueError("Invalid status")
```

The application works, but validation logic is duplicated throughout the codebase.

You need to design a more maintainable solution.

---

## Problem

Your task is to create a reusable typed validation system.

The system should allow developers to define validation rules and apply them consistently.

No specific architecture has been prescribed.

Part of the challenge is deciding how to represent validators and validation results while maintaining strong type safety.

The goal is not simply validating values.

The goal is creating a design that scales as the application grows.

---

## Requirements

Your solution must:

- Support validating multiple values
- Use type annotations throughout the design
- Support reusable validation rules
- Return useful validation results
- Allow multiple validation checks to be applied
- Prevent duplicated validation logic

Your solution should:

- Be easy to extend
- Encourage code reuse
- Separate validation logic from application logic
- Be understandable by another developer

Your solution must not:

- Use `Any`
- Duplicate validation implementations unnecessarily

---

## Example Usage

The completed solution should support behaviour similar to:

```python
user = {
    "username": "jonas",
    "age": 35,
}

result = validate_user(user)

if result.is_valid:
    print("Validation passed")
else:
    print(result.errors)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Validation rules can be reused.

Multiple validators can be combined.

Validation results clearly indicate success or failure.

Validation errors are easy to understand.

Application code remains clean and focused on
business behaviour rather than validation details.
```

---

## Constraints

Consider the following constraints:

- New validation rules should be easy to add
- Multiple developers may contribute validation logic
- Validation behaviour should be predictable
- Validation results should be easy to consume

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def create_user(username: str, age: int) -> None:
    if not username:
        raise ValueError("Username required")

    if age < 18:
        raise ValueError("Age must be at least 18")

    print("User created")


create_user("jonas", 35)
```

Your task is to redesign this approach.

---

## Hints

### Hint 1

Try separating validation rules from business logic.

---

### Hint 2

Think about how validators could be reused for different types of data.

---

### Hint 3

Consider whether a validation rule could be represented as a callable.

---

## Design Questions

As you work, consider:

1. How should validation results be represented?
2. How can validation rules be reused?
3. Should validation stop after the first error?
4. How will new validators be added?
5. Which typing features make the design safer?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- Validation receives invalid data
- Multiple validation failures occur
- No validation rules are supplied
- Validation passes successfully
- New validation rules are introduced later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What problems did the original approach have?
2. How did typing improve the design?
3. Which concepts from earlier exercises were most useful?
4. How reusable is your solution?
5. What would become difficult if the system grew ten times larger?

---

## Stretch Goal

Extend your solution to support:

- Validation severity levels
- Warning messages
- Validation groups
- Field-specific error reporting
- Custom validation pipelines

The stretch goal should build upon your existing design rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Web APIs
- Form processing systems
- Configuration management tools
- Data ingestion pipelines
- Internal business applications

In professional software systems, validation is often centralized into reusable frameworks because duplicated validation logic quickly becomes difficult to maintain.

Strong typing helps developers understand what is being validated, how validation behaves, and what results can be expected.

This exercise mirrors the design of validation systems commonly found in production applications.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] Validation rules are reusable
- [ ] Validation results are clearly represented
- [ ] The design uses appropriate type annotations
- [ ] The code avoids unnecessary duplication
- [ ] The solution is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative implementations

---

## Solution

See:

```text
solutions/34-typed-validation-system.py
```
