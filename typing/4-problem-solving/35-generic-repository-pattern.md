# Exercise 35 - Generic Repository Pattern

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ Refactoring Untyped Configuration
✅ Replacing Any with Explicit Types
✅ Type-Safe API Integration
✅ Typed Validation System

➡️ Current Problem Solving Exercise

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
TypeVar
Generic
Type Annotations
Reusable Components
Type-Safe Design
```

to solve a realistic problem.

This exercise focuses on building a reusable data-access component that can work with multiple data types while preserving type safety.

---

## Scenario

You are working on the following problem:

```text
A growing application manages users, products,
and orders.

The development team has created separate
repositories for each type of data.

Although the stored data is different, the
repositories contain nearly identical logic.

The duplicated code is becoming difficult
to maintain and extend.

The team wants a reusable solution that can
manage different types of objects while keeping
strong type guarantees.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to build a repository that can support multiple object types without sacrificing readability or type safety.

---

## Requirements

Your solution must:

- Create a reusable repository class
- Support storing different types of objects
- Preserve type information
- Allow items to be added
- Allow items to be retrieved

Your solution should:

- Minimize duplicated code
- Encourage reuse across an application

Your solution must not:

- Use `Any`
- Create a separate repository implementation for every data type

---

## Example Usage

The completed solution should support behaviour similar to:

```python
user_repository.add("Alice")
user = user_repository.get(0)

product_repository.add("Laptop")
product = product_repository.get(0)

print(user)
print(product)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
A single repository implementation can be used
for multiple types of objects.

The repository preserves the original type of
stored objects.

Developers can build reusable data access
components without duplicating logic.
```

---

## Constraints

Consider the following constraints:

- Different repositories may store different types
- Data is stored only in memory
- Retrieval should preserve type information

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
class Repository:
    pass
```

---

## Hints

### Hint 1

Think about how you could create a class that works with more than one type.

---

### Hint 2

Consider which typing construct allows one class to operate on multiple types while preserving type information.

---

### Hint 3

The repository logic should remain identical regardless of the object being stored.

---

## Design Questions

As you work, consider:

1. Why does repository duplication occur?
2. What information does typing help preserve?
3. How does a generic design improve maintainability?
4. What advantages does reuse provide?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- A repository contains no items
- Additional data types are introduced later
- Different repositories manage different object types

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What benefits does a generic repository provide?
2. Why is `TypeVar` useful in this design?
3. How did typing influence your implementation?
4. What code duplication was removed?
5. Where might this pattern be useful in real projects?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Item removal
- Item updates
- Searching
- Repository interfaces
- Repository protocols

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Business applications
- Internal tools
- APIs
- Web services
- Database-backed systems

Repository patterns are commonly used to separate business logic from data access logic.

Generics allow developers to create reusable abstractions while preserving type safety and improving maintainability.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The repository works with multiple data types
- [ ] Type information is preserved
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel comfortable building reusable generic components

---

## Solution

See:

```text
solutions/35-generic-repository-pattern.py
```