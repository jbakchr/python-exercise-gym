# Exercise 26 - Type Utility Functions

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
✅ Exercise 23 - Typed API Responses
✅ Exercise 24 - Generic Container
✅ Exercise 25 - Typed Validation Helpers
➡️ Current Manipulation Exercise
⬜ Exercise 27 - Type-Safe Record Processing
```

---

## Goal

Use:

```text
TypeVar
Generic Functions
Type Annotations
Reusable Utility Design
```

to build a practical utility.

By the end of this exercise you will have created:

```text
Reusable type-safe utility functions
that work with multiple data types.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Function parameter and return types
- Type aliases
- TypedDict
- Callable
- Generic classes
- TypeVar
- Reusable utility design

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are building a collection of helper functions that will be used throughout an application.

Many utility functions should work with:

```text
Strings
Numbers
Lists
Configuration objects
API models
```

Creating separate versions of the same function for every type quickly becomes repetitive.

Instead, you want to build reusable utility functions that preserve type information regardless of what data is passed to them.

The goal is to create a generic utility that can safely work with many different types.

---

## Challenge

Build a solution that:

1. Creates a reusable generic utility function.
2. Accepts a value of any type.
3. Returns the same value.
4. Preserves the original type information.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type variable named:

```python
T
```

- Create a function:

```python
def identity(value: T) -> T:
```

- Return the value unchanged
- Demonstrate the function using:

```text
A string
An integer
```

- Show that the same function can be reused for multiple types

Your solution should not:

- Use `Any`
- Create multiple versions of the function
- Duplicate logic

---

## Starter Code

```python
from typing import TypeVar


# Create a TypeVar


# Create an identity function


print(identity("hello"))
print(identity(42))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Accept values of different types.
Return those values unchanged.
Preserve type information.
Reuse the same function for multiple types.
```

Expected output:

```text
hello
42
```

You should also be able to explain:

- What a generic function is
- Why TypeVar is useful
- How type information is preserved
- Why this approach improves reusability

---

## Hints

### Hint 1

A generic function often starts with:

```python
T = TypeVar("T")
```

---

### Hint 2

Use the type variable both as the parameter type and the return type.

---

### Hint 3

The function should simply return the value it receives.

---

## Possible Improvements

Once the basic solution works, consider:

- Creating additional generic utilities
- Building list-processing helpers
- Working with TypedDict objects
- Combining generic functions with generic containers
- Creating a utility module

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does a generic utility function solve?
2. How is this exercise similar to the Generic Container exercise?
3. Why is TypeVar important here?
4. Where might you use generic utilities in a real application?

---

## Stretch Goal

Extend the utility with one additional feature.

Create a second function:

```python
def first_item(items: list[T]) -> T:
```

that returns the first item from a list.

---

## Real-World Connection

This pattern appears in:

- Utility libraries
- Framework internals
- Data processing tools
- Repository patterns
- Reusable helper modules

Developers often build generic utility functions to reduce duplication and improve consistency across an application.

Generics make these utilities flexible while preserving type information for both developers and type-checking tools.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `TypeVar` is implemented
- [ ] A generic utility function is implemented
- [ ] String values work correctly
- [ ] Integer values work correctly
- [ ] Type information is preserved
- [ ] You understand generic functions
- [ ] You can explain why generic utilities are useful

---

## Solution

See:

```text
solutions/26-type-utility-functions.py
```