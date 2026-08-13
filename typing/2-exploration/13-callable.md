# Exercise 13 - Callable

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
➡️ Current Exploration Exercise
⬜ Exercise 14 - Any
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Callable
```

behaves in different situations.

By the end of this exercise you should understand:

- How to annotate functions that accept other functions
- How Callable describes function signatures
- How Callable makes function-based APIs easier to understand

---

## Previously Learned

Before starting this exercise you should already understand:

- Function annotations
- Return type annotations
- Basic typing concepts

If not, review:

```text
Exercise 02 - Return Types
Exercise 09 - Annotating Real Functions
```

---

## Focus Area

This exercise explores:

```text
Describing functions as values.
```

Example:

```text
A function that accepts another function
and executes it.
```

This is not a completely new concept.

Python functions are objects and can be passed around just like any other value.

This exercise investigates how Python's typing system can describe those function relationships.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import Callable from typing
2. Create a function that accepts another function
3. Use Callable to describe the expected function signature
4. Call the provided function and display its result

As you work, pay attention to:

- How Callable describes parameters
- How Callable describes return types
- How function annotations become more expressive

---

## Starter Code

```python
from typing import Callable


def greet(name: str) -> str:
    return f"Hello, {name}"


def run_function(func, name):
    pass


run_function(greet, "Alice")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What information does Callable
provide about a function?
```

---

### Question 2

```text
Why is Callable more useful than
simply writing "function" in a comment?
```

---

### Question 3

```text
How does Callable help another
developer understand your code?
```

---

## Verify Your Understanding

You should be able to explain:

- What Callable is
- How Callable describes a function signature
- Why parameter and return types are important

You should also observe:

```text
Callable allows type annotations to
describe both the inputs and outputs
of functions being passed around.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Callable is imported from:

```python
from typing import Callable
```

---

### Hint 2

Callable describes:

```text
Parameter types
↓
Return type
```

---

### Hint 3

A Callable annotation looks like:

```python
Callable[[str], str]
```

This means:

```text
Accepts:
    str

Returns:
    str
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
def shout(name: str) -> str:
    return name.upper()
```

Pass it into your function.

What changes?

---

### Experiment 2

Try:

```python
def goodbye(name: str) -> str:
    return f"Goodbye, {name}"
```

What stays the same?

---

### Experiment 3

Try:

```python
def get_length(text: str) -> int:
    return len(text)
```

What is different about this function?

How would the Callable annotation need to change?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does Callable improve readability?
- What assumptions become explicit?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about Callable?
2. Why is describing function signatures useful?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a function that accepts:

```text
A function that receives an integer
and returns a boolean
```

Use Callable to annotate the parameter correctly.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Callback functions
- Event handlers
- Sorting and filtering operations
- Data processing pipelines
- Framework and library APIs

Understanding Callable matters because functions are frequently passed between components in modern Python applications.

Callable makes those relationships explicit and easier to understand.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain how Callable works
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/13-callable.py
```