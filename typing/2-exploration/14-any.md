# Exercise 14 - Any

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
➡️ Current Exploration Exercise
⬜ Exercise 15 - NewType
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Any
```

behaves in different situations.

By the end of this exercise you should understand:

- What Any means in a type annotation
- How Any differs from specific types
- Why Any can be both useful and dangerous

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Union types
- Literal
- Callable

If not, review:

```text
Exercise 05 - Union Types
Exercise 12 - Literal
Exercise 13 - Callable
```

---

## Focus Area

This exercise explores:

```text
Working without type restrictions.
```

Example:

```text
A function that can accept any type of value.
```

This is not a completely new idea.

You have already seen type annotations being used to make expectations more specific.

This exercise investigates what happens when those restrictions are removed.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import Any from typing
2. Write a function that accepts a value of type Any
3. Display the value
4. Call the function using different types of data

As you work, pay attention to:

- What kinds of values can be passed
- What information is lost when using Any
- How Any differs from specific annotations

---

## Starter Code

```python
from typing import Any


def display_value(value):
    print(value)


display_value("hello")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
How is Any different from str,
int, or list?
```

---

### Question 2

```text
What type-related guarantees
are lost when using Any?
```

---

### Question 3

```text
When might using Any be useful?
```

---

## Verify Your Understanding

You should be able to explain:

- What Any means
- Why Any exists
- The trade-offs involved when using Any

You should also observe:

```text
Any disables many of the benefits
normally provided by type annotations.

Almost any operation becomes acceptable
from the perspective of a type checker.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Any is imported from:

```python
from typing import Any
```

---

### Hint 2

A parameter can be annotated as:

```python
def example(value: Any) -> None:
    ...
```

---

### Hint 3

Try calling your function with:

```python
"A string"

123

3.14

["a", "b", "c"]

{"name": "Alice"}
```

Observe what happens.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
display_value("hello")
display_value(42)
display_value(True)
```

What changes?

---

### Experiment 2

Try:

```python
display_value(["apple", "orange"])
display_value({"name": "Alice"})
```

What stays the same?

---

### Experiment 3

Create two functions:

```python
def process_text(text: str) -> None:
    ...

def process_anything(value: Any) -> None:
    ...
```

Compare them.

Which function communicates more information?

Why?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What information is preserved by specific types?
- What information is lost when using Any?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about Any?
2. How does Any differ from other type annotations?
3. What patterns do you notice?
4. When might this be useful in real code?
5. When might it be harmful?

---

## Stretch Goal

Write two versions of the same function:

```text
Version 1:
Uses Any

Version 2:
Uses specific type annotations
```

Compare the readability of each.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Interacting with third-party libraries
- Working with dynamic data
- Gradually adding typing to older codebases
- Prototyping and experimentation
- Legacy systems

Understanding Any matters because it provides flexibility when precise type information is unavailable.

However, overusing Any can remove many of the benefits that type annotations provide.

Learning when to avoid Any is often just as important as learning when to use it.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what Any means
- [ ] You understand the trade-offs of using Any
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/14-any.py
```