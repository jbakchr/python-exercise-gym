# Exercise 39 - Designing a Type-Safe Architecture

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

➡️ Current Problem Solving Exercise

⬜ Typing Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
TypedDict
TypeVar
Generic
Protocol
Service Interfaces
Repository Patterns
Type-Safe Design
Application Modelling
```

to solve a realistic problem.

This exercise focuses on combining multiple typing techniques into a cohesive application architecture.

---

## Scenario

You are working on the following problem:

```text
A small application has grown over time and now
contains configuration management, data storage,
business logic, and processing components.

Different developers have contributed code using
various patterns and levels of type safety.

The application works, but the architecture is
becoming harder to understand and maintain.

The team wants to redesign the system using clear,
type-safe boundaries between components.

The goal is not merely to add type annotations,
but to create an architecture where each part of
the system has a well-defined responsibility and
interface.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how the different components of the application should interact and which typing constructs should be used to describe those interactions.

---

## Requirements

Your solution must:

- Define a typed configuration model
- Define a repository abstraction
- Define a service layer
- Use typed interfaces between components
- Preserve type safety throughout the application

Your solution should:

- Encourage separation of concerns
- Encourage maintainability
- Reduce coupling between layers

Your solution must not:

- Use `Any`
- Place all logic in a single class or function

---

## Example Usage

The completed solution should support behaviour similar to:

```python
config = load_config()

repository = InMemoryRepository()

service = UserService(repository, config)

service.create_user("Alice")

user = service.get_user(0)

print(user)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Configuration, storage, and business logic are
separated into distinct layers.

Components interact through well-defined typed
contracts.

The architecture remains understandable as the
application grows.

New implementations can be introduced without
requiring major changes to existing code.
```

---

## Constraints

Consider the following constraints:

- Configuration data must be typed
- Storage implementations may change in the future
- Business logic should remain separate from infrastructure concerns

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
config = {
    "environment": "development"
}


class UserService:
    pass
```

---

## Hints

### Hint 1

Think about the major components that appear in many real applications.

---

### Hint 2

Consider how the previous exercises can work together.

---

### Hint 3

Pay attention to the boundaries between layers and responsibilities.

---

## Design Questions

As you work, consider:

1. Which responsibilities belong in each layer?
2. How should components communicate?
3. Which parts of the system should depend on interfaces?
4. How can typing make the architecture easier to maintain?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- A new repository implementation is introduced
- Additional services are added to the application
- Configuration requirements grow over time

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. Which typing concepts were most useful?
2. How did typing influence your architecture?
3. Which components were easiest to separate?
4. What trade-offs did you make?
5. How would the design evolve in a larger application?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Multiple service types
- Additional repositories
- Plugin-based processing
- Generic repositories
- Typed event handling

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Business applications
- Internal tools
- APIs
- Backend services
- Enterprise systems

As applications grow, maintaining clear architectural boundaries becomes increasingly important.

Typing is not only useful for annotating individual functions. It can also help define contracts between layers, improve maintainability, and communicate architectural intent across a development team.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] Configuration is typed
- [ ] Repository and service layers are clearly separated
- [ ] Components interact through typed contracts
- [ ] The code is understandable and maintainable
- [ ] You can explain your architectural decisions
- [ ] You feel comfortable using typing to model larger applications

---

## Solution

See:

```text
solutions/39-designing-a-type-safe-architecture.py
```