# Exercise 31 - Refactoring Untyped Configuration

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

➡️ Current Problem Solving Exercise

⬜ Next Problem Solving Exercise
⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Type Annotations
TypedDict
Literal
Optional
Type Aliases
Validation Helpers
Service Design
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
An internal application uses configuration data
to control how it connects to services.

The configuration is stored in dictionaries and
passed around the codebase without type information.

Developers frequently misspell keys, use invalid
environment names, or provide incorrect values.

The team wants to make the configuration system
easier to understand, safer to modify, and easier
to maintain.
```

Example:

```python
config = {
    "environment": "production",
    "host": "api.company.com",
    "port": 443,
    "debug": False,
}
```

The application works, but nothing prevents a developer from writing:

```python
config = {
    "env": "prod",
    "host": "api.company.com",
    "port": "443",
}
```

The errors are only discovered at runtime.

You need to design a cleaner, typed solution.

---

## Problem

Your task is to refactor an untyped configuration system into a type-safe design.

No single technique has been prescribed.

Part of the challenge is deciding which typing tools should be used and how different concepts work together.

Your goal is not only to make the code type-safe, but also easier for future developers to understand and modify.

---

## Requirements

Your solution must:

- Create a typed representation of application configuration
- Define valid environment values
- Store host, port, and debug settings
- Include at least one optional configuration value
- Provide a way to display configuration information
- Use appropriate type annotations throughout the solution

Your solution should:

- Encourage clean code
- Improve readability
- Reduce opportunities for mistakes
- Make configuration requirements obvious

Your solution must not:

- Use `Any`
- Rely on untyped dictionaries for configuration data

---

## Example Usage

The completed solution should support behaviour similar to:

```python
config = create_config(
    environment="production",
    host="api.company.com",
    port=443,
    debug=False,
)

display_config(config)
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Configuration values are clearly defined.

Allowed environments are restricted to valid values.

Required settings must exist.

Optional settings are documented by the type system.

Developers can understand the expected structure
without reading implementation details.
```

---

## Constraints

Consider the following constraints:

- The application may support multiple environments
- New developers should quickly understand the configuration structure
- Configuration values should be discoverable through type hints
- Future configuration fields may be added later

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
# Existing untyped implementation

config = {
    "environment": "production",
    "host": "api.company.com",
    "port": 443,
    "debug": False,
}


def connect(config):
    print(
        f"Connecting to "
        f"{config['host']}:{config['port']}"
    )


connect(config)
```

Your task is to improve this design.

---

## Hints

### Hint 1

Identify the problems with the current approach before writing any code.

What mistakes could a developer make?

---

### Hint 2

Think about which typing constructs are specifically designed for structured dictionary data.

---

### Hint 3

Not every string should be valid.

Consider whether some values could be constrained.

---

## Design Questions

As you work, consider:

1. Why did you choose your approach?
2. Which typing features are most useful for modelling configuration?
3. How does your solution reduce errors?
4. Would a larger application need a different design?
5. Which previous exercises influenced your solution?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- An invalid environment value is provided
- A required configuration field is missing
- An optional field is not supplied
- A developer misspells a configuration key
- A developer supplies the wrong data type

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What problems existed in the original implementation?
2. Which typing features were most useful?
3. How did typing improve the design?
4. What trade-offs exist between flexibility and safety?
5. What did this exercise teach you about using typing in real applications?

---

## Stretch Goal

Extend your solution to support additional configuration sections.

Examples:

- Database settings
- Logging settings
- API credentials
- Cache settings

Consider how your design can scale while remaining easy to understand.

---

## Real-World Connection

Problems like this appear in:

- Web applications
- Internal business systems
- APIs
- CLI tools
- Cloud services

In real projects, configuration mistakes can cause deployment failures, connection issues, and difficult-to-debug runtime errors.

Developers often use typing to make configuration structures explicit, discoverable, and safer to modify.

This exercise mirrors a common refactoring task performed in production codebases.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The configuration structure is explicitly typed
- [ ] Environment values are constrained appropriately
- [ ] Optional fields are handled correctly
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel prepared to tackle larger refactoring challenges

---

## Solution

See:

```text
solutions/31-refactoring-untyped-configuration.py
```