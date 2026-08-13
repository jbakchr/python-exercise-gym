# Exercise 11 - TypedDict

## Progression

```text
✅ Foundations Complete
➡️ Current Exploration Exercise
⬜ Exercise 12 - Literal
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
TypedDict
```

behaves in different situations.

By the end of this exercise you should understand:

- How TypedDict describes dictionary structure
- How TypedDict improves readability compared to plain dict annotations
- How TypedDict helps communicate expected data shapes

---

## Previously Learned

Before starting this exercise you should already understand:

- Dictionary type annotations
- Nested dictionaries
- Type aliases

If not, review:

```text
Exercise 07 - Dictionaries and Nested Structures
Exercise 08 - Type Aliases
```

---

## Focus Area

This exercise explores:

```text
Describing the structure of dictionaries with TypedDict.
```

Example:

```text
A user dictionary that is expected to contain
specific keys and value types.
```

This is not a completely new idea.

You already know how to annotate dictionaries.

This exercise investigates how Python's typing system can describe dictionary structure more precisely.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a TypedDict named `User`
2. Define the required fields:
   - name (str)
   - age (int)
   - email (str)
3. Create a user dictionary using the TypedDict
4. Write a function that accepts a User and displays its information

As you work, pay attention to:

- How TypedDict definitions resemble class definitions
- How TypedDict differs from a normal dict annotation
- How TypedDict makes expected data structures clearer

---

## Starter Code

```python
from typing import TypedDict


class User(TypedDict):
    pass


def display_user(user):
    pass


user = {}
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What information can TypedDict describe that
dict[str, object] cannot?
```

---

### Question 2

```text
Why might TypedDict be easier to understand
than nested dictionary annotations?
```

---

### Question 3

```text
What changes if a required key is missing?
```

---

## Verify Your Understanding

You should be able to explain:

- What TypedDict is
- Why TypedDict exists
- How TypedDict differs from ordinary dictionary annotations

You should also observe:

```text
The dictionary behaves like a normal dictionary
at runtime, but provides additional type
information for developers and type checkers.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

TypedDict is imported from:

```python
from typing import TypedDict
```

---

### Hint 2

Fields are defined inside the TypedDict class body.

Example:

```python
class Example(TypedDict):
    name: str
```

---

### Hint 3

Creating an instance looks exactly like creating a normal dictionary.

```python
user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
user = {
    "name": "Alice",
    "age": 30
}
```

What changes?

---

### Experiment 2

Try:

```python
user = {
    "name": "Alice",
    "age": "30",
    "email": "alice@example.com"
}
```

What stays the same?

What would a type checker say?

---

### Experiment 3

Try:

```python
user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "country": "Denmark"
}
```

Why do you think this happens?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does TypedDict improve readability?
- What information is being communicated to other developers?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about TypedDict?
2. How does TypedDict improve upon ordinary dictionary annotations?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a second TypedDict:

```python
Product
```

with fields:

```text
name
price
stock
```

Then write a function that accepts a Product and displays its information.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- API request and response data
- Configuration files
- JSON-like application data

Understanding TypedDict matters because many applications pass structured dictionaries between functions, services, and systems.

TypedDict helps developers understand exactly what data is expected without reading implementation details.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain why TypedDict exists
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/11-typeddict.py
```