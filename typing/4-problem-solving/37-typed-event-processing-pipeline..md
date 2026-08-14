# Exercise 37 - Typed Event Processing Pipeline

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31. Refactoring Untyped Configuration
✅ 32. Replacing Any with Explicit Types
✅ 33. Type-Safe API Integration
✅ 34. Typed Validation System
✅ 35. Generic Repository Pattern
✅ 36. Plugin Interface Design

➡️ Current Problem Solving Exercise

⬜ 38. Service Layer Refactoring
⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
TypedDict
Literal
Type Aliases
Type Narrowing
Protocols
Generics
Callable
Data Transformation
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
An application receives events from multiple
systems.

Examples include:

- User registrations
- Orders
- Payments
- Notifications

Each event has a different structure.

The current implementation processes everything
using untyped dictionaries.

Developers frequently access missing keys,
misinterpret fields, and accidentally process
events using the wrong logic.

The team wants a safer and more maintainable
approach for processing incoming events.
```

Example:

```python
event = {
    "type": "user_registered",
    "username": "jonas",
}
```

The application currently relies on runtime assumptions:

```python
if event["type"] == "user_registered":
    create_account(event["username"])
```

As more event types are added, the codebase becomes increasingly difficult to maintain.

You need to design a type-safe event processing pipeline.

---

## Problem

Your task is to create a solution that can process different event types while maintaining strong type safety.

No single technique has been prescribed.

Part of the challenge is deciding how events should be represented and how processing logic should be organized.

Your design should help developers understand:

- Which event types exist
- Which fields belong to each event
- Which processing logic handles each event

The goal is not merely processing events.

The goal is designing an event pipeline that remains maintainable as the application grows.

---

## Requirements

Your solution must:

- Support multiple event types
- Use type annotations throughout
- Define explicit event structures
- Process events differently based on their type
- Avoid duplicated processing logic
- Make invalid event usage difficult

Your solution should:

- Be easy to extend
- Encourage separation of concerns
- Improve readability
- Reduce runtime mistakes

Your solution must not:

- Use `Any`
- Treat every event as a generic dictionary

---

## Example Usage

The completed solution should support behaviour similar to:

```python
event = {
    "type": "user_registered",
    "username": "jonas",
}

process_event(event)
```

Or:

```python
event = {
    "type": "payment_received",
    "amount": 100.0,
}

process_event(event)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Different event types are clearly defined.

Each event is processed by the correct logic.

Developers can discover event fields through
type hints.

The processing pipeline remains understandable
as additional event types are introduced.

The system becomes easier to maintain and extend.
```

---

## Constraints

Consider the following constraints:

- New event types may be added later
- Multiple developers may contribute event handlers
- Event processing should remain easy to understand
- Event definitions should be explicit and discoverable

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
events = [
    {
        "type": "user_registered",
        "username": "jonas",
    },
    {
        "type": "payment_received",
        "amount": 100.0,
    },
]


def process_event(event):
    if event["type"] == "user_registered":
        print(f"Creating account for {event['username']}")

    elif event["type"] == "payment_received":
        print(f"Processing payment: {event['amount']}")


for event in events:
    process_event(event)
```

Your task is to improve this design.

---

## Hints

### Hint 1

Different events often contain different fields.

Think about how you can represent those differences explicitly.

---

### Hint 2

Consider how earlier exercises used `TypedDict` and `Literal` to model structured data.

---

### Hint 3

Think about how processing logic should evolve when many new event types are introduced.

---

## Design Questions

As you work, consider:

1. How should event types be represented?
2. How should processing logic be organized?
3. How will new event types be added?
4. How can typing help prevent mistakes?
5. Which previous exercises influenced your design?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- A new event type is introduced
- An expected field is missing
- An event contains invalid data
- Many event types must be supported
- Processing logic becomes distributed across multiple modules

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What problems existed in the original implementation?
2. How did typing improve event handling?
3. Which concepts from earlier exercises were most useful?
4. How scalable is your design?
5. What did this exercise teach you about designing data pipelines?

---

## Stretch Goal

Extend your solution to support:

- Event priorities
- Event metadata
- Event validation
- Event routing
- Plugin-based event handlers

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Event-driven architectures
- Microservices
- Message queues
- Background processing systems
- Web applications

Many production systems communicate through events.

Developers often use strong typing to ensure that event producers and event consumers agree on event structure and behaviour.

Typed event models help prevent integration errors, improve maintainability, and make large systems easier to understand.

This exercise mirrors a common architectural challenge found in modern software systems.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] Multiple event types are supported
- [ ] Event structures are explicitly typed
- [ ] Processing logic is clean and maintainable
- [ ] The solution avoids unnecessary duplication
- [ ] The design is easy to extend
- [ ] You can explain your design decisions
- [ ] You can identify alternative solutions

---

## Solution

See:

```text
solutions/37-typed-event-processing-pipeline.py
```