# Exercise 19 - Nested Dataclasses

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
✅ Exercise 14 - Immutable Dataclasses
✅ Exercise 15 - Field Customization
✅ Exercise 16 - Ordering Objects
✅ Exercise 17 - Sorting Dataclass Instances
✅ Exercise 18 - Post Initialization
➡️ Current Exploration Exercise
⬜ Exercise 20 - Dataclass Design Patterns
```

---

## Goal

Explore how:

```text
Nested Dataclasses
```

behave in different situations.

By the end of this exercise you should understand:

- How one dataclass can contain another dataclass
- How nested objects are created and accessed
- Why nested dataclasses are useful for modelling complex data

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Object creation
- Post initialization
- Type annotations

If not, review:

```text
Exercise 18 - Post Initialization
```

---

## Focus Area

This exercise explores:

```text
Dataclasses that contain other
dataclass objects.
```

Example:

```text
A user has an address.

Both the user and the address can
be represented as separate dataclasses.
```

This is not a new concept.

It is a deeper look at how dataclasses can be combined to model larger structures.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a dataclass that contains another dataclass.
2. Create objects for both dataclasses.
3. Access data through the nested structure.

As you work, pay attention to:

- How nested objects are created
- How nested attributes are accessed
- How the generated representation looks

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    country: str


@dataclass
class User:
    username: str
    address: Address


address = Address(
    city="Copenhagen",
    country="Denmark",
)

user = User(
    username="alice",
    address=address,
)

print(user)
print(user.address.city)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What does the printed User object
look like?
```

---

### Question 2

```text
How can you access the city field?
```

---

### Question 3

```text
Why might nested dataclasses be
better than storing everything
in a single dataclass?
```

---

## Verify Your Understanding

You should be able to explain:

- What a nested dataclass is
- How nested objects are created
- How nested attributes are accessed

You should also observe:

```text
A dataclass field can contain
another dataclass object.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

The address field is not a string.

It is an Address object.

---

### Hint 2

Use dot notation multiple times.

Example:

```python
user.address.city
```

---

### Hint 3

Dataclasses behave like normal Python objects.

One object can contain another object.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
print(user.address.country)
```

What value is returned?

---

### Experiment 2

Try:

```python
user.address.city = "Aarhus"

print(user)
```

What changes?

---

### Experiment 3

Try:

```python
@dataclass
class Company:
    name: str
    address: Address
```

Create a Company object.

Why might multiple dataclasses reuse the same Address model?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What patterns are starting to emerge?
- What do you think Python is doing behind the scenes?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about nested dataclasses?
2. How does nesting differ from using simple fields?
3. What advantages come from separating related data into multiple models?
4. When might nested dataclasses be useful in real applications?

---

## Stretch Goal

Add a third dataclass:

```python
@dataclass
class Company:
    name: str
    address: Address
```

Then create:

```text
Company
↓
Address
```

Observe how models become easier to organize as complexity grows.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User profiles
- Customer records
- Company information
- E-commerce systems
- Application configuration

Many real-world data models are naturally hierarchical.

For example:

```text
User
└── Address

Order
└── Customer

Company
└── Location

Configuration
└── Database Settings
```

Nested dataclasses allow complex structures to be built from smaller, reusable models.

This makes code easier to organize, understand, and maintain.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what a nested dataclass is
- [ ] You can access nested attributes
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/19-nested-dataclasses.py
```