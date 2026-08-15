# Exercise 04 - Creating Dataclass Objects

## Progression

```text
✅ 01 Creating Your First Dataclass
✅ 02 Adding Multiple Fields
✅ 03 Using Type Annotations
➡️ 04 Creating Dataclass Objects
⬜ 05 Accessing Attributes
```

---

## Goal

Learn how to:

```text
Create objects from a dataclass.
```

By the end of this exercise you should understand:

- How to create dataclass objects
- How values are assigned to fields
- How each object stores its own data
- How dataclass objects are created using generated constructors

---

## Why This Matters

Defining a dataclass is only the first step.

The real value of a dataclass comes from creating objects that hold actual data.

For example:

```text
User
Product
Book
Configuration
```

Each object contains a different set of values while sharing the same structure.

In future exercises you will interact with these objects by accessing and modifying their attributes.

---

## Prerequisites

```text
Complete Exercise 03 first.
```

You should already know how to:

- Create a dataclass
- Add multiple fields
- Use type annotations

---

## New Concept

Once a dataclass is defined, Python automatically creates an `__init__()` method for you.

This means you can create objects by providing values for each field.

Example:

```python
person = Person("Alice", 30)
```

A new object is created and its fields are populated with the provided values.

---

## Challenge

Create a dataclass called:

```python
Car
```

The dataclass should contain these fields:

```text
make
model
year
```

Create two different `Car` objects using different values.

Print both objects.

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `Car` dataclass
- Define all three fields
- Create two different objects
- Print both objects

Do not:

- Add methods to the class
- Add default values
- Access attributes directly yet

---

## Starter Code

```python
from dataclasses import dataclass


# Create your Car dataclass here


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Car(make='Toyota', model='Corolla', year=2022)
Car(make='Ford', model='Focus', year=2020)
```

The exact values may differ.

You should also be able to explain:

```text
How a single dataclass definition can be
used to create many different objects.
```

Avoid including additional functionality.

---

## Hints

### Hint 1

Create the dataclass before creating any objects.

---

### Hint 2

Each object should receive values for every field.

---

### Hint 3

Store each object in its own variable before printing it.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a third `Car` object.

---

### Try 2

Use completely different values.

---

### Try 3

Create several objects from the same dataclass.

What stays the same?

What changes?

---

## Reflection

Answer these questions:

1. What is an object?
2. How are two objects of the same dataclass different?
3. Why can one dataclass create many objects?
4. What information is stored inside each object?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a third `Car` object and print all three objects in order.

---

## Real-World Connection

Creating dataclass objects is common when representing:

```text
Users
Products
Orders
Configurations
API Responses
Database Records
```

A single dataclass definition often creates hundreds or thousands of objects during the lifetime of an application.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a dataclass successfully
- [ ] You created multiple objects from the dataclass
- [ ] You printed the objects
- [ ] You understand the difference between a dataclass and an object created from it

---

## Solution

See:

```text
solutions/04-creating-dataclass-objects.py
```