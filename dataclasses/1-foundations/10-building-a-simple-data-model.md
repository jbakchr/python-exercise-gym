# Exercise 10 - Building a Simple Data Model

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
✅ 09 Using Default Values
➡️ 10 Building a Simple Data Model
⬜ Exploration Stage
```

---

## Goal

Learn how to:

```text
Combine everything learned in the Foundations
stage to model a real-world object.
```

By the end of this exercise you should understand:

- How dataclasses represent structured data
- How fields work together to model an entity
- How type annotations improve readability
- How default values simplify object creation
- Why dataclasses are useful in real applications

---

## Why This Matters

So far you have learned individual dataclass features:

```text
Creating dataclasses
Adding fields
Using type annotations
Creating objects
Accessing attributes
Generated methods
Default values
```

Real applications combine all of these concepts.

Dataclasses are primarily used to model real-world entities such as:

```text
Users
Products
Orders
Configurations
Books
Vehicles
```

This exercise brings together everything learned in the Foundations stage and gives you experience building a realistic data model.

---

## Prerequisites

```text
Complete Exercise 09 first.
```

You should already understand:

- Dataclass creation
- Multiple fields
- Type annotations
- Object creation
- Attribute access
- Generated methods
- Default values

---

## New Concept

Dataclasses are most valuable when they model real-world entities.

Example:

```text
Book
├── title
├── author
├── pages
└── available
```

Each field represents part of the data that describes the object.

Instead of storing information in separate variables, a dataclass keeps related information together in a clear and reusable structure.

---

## Challenge

Create a dataclass called:

```python
Product
```

The dataclass should contain:

```text
name
price
stock_quantity
in_stock
```

Requirements:

- Use appropriate type annotations
- Give `in_stock` a default value
- Create a Product object using sample values
- Print the object
- Print the product name
- Print the product price

---

## Requirements

Your solution must:

- Import `dataclass`
- Use the `@dataclass` decorator
- Create a `Product` dataclass
- Define all four fields
- Use type annotations for every field
- Use a default value for `in_stock`
- Create one Product object
- Print the object
- Access and print individual attributes

Do not:

- Create custom methods
- Use `field()` or `default_factory`
- Create multiple classes

---

## Starter Code

```python
from dataclasses import dataclass


# Create your Product dataclass here


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see output similar to:

```text
Product(
    name='Laptop',
    price=999.99,
    stock_quantity=15,
    in_stock=True
)

Laptop
999.99
```

The formatting may differ slightly.

You should also be able to explain:

```text
How a dataclass combines multiple pieces
of related data into a single object.
```

Avoid adding functionality beyond the requirements.

The goal is to consolidate everything learned in the Foundations stage.

---

## Hints

### Hint 1

Think about which data types are appropriate for each field.

---

### Hint 2

One field should have a default value.

---

### Hint 3

Use dot notation to access individual attributes.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a second Product object.

---

### Try 2

Change the default value of `in_stock`.

---

### Try 3

Add a temporary field such as:

```text
category
```

How does the generated output change?

---

## Reflection

Answer these questions:

1. Why is a dataclass useful for modelling products?
2. Which field uses a default value?
3. Which generated methods have you used throughout this stage?
4. How does a dataclass improve readability compared to separate variables?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a second Product object and compare the two products using:

```python
==
```

Observe how dataclass comparison behaves.

---

## Real-World Connection

Data models like this appear throughout Python applications:

```text
E-commerce systems
Inventory management
API responses
Configuration systems
Database records
Business applications
```

Many real applications contain dozens or hundreds of dataclasses that model important business entities.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You created a realistic Product dataclass
- [ ] You used type annotations correctly
- [ ] You used a default value
- [ ] You created and printed a Product object
- [ ] You accessed individual attributes
- [ ] You understand how dataclasses model structured data

---

## Solution

See:

```text
solutions/10-building-a-simple-data-model.py
```