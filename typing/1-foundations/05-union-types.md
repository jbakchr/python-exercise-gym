# Exercise 05 - Union Types

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
✅ 04 Optional Values
➡️ 05 Union Types
⬜ 06 Lists and Collections
```

---

## Goal

Learn how to:

```text
Represent values that may be one of several types.
```

By the end of this exercise you should understand:

- What a Union type is
- When multiple valid types are useful
- How Union differs from Optional
- How Union improves function contracts

---

## Why This Matters

Sometimes a value is not simply:

```text
Present
or
Missing
```

Instead, it may legitimately be one of several different types.

For example:

```text
A user ID might be an integer.

Or

A username might be a string.
```

Without typing:

```python
def find_user(identifier):
    ...
```

It is unclear what kinds of values are allowed.

With a Union type:

```python
def find_user(identifier: Union[int, str]):
    ...
```

the function contract immediately communicates:

```text
This function accepts either an integer
or a string.
```

This makes code easier to understand and use correctly.

---

## Prerequisites

```text
Complete Exercise 04 first.
```

You should already understand:

- Parameter annotations
- Return annotations
- Optional values
- The use of `None`

---

## New Concept

The `typing` module provides `Union`.

Example:

```python
from typing import Union


def greet(value: Union[str, int]) -> str:
    return f"Hello, {value}"
```

This means:

```text
value may be a string

or

value may be an integer
```

A Union allows multiple valid types.

---

### Optional vs Union

You can think of:

```python
Optional[str]
```

as:

```python
Union[str, None]
```

An Optional value is simply a special case of a Union.

---

## Challenge

Create the following functions.

### format_user

Accepts:

```python
identifier: Union[int, str]
```

Returns:

```python
str
```

containing a formatted message.

Example:

```text
User: alice
```

or

```text
User: 123
```

---

### calculate_tax

Accepts:

```python
amount: Union[int, float]
```

Returns:

```python
float
```

containing the amount plus 20% tax.

---

### create_label

Accepts:

```python
value: Union[str, int]
```

Returns:

```python
str
```

containing a formatted label.

Example:

```text
Value: abc
```

or

```text
Value: 42
```

---

### get_discount

Accepts:

```python
customer_type: Union[str, int]
```

Returns:

```python
str
```

describing the customer discount.

The implementation can be simple.

The goal is practicing Union types.

---

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Import `Union` from `typing`
- Use Union annotations in all functions
- Use parameter and return type annotations
- Return values instead of printing inside the functions
- Call all functions and print the results

Do not:

- Use Optional
- Use custom types
- Use advanced typing features

---

## Starter Code

```python
from typing import Union


def format_user(identifier):
    pass


def calculate_tax(amount):
    pass


def create_label(value):
    pass


def get_discount(customer_type):
    pass


# Call the functions here
# Store returned values
# Print results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
User: alice
120.0
Value: 42
Standard Discount
```

The exact values may differ.

You should also be able to explain:

```text
How Union allows more than one valid type.
```

---

## Hints

### Hint 1

Import Union:

```python
from typing import Union
```

---

### Hint 2

The syntax looks like:

```python
Union[int, str]
```

---

### Hint 3

A function signature may look like:

```python
def example(value: Union[int, str]) -> str:
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Pass different valid types to each function.

---

### Try 2

Create a function that accepts:

```python
Union[int, float]
```

---

### Try 3

Compare:

```python
Optional[str]
```

with:

```python
Union[str, None]
```

Are they describing the same thing?

---

## Reflection

Answer these questions:

1. What problem does Union solve?
2. How does Union differ from Optional?
3. Why might a function accept more than one type?
4. What information does Union communicate to other developers?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
describe_value
```

that accepts:

```python
Union[str, int, float]
```

and returns a descriptive string.

---

## Real-World Connection

Union types appear frequently in modern Python applications.

Examples include:

```text
API request parameters

Configuration values

User identifiers

Data transformation pipelines

Library development

Framework code
```

Whenever multiple types are intentionally valid, Union can communicate that clearly.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You imported Union
- [ ] All functions use Union type annotations
- [ ] You understand how Union differs from Optional
- [ ] You can annotate functions that accept multiple valid types
- [ ] You can explain when Union is useful

---

## Solution

See:

```text
solutions/05-union-types.py
```