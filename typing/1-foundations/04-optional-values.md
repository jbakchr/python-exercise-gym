# Exercise 04 - Optional Values

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
➡️ 04 Optional Values
⬜ 05 Union Types
```

---

## Goal

Learn how to:

```text
Represent values that may or may not exist.
```

By the end of this exercise you should understand:

- What `Optional` means
- When a value can be `None`
- How `Optional` improves function contracts
- How to safely handle missing values

---

## Why This Matters

Not every piece of information is always available.

Consider:

```text
A user may not have supplied a phone number.

A customer may not have a middle name.

A product may not have a discount price.

A configuration setting may not exist.
```

Python often represents "missing" values using:

```python
None
```

Without type hints, it may not be obvious whether a value can be `None`.

For example:

```python
def get_nickname(user_id):
    ...
```

Can this function return a string?

Can it return `None`?

We cannot tell.

With typing:

```python
def get_nickname(user_id: int) -> Optional[str]:
    ...
```

the function contract becomes much clearer.

Future exercises will build on this idea when working with:

```text
Union types
Complex data structures
TypedDict
Real-world APIs
```

---

## Prerequisites

```text
Complete Exercise 03 first.
```

You should already understand:

- Parameter annotations
- Return annotations
- Functions with multiple parameters

---

## New Concept

Sometimes a value may either be:

```text
A specific type
or
None
```

The `typing` module provides `Optional` to describe this.

Example:

```python
from typing import Optional


def get_middle_name() -> Optional[str]:
    return None
```

This means:

```text
The function may return a string.

Or

The function may return None.
```

You can think of:

```python
Optional[str]
```

as:

```text
A string that may be missing.
```

---

## Challenge

Create the following functions.

### get_middle_name

Accepts:

```python
use_middle_name: bool
```

Returns:

```python
Optional[str]
```

Return:

```python
"Marie"
```

when `use_middle_name` is `True`.

Otherwise return:

```python
None
```

---

### get_discount_code

Accepts:

```python
has_discount: bool
```

Returns:

```python
Optional[str]
```

Return:

```python
"SAVE10"
```

when a discount is available.

Otherwise return:

```python
None
```

---

### get_manager

Accepts:

```python
has_manager: bool
```

Returns:

```python
Optional[str]
```

Return a manager name when one exists.

Otherwise return:

```python
None
```

---

Call all functions and print their returned values.

---

## Requirements

Your solution must:

- Import `Optional` from `typing`
- Use `Optional[str]` as the return type
- Return real string values when available
- Return `None` when values are unavailable
- Call every function and print the returned values

Do not:

- Use `Union` yet
- Create custom types
- Introduce any new typing concepts

---

## Starter Code

```python
from typing import Optional


def get_middle_name(use_middle_name):
    pass


def get_discount_code(has_discount):
    pass


def get_manager(has_manager):
    pass


# Call the functions here
# Store returned values
# Print results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Marie
None
Sarah
```

The exact values may differ.

You should also be able to explain:

```text
Why Optional[str] is different from str.
```

---

## Hints

### Hint 1

A missing value in Python is represented by:

```python
None
```

---

### Hint 2

Import `Optional`:

```python
from typing import Optional
```

---

### Hint 3

The return annotation should look similar to:

```python
def example() -> Optional```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change some function calls so they return `None`.

---

### Try 2

Print the type of the returned values.

Example:

```python
print(type(value))
```

---

### Try 3

Create another function that returns:

```python
Optional[int]
```

---

## Reflection

Answer these questions:

1. What problem does `Optional` solve?
2. Why might `None` be a valid result?
3. How does `Optional[str]` differ from `str`?
4. Why is it useful for other developers to know when a value may be missing?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
get_bonus_points
```

that returns:

```python
Optional[int]
```

Return an integer when points are available and `None` otherwise.

---

## Real-World Connection

Optional values appear throughout real Python applications.

Examples include:

```text
Database lookups

Configuration settings

API responses

User profile information

Environment variables

Authentication systems
```

Whenever data may be missing, `Optional` is often used to communicate that possibility clearly.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You imported `Optional`
- [ ] All functions use `Optional[str]`
- [ ] You understand what `None` represents
- [ ] You understand why `Optional[str]` is different from `str`
- [ ] You can explain when Optional values are useful

---

## Solution

See:

```text
solutions/04-optional-values.py
```