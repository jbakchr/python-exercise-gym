# Exercise 38 - Service Layer Refactoring

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

➡️ Current Problem Solving Exercise

⬜ Designing a Type-Safe Architecture
⬜ Typing Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Protocols
TypedDict
Generic Design
Type Annotations
Service Interfaces
Dependency Injection
Type-Safe Contracts
```

to solve a realistic problem.

This exercise focuses on improving an application service layer by replacing tightly coupled implementations with clearly defined typed interfaces.

---

## Scenario

You are working on the following problem:

```text
An application contains a user service responsible
for creating and retrieving users.

The service directly depends on a specific
repository implementation.

As the application grows, developers want to
replace the repository with alternative
implementations for testing and future features.

The current design makes this difficult because
the service is tightly coupled to one concrete
class.

The team wants a more flexible design built
around typed contracts.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to separate service logic from implementation details while maintaining strong type safety.

---

## Requirements

Your solution must:

- Create a service layer
- Use a typed interface for data access
- Allow different repository implementations
- Preserve type safety throughout the design
- Keep business logic separate from storage logic

Your solution should:

- Encourage loose coupling
- Improve maintainability

Your solution must not:

- Use `Any`
- Hard-code repository implementations inside the service

---

## Example Usage

The completed solution should support behaviour similar to:

```python
repository = InMemoryUserRepository()

service = UserService(repository)

service.create_user("Alice")

user = service.get_user(0)

print(user)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
The service interacts with a repository through a
well-defined contract.

Different repository implementations can be used
without changing service code.

Business logic remains independent from storage
details.

The design becomes easier to test and extend.
```

---

## Constraints

Consider the following constraints:

- Repositories may change in the future
- Business logic should remain in the service layer
- Storage details should remain outside the service layer

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
class UserRepository:
    def add(self, name):
        pass


class UserService:
    def __init__(self):
        self.repository = UserRepository()
```

---

## Hints

### Hint 1

Focus on the dependency between the service and repository.

---

### Hint 2

Consider how interfaces can reduce coupling.

---

### Hint 3

The service should depend on behaviour rather than a specific implementation.

---

## Design Questions

As you work, consider:

1. Why is tight coupling a problem?
2. What responsibilities belong in the service layer?
3. What responsibilities belong in the repository layer?
4. How does typing improve the relationship between the two?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- A new repository implementation is introduced
- The application requires testing without a real repository
- Additional service methods are added later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What problem did the refactoring solve?
2. Why are typed interfaces useful here?
3. How did the service layer become more flexible?
4. What benefits does loose coupling provide?
5. Where might you use this pattern in real projects?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Logging repositories
- Database-backed repositories
- Mock repositories for testing
- Additional service methods
- Multiple service types

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Business applications
- FastAPI services
- Internal tools
- Enterprise applications
- Microservices

Service layers are commonly used to separate business logic from infrastructure concerns.

Typed interfaces help developers create flexible architectures that are easier to maintain, test, and extend as applications grow.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The service depends on a typed contract
- [ ] Repository implementations can be replaced easily
- [ ] Business and storage logic are separated
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You feel comfortable designing typed service layers

---

## Solution

See:

```text
solutions/38-service-layer-refactoring.py
```