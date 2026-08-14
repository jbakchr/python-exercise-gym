# Exercise 22 - Typed Environment Settings

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
➡️ Current Manipulation Exercise
⬜ Exercise 23 - Typed API Response Models
```

---

## Goal

Use:

```text
TypedDict
Literal
Type Aliases
Optional
Function Type Annotations
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A type-safe environment settings system.
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
- Typed configuration objects

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are deploying an application to multiple environments.

Different environments require different settings:

```text
Development
Testing
Production
```

Some settings may be present only in certain environments.

For example:

```text
Development may enable debugging.

Production may disable debugging but enable monitoring.

Testing may use a temporary database.
```

You want to model these settings using Python's typing system so that developers can clearly see which values are expected.

The goal is to create a reusable settings model that can represent different deployment environments safely and consistently.

---

## Challenge

Build a solution that:

1. Defines a typed environment settings structure.
2. Restricts environment names to valid values.
3. Supports optional monitoring settings.
4. Provides a utility function for determining whether debugging is enabled.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type alias called `Environment`
- Restrict environments to:
  - `"development"`
  - `"testing"`
  - `"production"`
- Create a `TypedDict` named `EnvironmentSettings`
- Include the following fields:

```text
environment
debug
database_url
monitoring_url
```

- Make `monitoring_url` optional
- Create a function:

```python
def is_debug_enabled(settings: EnvironmentSettings) -> bool:
```

that returns whether debugging is enabled.

Your solution should not:

- Use `Any`
- Use untyped dictionaries
- Hardcode environment checks inside the utility function

---

## Starter Code

```python
from typing import Literal, TypedDict


# Create an Environment type alias


# Create an EnvironmentSettings TypedDict


development_settings = {
    "environment": "development",
    "debug": True,
    "database_url": "sqlite:///dev.db",
}


def is_debug_enabled(settings):
    pass


print(is_debug_enabled(development_settings))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Represent environment-specific settings.
Restrict valid environment values.
Support optional monitoring configuration.
Determine whether debugging is enabled.
```

Expected output:

```text
True
```

You should also be able to explain:

- Why Optional is useful for configuration data
- Why Literal improves safety
- How the settings structure can support multiple environments
- How type checking can catch configuration mistakes

---

## Hints

### Hint 1

Use:

```python
Literal
```

for the allowed environment names.

---

### Hint 2

Use:

```python
Optional[str]
```

for a value that may or may not exist.

---

### Hint 3

A `TypedDict` can contain both required and optional information.

Think carefully about which setting is always present and which setting might not exist.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding log level settings
- Adding API endpoint settings
- Adding cache settings
- Creating separate settings objects for each environment
- Loading settings from external files

These are optional improvements.

---

## Reflection

Answer the following questions.

1. Why might some settings be optional?
2. How does this exercise build on Typed Configuration Data?
3. What mistakes could a type checker identify?
4. How might larger applications organize environment settings?

---

## Stretch Goal

Extend the utility with one additional feature.

Add a function:

```python
def has_monitoring(settings: EnvironmentSettings) -> bool:
```

that returns whether a monitoring URL is configured.

---

## Real-World Connection

This pattern appears in:

- Web applications
- Cloud deployments
- APIs and microservices
- CI/CD pipelines
- Internal developer tools

Developers frequently manage different settings for development, testing, and production environments.

Typed settings make these configurations easier to understand, validate, and maintain while reducing deployment mistakes.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The `Environment` type alias is implemented
- [ ] The `EnvironmentSettings` TypedDict is implemented
- [ ] The optional monitoring setting works correctly
- [ ] `is_debug_enabled()` works correctly
- [ ] You understand why Optional is useful
- [ ] You can explain how this pattern helps real applications

---

## Solution

See:

```text
solutions/22-typed-environment-settings.py
```
