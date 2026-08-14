# Exercise 40 - Typing Design Challenge

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ Refactoring Untyped Configuration
✅ Replacing Any with Explicit Types
✅ Type-Safe API Integration
✅ Typed Validation System
✅ Generic Repository Pattern
✅ Plugin Interface Design
✅ Typed Event Processing Pipeline
✅ Service Layer Refactoring
✅ Designing a Type-Safe Architecture

➡️ Current Problem Solving Exercise

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
TypedDict
Literal
Optional
TypeVar
Generic
Protocol
Type Annotations
Service Interfaces
Repository Patterns
Architecture Design
```

to solve a realistic problem.

This exercise focuses on making architecture and design decisions rather than applying a single typing feature.

You should use the concepts learned throughout the Typing topic to design a type-safe solution to an open-ended problem.

---

## Scenario

You are working on the following problem:

```text
A small application has grown into a larger system.

The application now manages configuration,
repositories, services, data processing, and
external integrations.

The code works, but there is no consistent
approach to typing.

Different modules use different conventions,
and developers often disagree about how data,
interfaces, and components should be modelled.

The team wants a type-safe design that provides
clear contracts between components while
remaining maintainable and easy to extend.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding which typing constructs are appropriate and how they should be combined.

This exercise intentionally provides more freedom than previous exercises.

---

## Requirements

Your solution must:

- Define at least one typed data model
- Define at least one typed interface
- Include a service layer
- Include some form of typed configuration
- Demonstrate interaction between multiple components

Your solution should:

- Encourage maintainability
- Encourage separation of concerns
- Use typing as a design tool rather than decoration

Your solution must not:

- Use `Any`
- Place all functionality in a single class
- Ignore type contracts between components

---

## Example Usage

The completed solution should support behaviour similar to:

```python
config = load_config()

repository = Repository()

service = ApplicationService(
    repository=repository,
    config=config,
)

result = service.run()

print(result)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Multiple parts of the application communicate
through clearly defined typed contracts.

The structure of the system is easy to understand.

Developers can extend individual components
without unexpectedly affecting other parts of
the application.

Typing is used to clarify design and intent
throughout the architecture.
```

---

## Constraints

Consider the following constraints:

- Components should have clear responsibilities
- Data structures should be explicitly modelled
- Application layers should remain loosely coupled

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def load_config():
    return {}


class ApplicationService:
    pass
```

---

## Hints

### Hint 1

Review the concepts used throughout Exercises 31-39.

---

### Hint 2

Focus on designing clear boundaries between components.

---

### Hint 3

There is rarely a single correct architecture.

Think about trade-offs and maintainability.

---

## Design Questions

As you work, consider:

1. Which typing constructs are most appropriate?
2. What responsibilities belong in each component?
3. How should components communicate?
4. Which contracts should be defined explicitly?
5. How does typing improve the overall design?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- New application features are added
- New implementations replace existing ones
- More developers contribute to the codebase
- Additional services and repositories are introduced

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. Which typing concepts were most useful?
2. Which design decisions were most difficult?
3. What trade-offs did you make?
4. How did typing influence the architecture?
5. What would you improve in a future iteration?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Plugin support
- Event processing
- Multiple repositories
- Generic service layers
- Additional configuration options

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Enterprise systems
- Internal tools
- APIs
- Backend services

Professional developers rarely apply typing in isolation.

Instead, they use typing to model data, define contracts, communicate intent, and improve maintainability across an entire application.

The challenge of designing a coherent type-safe architecture becomes increasingly important as systems grow.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] Multiple typing concepts are combined effectively
- [ ] Components communicate through typed contracts
- [ ] The architecture is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can justify your choice of typing constructs
- [ ] You feel confident applying typing to real-world software design

---

## Solution

See:

```text
solutions/40-typing-design-challenge.py
```
