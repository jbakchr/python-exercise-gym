# Exercise 21 - Typed Configuration Data

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
➡️ Current Manipulation Exercise
⬜ Exercise 22 - Typed Environment Settings
⬜ Future Manipulation Exercises
```

---

## Goal

Use:

```text
TypedDict
Literal
Type Aliases
Function Type Annotations
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A type-safe application configuration model.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Function parameter and return types
- Type aliases
- TypedDict
- Literal
- Optional values
- Structured data modelling

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to configure a web application.

The application requires settings such as:

```text
Application name
Environment
Debug mode
Database URL
```

Without typing, configuration values can easily become inconsistent.

For example:

```python
{
    "environment": "devlopment"
}
```

contains a typo that might not be discovered until runtime.

You want to use Python's typing system to clearly define what a valid configuration looks like.

The goal is to create a reusable configuration model that tools and developers can validate before the application runs.

---

## Challenge

Build a solution that:

1. Defines a typed application configuration structure.
2. Restricts allowed environment values.
3. Provides a utility function for accessing configuration data.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type alias called `Environment`
- Restrict environments to:
  - `"development"`
  - `"testing"`
  - `"production"`
- Create a `TypedDict` named `AppConfig`
- Store:
  - application name
  - environment
  - debug flag
  - database URL
- Create a function:

```python
def get_database_url(config: AppConfig) -> str:
```

that returns the configured database URL.

Your solution should not:

- Use `Any`
- Use an untyped dictionary

---

## Starter Code

```python
from typing import Literal, TypedDict


# Create a type alias for valid environments


# Create a TypedDict named AppConfig


config = {
    "name": "My App",
    "environment": "development",
    "debug": True,
    "database_url": "sqlite:///app.db",
}


def get_database_url(config):
    pass


print(get_database_url(config))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Represent application configuration using types.
Restrict valid environment values.
Return the configured database URL.
```

Expected output:

```text
sqlite:///app.db
```

You should also be able to explain:

- Why `TypedDict` is useful
- Why `Literal` improves safety
- How the configuration structure can be reused
- What type-checking tools could catch automatically

---

## Hints

### Hint 1

A type alias can describe a small set of valid values.

Think about:

```python
Literal
```

---

### Hint 2

`TypedDict` allows you to describe the expected keys and value types of a dictionary.

---

### Hint 3

The `environment` field should use the type alias rather than plain `str`.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding more configuration fields
- Supporting optional values
- Adding logging settings
- Adding feature flags
- Creating multiple configuration objects

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this solution solve?
2. Why is a typed configuration safer than an untyped dictionary?
3. Which earlier typing concepts were reused in this exercise?
4. How could this approach help larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

Add a configuration field:

```text
log_level
```

that only accepts:

```text
INFO
WARNING
ERROR
```

using `Literal`.

---

## Real-World Connection

This pattern appears in:

- Web applications
- APIs and microservices
- CLI tools
- Data pipelines
- Cloud deployments

Developers frequently use typing to model configuration structures so that invalid values can be detected before software reaches production environments.

Typed configuration models also make applications easier to understand, document, and maintain.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The `Environment` type alias is implemented
- [ ] The `AppConfig` TypedDict is implemented
- [ ] The configuration object satisfies the type definition
- [ ] `get_database_url()` works correctly
- [ ] You understand why `Literal` improves safety
- [ ] You can explain how this pattern could be reused

---

## Solution

See:

```text
solutions/21-typed-configuration-data.py
```