# Exercise 03 - Using Type Annotations

## Progression

```text
✅ 01 Creating Your First Dataclass
✅ 02 Adding Multiple Fields
➡️ 03 Using Type Annotations
⬜ 04 Creating Dataclass Objects
```

---

## Goal

Learn how to:

```text
Use type annotations when defining dataclass fields.
```

By the end of this exercise you should understand:

- Why dataclass fields use type annotations
- How type annotations describe expected data
- How dataclasses and typing work together

---

## Why This Matters

Dataclasses and type annotations are designed to work together.

The type annotations you add to a dataclass field communicate:

```text
What kind of data belongs in the field
```

This makes code easier to understand and helps tools detect mistakes.

You recently completed the Typing topic.

Dataclasses are one of the most common places where type annotations are used in real-world Python applications.

---

## Prerequisites

```text
Complete Exercise 02 first.
```

You should already know how to:

- Create a dataclass
- Add multiple fields
- Create an object from a dataclass

---

## New Concept

Dataclass fields use type annotations to describe the expected type of each value.

Example:

```python
name: str
age: int
```

This tells readers (and development tools) what kind of data should be stored in each field.

The annotations do not create the field values.

They describe them.

---

## Challenge

Create a dataclass called:

```python
Book
```

The dataclass should have these fields:

```text
title
author
pages
```

Use appropriate type annotations for each field.

Create a `Book` object using sample values.

Print the object.

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `Book` dataclass
- Add three fields
- Use type annotations for every field
- Create one `Book` object
- Print the object

Do not:

- Add methods to the class
- Add default values yet
- Use types that do not match the data

---

## Starter Code

```python
from dataclasses import dataclass


# Create your Book dataclass here


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Book(title='Python Basics', author='Jane Smith', pages=250)
```

The exact values may differ.

You should also be able to explain:

```text
Why each field has a type annotation
and what information the annotation provides.
```

Avoid including extra features.

---

## Hints

### Hint 1

A book title and author are text values.

---

### Hint 2

The number of pages is a whole number.

---

### Hint 3

Every field declaration should follow this pattern:

```python
field_name: field_type
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a second `Book` object.

---

### Try 2

Add another field temporarily.

For example:

```text
publisher
```

---

### Try 3

Read the type annotations and ask yourself:

```text
Could another developer understand the
structure of this data just from the annotations?
```

---

## Reflection

Answer these questions:

1. What is the purpose of a type annotation?
2. Why are type annotations useful when reading code?
3. Which field uses `int`?
4. Which fields use `str`?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a second dataclass called:

```python
Movie
```

Include appropriately typed fields and print a movie object.

---

## Real-World Connection

Type annotations are heavily used in dataclasses that represent:

```text
Application settings
User profiles
Configuration objects
API request models
API response models
Database records
```

In many modern Python codebases, dataclasses and type annotations are used together by default.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a dataclass with type-annotated fields
- [ ] You used appropriate types for every field
- [ ] You successfully created and printed a Book object
- [ ] You understand the purpose of type annotations in dataclasses

---

## Solution

See:

```text
solutions/03-using-type-annotations.py
```
``