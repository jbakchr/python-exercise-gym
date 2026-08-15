# Exercise 09 - Using Default Values

## Progression

```text
✅ 01 Creating Your First Dataclass
✅ 02 Adding Multiple Fields
✅ 03 Using Type Annotations
✅ 04 Creating Dataclass Objects
✅ 05 Accessing Attributes
✅ 06 Understanding Generated __init__
✅ 07 Understanding Generated __repr__
✅ 08 Comparing Dataclass Objects
➡️ 09 Using Default Values
⬜ 10 Building a Simple Data Model
```

---

## Goal

Learn how to:

```text
Assign default values to dataclass fields.
```

By the end of this exercise you should understand:

- How default field values work
- Why default values can be useful
- How dataclasses generate constructors using defaults
- How default values make object creation easier

---

## Why This Matters

Not every piece of data needs to be supplied every time an object is created.

For example:

```text
A new user may start with:
- An active status of True

A new product may start with:
- A stock quantity of 0

A new game character may start with:
- A level of 1
```

Default values make common situations easier by allowing Python to automatically provide values when none are supplied.

This is one of the most useful features of dataclasses and appears frequently in real-world application models.

---

## Prerequisites

```text
Complete Exercise 08 first.
```

You should already know how to:

- Create dataclasses
- Define fields
- Use type annotations
- Create objects
- Access attributes
- Understand generated methods

---

## New Concept

Dataclass fields can be given default values.

Example:

```python
@dataclass
class User:
    username: str
    active: bool = True
```

When a value is not provided for `active`, Python automatically uses:

```python
True
```

The field still exists, but its value becomes optional during object creation.

---

## Challenge

Create a dataclass called:

```python
User
```

The dataclass should contain:

```text
username
active
```

Requirements:

- `username` should not have a default value.
- `active` should default to `True`.

Create a `User` object by supplying only a username.

Print the object.

Observe how the default value is automatically applied.

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `User` dataclass
- Define both fields using type annotations
- Assign a default value to `active`
- Create an object without providing `active`
- Print the object

Do not:

- Create custom methods
- Use `field()` or `default_factory`
- Override the default value

---

## Starter Code

```python
from dataclasses import dataclass


# Create your User dataclass here


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
User(username='alice', active=True)
```

The exact username may differ.

You should also be able to explain:

```text
Why the active field received a value
even though you did not provide one.
```

Avoid manually assigning the value after object creation.

The goal is to let the dataclass use the default automatically.

---

## Hints

### Hint 1

A default value is assigned directly in the field definition.

---

### Hint 2

The pattern looks like:

```python
field_name: type = value
```

---

### Hint 3

Create the object using only a username.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create another user and explicitly set:

```python
active=False
```

---

### Try 2

Change the default value.

What happens to newly created objects?

---

### Try 3

Add an additional field with its own default value.

---

## Reflection

Answer these questions:

1. What is a default value?
2. Why are default values useful?
3. What happens when a value is not provided?
4. When might default values simplify application code?

The goal is to reinforce understanding.

---

## Stretch Goal

Add a third field:

```text
role
```

Give it a default value such as:

```text
member
```

Create a new object and observe the generated output.

---

## Real-World Connection

Default values are commonly used for:

```text
Application settings
Configuration objects
User accounts
Product inventories
Game characters
API request models
```

They help reduce repetitive code and provide sensible starting values for objects.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a dataclass with a default value
- [ ] You created an object without supplying every field
- [ ] You observed the default value being used automatically
- [ ] You understand why default values are useful

---

## Solution

See:

```text
solutions/09-using-default-values.py
```