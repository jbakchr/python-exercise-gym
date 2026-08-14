# Exercise 24 - Generic Container

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
✅ Exercise 23 - Typed API Responses
➡️ Current Manipulation Exercise
⬜ Exercise 25 - Typed Validation Helpers
```

---

## Goal

Use:

```text
TypeVar
Generic
Type Annotations
Reusable Type Design
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable generic container that can
store different types of data safely.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Function parameter and return types
- Type aliases
- TypedDict
- Literal
- Nested structures
- Reusable data models
- Type-safe APIs

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are building a system that processes many different kinds of data.

For example:

```text
User records

Configuration objects

API responses

Numbers

Strings
```

You could create a separate container class for every type of data.

However, this would quickly become repetitive.

Instead, you want to build a reusable container that can safely store any type of value while preserving type information.

The goal is to create a utility that works with many different data types without sacrificing type safety.

---

## Challenge

Build a solution that:

1. Creates a generic container class.
2. Stores a value of any type.
3. Returns the stored value.
4. Preserves the original type information.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type variable named:

```python
T
```

- Create a generic class named:

```python
Container
```

- Allow the container to store a value of type `T`
- Provide a method:

```python
def get_value(self) -> T:
```

that returns the stored value

- Demonstrate the container with:

```text
A string value
An integer value
```

Your solution should not:

- Use `Any`
- Create separate classes for each data type
- Duplicate logic

---

## Starter Code

```python
from typing import Generic, TypeVar


# Create a TypeVar


# Create a generic Container class


string_container = None
number_container = None

print(string_container.get_value())
print(number_container.get_value())
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Store values of different types.
Return those values correctly.
Preserve type information.
Reuse the same class for multiple data types.
```

Expected output:

```text
hello
42
```

You should also be able to explain:

- Why generics are useful
- What TypeVar represents
- How type information is preserved
- Why this approach is better than duplicating classes

---

## Hints

### Hint 1

A generic class usually starts with:

```python
class Container(Generic[T]):
```

---

### Hint 2

The constructor should receive a value whose type matches `T`.

---

### Hint 3

The return type of `get_value()` should match the stored type.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding a method to replace the stored value
- Creating multiple containers
- Using custom classes inside the container
- Storing TypedDict objects
- Storing API response models

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem do generics solve?
2. How does TypeVar make a class reusable?
3. Why is a generic container better than using Any?
4. Where might you use this pattern in a real application?

---

## Stretch Goal

Extend the utility with one additional feature.

Add a method:

```python
def set_value(self, value: T) -> None:
```

that replaces the stored value.

---

## Real-World Connection

This pattern appears in:

- Data processing libraries
- API client libraries
- Framework internals
- Repository patterns
- Caching systems

Developers often create reusable containers, wrappers, and helper classes that work with many different data types.

Generics allow these utilities to remain flexible while preserving strong type information.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `TypeVar` is defined
- [ ] A generic `Container` class is implemented
- [ ] String data can be stored and retrieved
- [ ] Integer data can be stored and retrieved
- [ ] The same class is reused for multiple types
- [ ] You understand how generics improve type safety
- [ ] You can explain the role of `TypeVar`

---

## Solution

See:

```text
solutions/24-generic-container.py
```