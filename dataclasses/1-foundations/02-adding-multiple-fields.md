# Exercise 02 - Adding Multiple Fields

## Progression

```text
✅ 01 Creating Your First Dataclass
➡️ 02 Adding Multiple Fields
⬜ 03 Using Type Annotations
⬜ Future Exercises
```

---

## Goal

Learn how to:

```text
Define multiple fields in a dataclass.
```

By the end of this exercise you should understand:

- A dataclass can contain more than one field
- Related data can be grouped together in a single object
- Dataclasses become more useful as they model richer data

---

## Why This Matters

Most real-world objects contain multiple pieces of information.

A person is not just a name.

A person might also have:

```text
Name
Age
Email Address
```

Dataclasses allow us to group these related values into a single object.

In future exercises, you will continue expanding these models and learn how dataclasses automatically generate useful functionality based on their fields.

---

## Prerequisites

```text
Complete Exercise 01 first.
```

You should already know how to create a basic dataclass with a single field.

---

## New Concept

A dataclass can contain multiple fields.

Example:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

Each field represents a piece of data stored in the object.

Avoid thinking of a dataclass as a single value.

Think of it as a collection of related values.

---

## Challenge

Create a dataclass called:

```python
Person
```

The dataclass should contain these fields:

```text
name
age
email
```

Create a `Person` object using sample values.

Print the object.

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `Person` dataclass
- Define three fields
- Create one `Person` object
- Print the object

Do not:

- Add extra fields
- Add methods to the class

---

## Starter Code

```python
from dataclasses import dataclass


# Create your Person dataclass here


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Person(name='Alice', age=30, email='alice@example.com')
```

The exact values may differ.

You should also be able to explain:

```text
Why multiple fields make dataclasses useful
for modelling real-world data.
```

Avoid copying a finished solution.

---

## Hints

### Hint 1

Each field is declared inside the class body.

---

### Hint 2

Every field should have a type annotation.

---

### Hint 3

Create the object by providing values for all three fields.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a second `Person` object with different values.

---

### Try 2

Add a temporary fourth field.

How does the printed output change?

---

### Try 3

Change the order of the fields in the class.

What changes when creating the object?

---

## Reflection

Answer these questions:

1. Why is a dataclass useful for storing related information?
2. What does each field represent?
3. Could you store the same information without a dataclass?
4. Why might a dataclass be easier to understand than several separate variables?

The goal is to reinforce understanding.

---

## Stretch Goal

Extend the dataclass by adding:

```text
city
```

Create a new object using the additional field.

---

## Real-World Connection

Multiple-field dataclasses are commonly used for:

```text
User profiles
Application settings
Configuration objects
Product information
API response models
```

Almost all practical dataclasses contain multiple fields because they represent structured pieces of application data.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a dataclass with multiple fields
- [ ] You created a Person object successfully
- [ ] You can explain the purpose of each field
- [ ] You understand why dataclasses are useful for grouping related data

---

## Solution

See:

```text
solutions/02-adding-multiple-fields.py
```