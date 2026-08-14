# Exercise 33 - Type-Safe API Integration

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ Refactoring Untyped Configuration
✅ Replacing Any with Explicit Types

➡️ Current Problem Solving Exercise

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
Optional
Type Aliases
Union
Literal
Function Annotations
Type Narrowing
Structured Data Modelling
```

to solve a realistic problem.

This exercise focuses on modelling external API data using explicit types and creating safer interfaces between your application and external services.

---

## Scenario

You are working on the following problem:

```text
A web application retrieves user data from an
external API.

The API always returns dictionaries but the
developers have never formally documented the
response structure.

As the application grows, bugs are appearing
because developers make incorrect assumptions
about the data being returned.

The team wants a type-safe integration that
clearly describes the expected API response
structure.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to model API responses using the typing tools you have learned so far.

---

## Requirements

Your solution must:

- Define an explicit type for the API response
- Model the user data returned by the API
- Use type annotations throughout the solution
- Return properly typed data from helper functions

Your solution should:

- Be easy to understand
- Make the API response structure obvious

Your solution must not:

- Use `Any`
- Rely on undocumented data structures

---

## Example Usage

The completed solution should support behaviour similar to:

```python
user = fetch_user()

print(user["name"])
print(user["email"])
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
API responses are represented using clearly
defined types.

Developers can understand the expected structure
of the response without reading additional
documentation.

Incorrect assumptions about API data become
easier to detect during development.
```

---

## Constraints

Consider the following constraints:

- The API returns dictionary-based data
- User IDs are integers
- Some fields may be optional

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def fetch_user():
    return {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "active": True,
    }
```

---

## Hints

### Hint 1

Think about how API responses are commonly represented in Python applications.

---

### Hint 2

A fixed dictionary structure can often be modelled explicitly.

---

### Hint 3

Consider whether every field is always guaranteed to exist.

---

## Design Questions

As you work, consider:

1. How should API response data be represented?
2. Which fields are required?
3. Which fields might be optional?
4. How can type annotations improve maintainability?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- New fields are added to the response
- Some optional information is unavailable
- Multiple developers work with the same API response

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. Why is typing especially useful when working with APIs?
2. What risks exist when API responses are undocumented?
3. Which typing constructs were most useful?
4. What assumptions did you make about the response structure?
5. How would this approach scale to larger APIs?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Multiple API response types
- Nested response structures
- Response status models
- Error response handling

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- REST APIs
- FastAPI applications
- Internal services
- Third-party integrations
- Cloud platforms

Professional Python applications frequently consume external APIs.

Well-designed type annotations help developers understand external data contracts, improve IDE support, and reduce integration mistakes.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] API responses use explicit types
- [ ] The response structure is clearly documented through typing
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel comfortable modelling API responses with typing

---

## Solution

See:

```text
solutions/33-type-safe-api-integration.py
```