# Exercise 36 - Plugin Interface Design

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

➡️ Current Problem Solving Exercise

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
Protocol
Callable
Type Annotations
Interface Design
Dependency Inversion
Type-Safe Contracts
```

to solve a realistic problem.

This exercise focuses on creating flexible, extensible systems using typed interfaces instead of concrete implementations.

---

## Scenario

You are working on the following problem:

```text
An application processes data using a built-in
set of plugins.

The application currently depends directly on
specific plugin implementations.

Adding new plugins often requires modifying
existing application code.

The team wants a cleaner design where plugins
can be added, replaced, or removed without
changing the application itself.

The application should depend on a well-defined
contract rather than specific classes.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to define a clear plugin contract that multiple implementations can satisfy.

---

## Requirements

Your solution must:

- Define a plugin interface
- Support multiple plugin implementations
- Use typing to describe the plugin contract
- Allow plugins to be processed through a shared interface

Your solution should:

- Encourage extensibility
- Reduce coupling between application code and plugin implementations

Your solution must not:

- Use `Any`
- Depend on concrete plugin implementations everywhere in the codebase

---

## Example Usage

The completed solution should support behaviour similar to:

```python
plugin = UpperCasePlugin()

result = plugin.process("hello")

print(result)
```

Output:

```text
HELLO
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Multiple plugin implementations can be used
interchangeably.

Application code depends on a shared contract
rather than specific implementations.

New plugins can be added with minimal changes
to the existing system.
```

---

## Constraints

Consider the following constraints:

- Every plugin processes text data
- Plugins may implement different behaviour
- Application code should only depend on the plugin interface

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
class UpperCasePlugin:
    def process(self, text):
        return text.upper()


class LowerCasePlugin:
    def process(self, text):
        return text.lower()
```

---

## Hints

### Hint 1

Think about how different classes can share a common contract.

---

### Hint 2

Consider which typing construct allows you to define behaviour without requiring inheritance.

---

### Hint 3

Focus on what plugins do, not how they are implemented.

---

## Design Questions

As you work, consider:

1. Why are interfaces useful?
2. How does a plugin contract improve flexibility?
3. What benefit does typing provide?
4. How can this design reduce future code changes?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- Additional plugin types are introduced
- Multiple plugins are used together
- A plugin implementation changes internally

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. Why are plugin systems useful?
2. What problem does a Protocol solve?
3. How does the interface improve maintainability?
4. What alternatives could be used?
5. Where have you seen similar patterns in real applications?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Plugin registration
- Multiple processing methods
- Configurable plugins
- Plugin discovery
- Chained plugin execution

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- IDE extensions
- Automation tools
- Data processing systems
- Web frameworks
- Application integrations

Many successful systems use plugin architectures because they allow new functionality to be added without modifying existing application logic.

Python's `Protocol` type makes it possible to create these flexible architectures while preserving type safety and clear contracts between components.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] A plugin interface is defined
- [ ] Multiple implementations use the interface
- [ ] Application code depends on the interface rather than concrete classes
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You feel comfortable designing typed interfaces

---

## Solution

See:

```text
solutions/36-plugin-interface-design.py
```
