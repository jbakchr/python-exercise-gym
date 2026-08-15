# Exercise 05 - Accessing Attributes

## Progression

```text
✅ 01 Creating Your First Dataclass
✅ 02 Adding Multiple Fields
✅ 03 Using Type Annotations
✅ 04 Creating Dataclass Objects
➡️ 05 Accessing Attributes
⬜ 06 Understanding Generated __init__
```

---

## Goal

Learn how to:

```text
Access values stored inside a dataclass object.
```

By the end of this exercise you should understand:

- How to access dataclass attributes
- How object data is stored in fields
- How dot notation works
- How to retrieve individual values from an object

---

## Why This Matters

Creating dataclass objects is only useful if you can access the data stored inside them.

For example:

```text
User name
Product price
Configuration settings
Book title
```

All of these values are stored inside object attributes.

Accessing attributes is a fundamental skill that you will use in nearly every future dataclass exercise.

Before you can understand generated methods like `__init__()` and `__repr__()`, you should first be comfortable working with the data stored in an object.

---

## Prerequisites

```text
Complete Exercise 04 first.
```

You should already know how to:

- Create a dataclass
- Define multiple fields
- Use type annotations
- Create dataclass objects

---

## New Concept

Values stored inside an object can be accessed using dot notation.

Example:

```python
person.name
```

This retrieves the value stored in the `name` field.

Dot notation is the standard way to work with object attributes in Python.

Avoid showing the full solution while practicing this concept.

---

## Challenge

Create a dataclass called:

```python
Book
```

The dataclass should contain:

```text
title
author
pages
```

Create a `Book` object using sample values.

Print:

- The title
- The author
- The number of pages

Print each value individually by accessing the object's attributes.

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `Book` dataclass
- Define all three fields
- Create one `Book` object
- Access all three attributes
- Print each attribute separately

Do not:

- Print the entire object
- Add methods to the class

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass
class Book:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Python Basics
Jane Smith
250
```

The exact values may differ.

You should also be able to explain:

```text
How dot notation retrieves values
stored inside an object.
```

Avoid printing the whole object.

The goal is to access individual fields.

---

## Hints

### Hint 1

Create the object before attempting to access its attributes.

---

### Hint 2

Use a period (`.`) after the variable name.

---

### Hint 3

The pattern looks like:

```python
object_name.field_name
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Print the same attribute multiple times.

---

### Try 2

Create a second `Book` object and access its attributes.

---

### Try 3

Try accessing each field in a different order.

Does the stored data change?

---

## Reflection

Answer these questions:

1. What is an attribute?
2. How do you access an attribute in Python?
3. Why is dot notation useful?
4. What is the difference between printing an object and printing one attribute?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a second `Book` object and print the title of both books.

---

## Real-World Connection

Attribute access appears throughout Python applications.

Examples include:

```text
User profiles
Configuration objects
Database records
API response models
Application settings
```

Most interactions with dataclass objects involve reading or modifying attributes.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a dataclass object successfully
- [ ] You accessed attributes using dot notation
- [ ] You printed each attribute individually
- [ ] You understand how object data is retrieved

---

## Solution

See:

```text
solutions/05-accessing-attributes.py
```