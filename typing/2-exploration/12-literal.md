# Exercise 12 - Literal

## Progression

```text
✅ Exercise 11 - TypedDict
➡️ Current Exploration Exercise
⬜ Exercise 13 - Callable
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Literal
```

behaves in different situations.

By the end of this exercise you should understand:

- How Literal restricts values to a predefined set
- How Literal communicates valid choices to developers
- How Literal improves type safety compared to plain strings

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Union types
- TypedDict

If not, review:

```text
Exercise 05 - Union Types
Exercise 11 - TypedDict
```

---

## Focus Area

This exercise explores:

```text
Restricting values to specific allowed options.
```

Example:

```text
A function that only accepts:

"pending"
"approved"
"rejected"

instead of any string.
```

This is not a new concept.

You already know how to annotate strings.

This exercise investigates how Python's typing system can describe exactly which string values are allowed.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import Literal from typing
2. Create a type annotation that allows only:
   - "pending"
   - "approved"
   - "rejected"
3. Write a function that accepts one of these values
4. Display the status inside the function

As you work, pay attention to:

- How Literal differs from str
- How Literal documents valid values
- How Literal can prevent invalid inputs

---

## Starter Code

```python
from typing import Literal


def display_status(status):
    print(f"Status: {status}")


display_status("pending")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What can Literal express that a normal
str annotation cannot?
```

---

### Question 2

```text
Why might Literal be preferable to
writing comments that list valid values?
```

---

### Question 3

```text
What happens when an unexpected value
is provided?
```

---

## Verify Your Understanding

You should be able to explain:

- What Literal is
- Why Literal exists
- When Literal is more useful than a normal type annotation

You should also observe:

```text
Literal does not change runtime behavior.

Its primary purpose is to communicate
allowed values to developers and
type-checking tools.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Literal is imported from:

```python
from typing import Literal
```

---

### Hint 2

A Literal annotation can specify exact values.

Example:

```python
Literal["yes", "no"]
```

---

### Hint 3

A function signature might look like:

```python
def example(value: Literal["a", "b"]) -> None:
    ...
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
display_status("approved")
display_status("rejected")
```

What changes?

---

### Experiment 2

Try:

```python
display_status("unknown")
```

What happens at runtime?

What would a type checker say?

---

### Experiment 3

Try:

```python
Priority = Literal["low", "medium", "high"]
```

Create a function that uses this type.

Why might this be useful?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does Literal improve readability?
- What assumptions become explicit?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about Literal?
2. How does Literal improve upon a plain string annotation?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a function that accepts:

```text
"development"
"testing"
"production"
```

using Literal.

Then display a message based on the selected environment.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Application environments
- User roles
- Configuration settings
- Status values
- API request parameters

Understanding Literal matters because many systems only allow a small set of valid values.

Literal makes those restrictions visible directly in the type annotations.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain why Literal exists
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/12-literal.py
```
