# Exercise 16 - Ordering Objects

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
✅ Exercise 14 - Immutable Dataclasses
✅ Exercise 15 - Field Customization
➡️ Current Exploration Exercise
⬜ Exercise 17 - Sorting Dataclass Instances
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Dataclass Object Ordering
```

behaves in different situations.

By the end of this exercise you should understand:

- How dataclasses can be compared using ordering operators
- How order=True generates comparison methods
- Which fields Python uses when comparing objects

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Equality comparisons
- Field customization

If not, review:

```text
Exercise 15 - Field Customization
```

---

## Focus Area

This exercise explores:

```text
How dataclass objects can be compared
using operators such as <, <=, >, and >=.
```

Example:

```text
One product may be considered
"less than" another product.
```

This is not a new concept.

It is a deeper look at how dataclasses automatically generate comparison behavior.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a dataclass with order=True.
2. Create several objects.
3. Compare the objects using comparison operators.

As you work, pay attention to:

- Which comparisons succeed
- Which fields affect the result
- The order in which fields are evaluated

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass(order=True)
class Product:
    price: float
    name: str


product1 = Product(
    price=10.0,
    name="Mouse",
)

product2 = Product(
    price=20.0,
    name="Keyboard",
)

print(product1 < product2)
print(product1 > product2)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Why is product1 considered
less than product2?
```

---

### Question 2

```text
Which field is being compared first?
```

---

### Question 3

```text
What happens when the prices
are identical?
```

---

## Verify Your Understanding

You should be able to explain:

- What order=True does
- How dataclass ordering works
- Which fields participate in comparisons

You should also observe:

```text
Dataclasses compare fields in
the order they are defined.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look at the order of fields in the class definition.

---

### Hint 2

Dataclasses compare field values one at a time.

---

### Hint 3

If the first field is equal, Python moves to the next field.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
product1 = Product(
    price=20.0,
    name="Mouse",
)

product2 = Product(
    price=20.0,
    name="Keyboard",
)
```

What comparison result do you observe?

---

### Experiment 2

Try:

```python
print(product1 <= product2)
print(product1 >= product2)
```

What new comparison methods are available?

---

### Experiment 3

Try:

```python
@dataclass(order=True)
class Player:
    score: int
    name: str
```

Create multiple players and compare them.

Why do you think the field order matters?

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

1. What did this exercise reveal about ordering?
2. How does ordering differ from equality comparison?
3. Why might field order be important?
4. When might object ordering be useful in real applications?

---

## Stretch Goal

Create a dataclass representing a game score:

```python
@dataclass(order=True)
class Score:
    points: int
    player: str
```

Create multiple Score objects and investigate how comparisons are performed.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Product pricing
- Rankings
- Leaderboards
- Customer priorities
- Task scheduling

Many applications need objects that can be compared and ranked.

For example:

```text
The cheapest product

The highest score

The highest priority task

The earliest deadline
```

Dataclass ordering allows Python to automatically generate comparison methods, reducing boilerplate code and making models easier to work with.

Understanding ordering is important because the next exercise will explore how ordering enables collections of dataclass objects to be sorted.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what order=True does
- [ ] You understand how fields are compared
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/16-ordering-objects.py
```