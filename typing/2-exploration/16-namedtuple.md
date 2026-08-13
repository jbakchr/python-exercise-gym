# Exercise 16 - NamedTuple

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
✅ Exercise 14 - Any
✅ Exercise 15 - NewType
➡️ Current Exploration Exercise
⬜ Exercise 17 - Type Inference
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
NamedTuple
```

behaves in different situations.

By the end of this exercise you should understand:

- How NamedTuple creates lightweight structured objects
- How NamedTuple differs from regular tuples
- How NamedTuple improves readability through named fields

---

## Previously Learned

Before starting this exercise you should already understand:

- Tuples
- Type annotations
- TypedDict
- NewType

If not, review:

```text
Exercise 06 - Lists and Collections
Exercise 11 - TypedDict
Exercise 15 - NewType
```

---

## Focus Area

This exercise explores:

```text
Giving names to tuple values.
```

Example:

Instead of:

```python
user = ("Alice", 30, "alice@example.com")
```

you can create:

```python
user.name
user.age
user.email
```

This is not a completely new concept.

You already know tuples can store related pieces of information.

This exercise investigates how NamedTuple makes that information easier to understand and access.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import NamedTuple from typing
2. Create a NamedTuple called User
3. Define the fields:
   - name (str)
   - age (int)
   - email (str)
4. Create a User instance
5. Display all values using the field names

As you work, pay attention to:

- How NamedTuple is defined
- How instances are created
- How values are accessed

---

## Starter Code

```python
from typing import NamedTuple


class User(NamedTuple):
    pass


user = None
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
How is NamedTuple different from
a regular tuple?
```

---

### Question 2

```text
How is NamedTuple similar to
a class?
```

---

### Question 3

```text
Why might named fields be easier
to understand than numeric indexes?
```

---

## Verify Your Understanding

You should be able to explain:

- What NamedTuple is
- Why NamedTuple exists
- How NamedTuple differs from a regular tuple

You should also observe:

```text
A NamedTuple behaves like a tuple
but allows values to be accessed
through meaningful field names.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

NamedTuple is imported from:

```python
from typing import NamedTuple
```

---

### Hint 2

Fields are defined inside the class body.

Example:

```python
class Person(NamedTuple):
    name: str
```

---

### Hint 3

An instance can be created like:

```python
person = Person("Alice")
```

and accessed like:

```python
print(person.name)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
print(user[0])
print(user[1])
```

What do you notice?

---

### Experiment 2

Try:

```python
name, age, email = user
```

Can a NamedTuple still be unpacked like a normal tuple?

---

### Experiment 3

Create:

```python
class Product(NamedTuple):
    name: str
    price: float
```

How does this compare to using a regular tuple?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How do named fields improve readability?
- What information becomes clearer?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about NamedTuple?
2. How does NamedTuple improve upon a regular tuple?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a NamedTuple representing:

```text
Book
```

with fields:

```text
title
author
year
```

Display the information using field names.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- API responses
- Database query results
- Configuration data
- Geographic coordinates
- Lightweight data models

Understanding NamedTuple matters because many applications need simple structured data without the overhead of creating a full class.

NamedTuple provides a readable way to group related values while preserving the simplicity of tuples.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain how NamedTuple works
- [ ] You understand how it differs from a regular tuple
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/16-namedtuple.py
```