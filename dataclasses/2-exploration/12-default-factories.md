# Exercise 12 - Default Factories

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
➡️ Current Exploration Exercise
⬜ Exercise 13 - Optional Fields
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
default_factory
```

behaves in dataclasses.

By the end of this exercise you should understand:

- Why normal defaults do not work well for mutable objects
- How default_factory creates new values for each object
- When default_factory should be preferred over a regular default

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Dataclass default values
- Creating dataclass objects

If not, review:

```text
Exercise 11 - Default Values Revisited
```

---

## Focus Area

This exercise explores:

```text
How dataclasses create default values for
mutable objects such as lists.
```

Example:

```text
Every new object may need its own list.
```

This is not a new concept.

It is a deeper look at how dataclass defaults are created and assigned.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create multiple dataclass objects.
2. Add data to one object's list.
3. Observe whether the other objects are affected.

As you work, pay attention to:

- Whether lists are shared
- Whether lists are independent
- When a new list is created

---

## Starter Code

```python
from dataclasses import dataclass, field


@dataclass
class ShoppingCart:
    items: list[str] = field(default_factory=list)


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.items.append("Laptop")

print(cart1)
print(cart2)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What happens when an item is added to cart1?
```

---

### Question 2

```text
Why does cart2 remain unchanged?
```

---

### Question 3

```text
What would happen if both objects shared
the same list?
```

---

## Verify Your Understanding

You should be able to explain:

- What default_factory does
- Why mutable defaults are handled differently
- Why each object receives its own list

You should also observe:

```text
Each ShoppingCart object receives a
separate list even though no list was
provided during object creation.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look carefully at the contents of both carts after appending an item.

---

### Hint 2

Ask yourself whether cart1.items and cart2.items refer to the same list.

---

### Hint 3

default_factory creates a new object every time a dataclass instance is created.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
cart1.items.append("Mouse")

print(cart1)
print(cart2)
```

What changes?

---

### Experiment 2

Try:

```python
cart2.items.append("Keyboard")

print(cart1)
print(cart2)
```

What stays independent?

---

### Experiment 3

Try:

```python
cart3 = ShoppingCart()

print(cart3)
```

Why does the new cart start with its own empty list?

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

1. What problem does default_factory solve?
2. How does it differ from a normal default value?
3. What patterns do you notice when using mutable objects?
4. When might this be useful in real applications?

---

## Stretch Goal

Modify the dataclass so that each cart starts with a default category list.

Example:

```python
field(default_factory=lambda: ["General"])
```

Observe how newly created objects behave.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Shopping carts
- User permissions
- Configuration settings
- API response collections
- Task lists

Many applications need collections that belong to a specific object.

For example:

```text
Each user should have their own list of roles.

Each project should have its own list of tasks.

Each order should have its own list of products.
```

Understanding default_factory helps prevent accidental data sharing between objects and makes application models more predictable.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain why default_factory exists
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/12-default-factories.py
```