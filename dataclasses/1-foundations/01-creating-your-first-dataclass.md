# Exercise 01 - Creating Your First Dataclass

## Progression

```text
✅ Previous Exercise

➡️ Current Exercise

⬜ Exercise 02 - Adding Multiple Fields

⬜ Future Exercises
```

---

## Goal

Learn how to:

```text
Create a dataclass using @dataclass.
```

By the end of this exercise you should understand:

- What a dataclass is
- How to create a simple dataclass
- How dataclass fields are defined

---

## Why This Matters

Dataclasses are one of the most common ways to represent structured data in modern Python.

Instead of writing repetitive code for constructors and object representations, you can describe the data you want and let Python generate much of the boilerplate for you.

This exercise introduces the foundation that every future dataclass exercise will build upon.

Later exercises will use dataclasses to model:

```text
Users
Products
Configuration Settings
API Responses
Application Data
```

---

## Prerequisites

```text
Basic understanding of Python classes.

Typing foundations are helpful but not required.
```

---

## New Concept

A dataclass is a class that is primarily used to store data.

Python can automatically generate useful methods such as:

- `__init__`
- `__repr__`
- `__eq__`

when you decorate the class with `@dataclass`.

Example:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
```

Notice that the class only describes the data it contains.

---

## Challenge

Create a dataclass called:

```python
Person
```

The dataclass should contain a single field:

```python
name
```

Create an instance of the dataclass and store the name:

```text
Alice
```

Finally, print the object.

---

## Requirements

Your solution must:

- Import `dataclass` from the `dataclasses` module
- Create a dataclass named `Person`
- Define a field called `name`
- Create a `Person` object with the name `"Alice"`
- Print the object

Do not:

- Write your own `__init__` method
- Use a regular class without `@dataclass`

---

## Starter Code

```python
from dataclasses import dataclass


# Create your dataclass here


# Create a Person object


# Print the object
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Person(name='Alice')
```

You should also be able to explain:

```text
Why @dataclass can generate functionality automatically.
```

Avoid copying the output exactly into your solution.

---

## Hints

### Hint 1

A dataclass starts with a decorator.

```python
@dataclass
```

---

### Hint 2

Fields inside a dataclass use type annotations.

```python
name: str
```

---

### Hint 3

Create an instance by calling the class and passing a value for `name`.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a second `Person` object with a different name.

---

### Try 2

Add another field called:

```python
age
```

and observe what changes.

---

### Try 3

Print multiple `Person` objects and compare the output.

---

## Reflection

Answer these questions:

1. What does the `@dataclass` decorator do?
2. Why is `name` written with a type annotation?
3. What would happen if you removed `@dataclass`?
4. How is a dataclass different from a dictionary?

The goal is to reinforce understanding.

---

## Stretch Goal

Add a second field:

```python
age: int
```

Create a new object and print it.

The goal is simply to become more comfortable defining dataclass fields.

---

## Real-World Connection

Dataclasses commonly appear in:

```text
Configuration Objects

API Requests and Responses

User Profiles

Application Settings

Domain Models

Data Processing Pipelines
```

Whenever a program needs to represent structured data, a dataclass is often a good choice.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a dataclass using `@dataclass`
- [ ] You can define dataclass fields using type annotations
- [ ] You can create an instance of a dataclass
- [ ] You understand that Python generates functionality automatically

---

## Solution

See:

```text
solutions/01-creating-your-first-dataclass.py
```