# Exercise 28 - Service Interface Design

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
✅ Exercise 23 - Typed API Responses
✅ Exercise 24 - Generic Container
✅ Exercise 25 - Typed Validation Helpers
✅ Exercise 26 - Type Utility Functions
✅ Exercise 27 - Typed Data Processor
➡️ Current Manipulation Exercise
⬜ Exercise 29 - Data Transformation Pipeline
```

---

## Goal

Use:

```text
Protocol
Type Annotations
Typed Service Design
Interface-Based Programming
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A typed service interface that defines
how services should behave.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Function type annotations
- Type aliases
- Callable
- TypeVar
- Generic utilities
- TypedDict
- Reusable utility design

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are building an application that retrieves user information.

Today the data comes from:

```text
A database
```

Tomorrow the data might come from:

```text
An API
```

Or:

```text
A cache
```

You want the rest of your application to work regardless of where the data originates.

To accomplish this, you decide to define a service interface.

Any service that follows the interface should be usable by the application.

The goal is to create a typed contract that describes how a user service should behave.

---

## Challenge

Build a solution that:

1. Defines a service interface.
2. Describes a required service method.
3. Implements a service that follows the interface.
4. Uses the service through the interface rather than through a concrete implementation.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Import:

```python
Protocol
```

from the typing module.

- Create a protocol named:

```python
UserService
```

- The protocol must define:

```python
def get_username(self) -> str:
```

- Create a class named:

```python
DatabaseUserService
```

that implements the protocol.

- Return:

```text
alice
```

from the service method.

- Create a function:

```python
def display_username(service: UserService) -> None:
```

that displays the username.

Your solution should not:

- Use `Any`
- Depend on a specific implementation inside `display_username`
- Duplicate service logic

---

## Starter Code

```python
from typing import Protocol


# Create a UserService protocol


# Create a DatabaseUserService class


def display_username(service):
    pass


service = DatabaseUserService()

display_username(service)
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Define a service contract.
Implement the contract.
Use the contract instead of a concrete type.
Display a username.
```

Expected output:

```text
alice
```

You should also be able to explain:

- What a Protocol represents
- Why interfaces improve flexibility
- How services can be swapped without changing application code
- Why typing is useful for service contracts

---

## Hints

### Hint 1

A protocol defines a set of methods that a class must provide.

Example:

```python
class MyProtocol(Protocol):
    ...
```

---

### Hint 2

Your service class does not need to inherit from the protocol.

It only needs to provide the required method.

---

### Hint 3

The `display_username()` function should accept the protocol type rather than a specific class.

---

## Possible Improvements

Once the basic solution works, consider:

- Creating additional service implementations
- API-based services
- Cache-based services
- Configuration services
- Notification services

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does a service interface solve?
2. How does Protocol differ from a concrete class?
3. Why is interface-based design useful in larger applications?
4. How could this approach improve testing?

---

## Stretch Goal

Extend the utility with one additional feature.

Create another implementation:

```python
ApiUserService
```

that also satisfies the `UserService` protocol.

Use the same:

```python
display_username()
```

function without modifying it.

---

## Real-World Connection

This pattern appears in:

- Web applications
- Dependency injection systems
- Repository patterns
- Service layers
- Testable application architectures

Developers frequently define interfaces that describe behavior rather than implementation details.

Protocols make it possible to create flexible systems where components can be replaced without changing the code that uses them.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `UserService` protocol is implemented
- [ ] A service class satisfies the protocol
- [ ] `display_username()` accepts the protocol type
- [ ] The username is displayed correctly
- [ ] You understand the purpose of Protocol
- [ ] You can explain interface-based design
- [ ] You can identify real-world uses of service contracts

---

## Solution

See:

```text
solutions/28-service-interface-design.py
```