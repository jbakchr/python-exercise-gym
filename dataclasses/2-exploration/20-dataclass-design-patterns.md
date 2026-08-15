# Exercise 20 - Dataclass Design Patterns

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
✅ Exercise 19 - Nested Dataclasses
➡️ Current Exploration Exercise
✅ Exploration Stage Complete
```

---

## Goal

Explore how:

```text
Multiple Dataclass Features
```

can be combined into practical application models.

By the end of this exercise you should understand:

- How several dataclass features can work together
- Why different fields are designed differently
- How dataclasses can model realistic application data

---

## Previously Learned

Before starting this exercise you should already understand:

- Default values
- Default factories
- Optional fields
- Immutable dataclasses
- Field customization
- Object ordering
- Post initialization
- Nested dataclasses

If not, review:

```text
Exercise 19 - Nested Dataclasses
```

---

## Focus Area

This exercise explores:

```text
How multiple dataclass features can
work together within a single model.
```

Example:

```text
A user profile may contain:

Required fields
Optional fields

Nested dataclasses

Automatically generated values

Collections
```

This is not a new concept.

It is a deeper look at how dataclasses are designed in real-world applications.

---

## Challenge

Investigate the following design.

Your task is to:

1. Create the dataclass objects.
2. Examine how the model is structured.
3. Identify which dataclass features are being used.
4. Explain why each design decision might be useful.

As you work, pay attention to:

- Required fields
- Optional fields
- Nested models
- Collection fields
- Post-initialization processing

---

## Starter Code

```python
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    city: str
    country: str


@dataclass
class UserProfile:
    username: str
    address: Address
    email: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.username = self.username.strip().lower()


address = Address(
    city="Copenhagen",
    country="Denmark",
)

user = UserProfile(
    username="  Alice  ",
    address=address,
)

print(user)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Which fields are required?
```

---

### Question 2

```text
Which fields are optional?
```

---

### Question 3

```text
Which field uses a default factory?
```

---

### Question 4

```text
How is nesting being used?
```

---

### Question 5

```text
What role does __post_init__
play in this model?
```

---

## Verify Your Understanding

You should be able to explain:

- Why Address is its own dataclass
- Why email uses Optional
- Why tags uses default_factory
- Why username is normalized in __post_init__

You should also observe:

```text
Multiple dataclass features can work
together naturally within a single
application model.
```

Avoid checking the solution until you can explain why these design decisions were made.

---

## Hints

### Hint 1

Try identifying features from previous exercises.

---

### Hint 2

Ask yourself:

```text
Which exercise introduced this feature?
```

for each field and behavior.

---

### Hint 3

This exercise is about understanding design choices.

Not just syntax.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
user = UserProfile(
    username="Bob",
    address=address,
    email="bob@example.com",
)
```

What changes?

---

### Experiment 2

Try:

```python
user.tags.append("python")

print(user)
```

Why does this work even though no tags were provided originally?

---

### Experiment 3

Try:

```python
address2 = Address(
    city="Aarhus",
    country="Denmark",
)

user2 = UserProfile(
    username="Charlie",
    address=address2,
)
```

What parts of the model are reusable?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- Which dataclass feature seems most useful?
- Which feature appears most often in realistic models?
- How would this design scale as an application grows?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about dataclass design?
2. Which features combine particularly well?
3. Why are nested models useful?
4. How do dataclasses reduce boilerplate code?
5. Which feature from the Exploration stage do you think will be most useful in future projects?

---

## Stretch Goal

Design your own application model using at least:

```text
One nested dataclass

One Optional field

One default_factory

One __post_init__ method
```

Possible ideas:

```text
Customer Profile

Employee Record

Project Information

Order System

Game Character
```

The goal is not to build something larger.

The goal is to practice design decisions.

---

## Real-World Connection

This behavior appears in situations such as:

- User management systems
- Customer databases
- Application configuration
- E-commerce platforms
- API request and response models

Real-world dataclass usage rarely involves a single feature.

Instead, developers combine features to create models that are:

```text
Readable

Maintainable

Reusable

Predictable

Easy to extend
```

Understanding how these features work together is an important step toward designing real application data models.

This exercise serves as a bridge into the Manipulation stage, where dataclasses will be used to build practical tools and reusable application structures.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You identified every dataclass feature being used
- [ ] You can explain why each feature was chosen
- [ ] You explored at least one variation
- [ ] You feel comfortable designing your own dataclass models
- [ ] You can recognize dataclass design patterns in real code

---

## Solution

See:

```text
solutions/20-dataclass-design-patterns.py
```