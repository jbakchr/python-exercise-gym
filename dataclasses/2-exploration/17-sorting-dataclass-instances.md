# Exercise 17 - Sorting Dataclass Instances

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
✅ Exercise 14 - Immutable Dataclasses
✅ Exercise 15 - Field Customization
✅ Exercise 16 - Ordering Objects
➡️ Current Exploration Exercise
⬜ Exercise 18 - Post Initialization
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Dataclass Instances
```

can be sorted.

By the end of this exercise you should understand:

- How sorting uses dataclass ordering
- Why order=True enables sorting
- How field order affects sorted results

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass ordering
- Comparison operators
- order=True

If not, review:

```text
Exercise 16 - Ordering Objects
```

---

## Focus Area

This exercise explores:

```text
How collections of dataclass objects
can be sorted automatically.
```

Example:

```text
Products can be sorted by price.

Players can be sorted by score.

Tasks can be sorted by priority.
```

This is not a new concept.

It is a deeper look at what becomes possible once dataclass ordering has been enabled.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create multiple dataclass objects.
2. Store them in a list.
3. Sort the list.

As you work, pay attention to:

- The order before sorting
- The order after sorting
- Which fields influence the result

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass(order=True)
class Product:
    price: float
    name: str


products = [
    Product(25.0, "Keyboard"),
    Product(10.0, "Mouse"),
    Product(100.0, "Monitor"),
]

print("Before sorting:")
print(products)

products.sort()

print("After sorting:")
print(products)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Why do the products appear in a
different order after sorting?
```

---

### Question 2

```text
Which field determines the sort order?
```

---

### Question 3

```text
What happens when two products have
the same price?
```

---

## Verify Your Understanding

You should be able to explain:

- Why sorting works
- How order=True enables sorting
- Which fields are used during sorting

You should also observe:

```text
Objects are sorted according to the
same comparison rules introduced in
the previous exercise.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Sorting repeatedly compares objects.

---

### Hint 2

The comparison behavior comes from order=True.

---

### Hint 3

Remember how dataclass fields were compared in Exercise 16.

Sorting relies on exactly the same rules.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
products = [
    Product(10.0, "Keyboard"),
    Product(10.0, "Mouse"),
    Product(10.0, "Monitor"),
]
```

What determines the order now?

---

### Experiment 2

Try:

```python
sorted_products = sorted(products)

print(sorted_products)
```

How is this different from using:

```python
products.sort()
```

?

---

### Experiment 3

Try:

```python
@dataclass(order=True)
class Player:
    score: int
    name: str
```

Create multiple players and sort them.

What field controls the ordering?

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

1. What did this exercise reveal about dataclass sorting?
2. How does sorting build upon object ordering?
3. Why is field order important?
4. When might automatic sorting be useful in real applications?

---

## Stretch Goal

Create a dataclass representing tasks:

```python
@dataclass(order=True)
class Task:
    priority: int
    title: str
```

Create several tasks and sort them.

Observe how Python decides the final order.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Product catalogs
- High score tables
- To-do lists
- Customer priority queues
- Event scheduling

Many applications need collections of objects displayed in a predictable order.

For example:

```text
Cheapest products first

Highest scores first

Highest priority tasks first

Earliest deadlines first
```

Dataclass ordering allows Python's built-in sorting tools to work automatically without requiring custom comparison methods.

Understanding sorting is important because many real-world applications process collections of objects rather than individual objects.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain why sorting works
- [ ] You understand the relationship between order=True and sorting
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/17-sorting-dataclass-instances.py
```