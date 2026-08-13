# Exercise 20 - Advanced Annotation Patterns

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
✅ Exercise 14 - Any
✅ Exercise 15 - NewType
✅ Exercise 16 - NamedTuple
✅ Exercise 17 - Type Inference
✅ Exercise 18 - Type Narrowing
✅ Exercise 19 - Self
➡️ Current Exploration Exercise
✅ Final Exploration Exercise
```

---

## Goal

Explore how:

```text
Multiple typing features
```

can be combined to create more expressive type annotations.

By the end of this exercise you should understand:

- How different typing tools work together
- How annotations can model both data and behavior
- How modern Python projects combine typing features

---

## Previously Learned

Before starting this exercise you should already understand:

- TypedDict
- Literal
- Callable
- NewType
- NamedTuple
- Type Inference
- Type Narrowing
- Self

If not, review:

```text
Exercises 11-19
```

---

## Focus Area

This exercise explores:

```text
Combining multiple typing features
in a single design.
```

Example:

```text
A user record described by TypedDict
that contains a Literal status and
uses a NewType identifier.
```

This is not introducing a completely new typing feature.

Instead, this exercise investigates how the pieces you have learned can work together.

The goal is to begin thinking like a developer designing typed systems rather than a learner practicing individual annotations.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a UserId using NewType
2. Create a User TypedDict
3. Use Literal to restrict the user's status
4. Write a function that accepts a User
5. Display the user's information

As you work, pay attention to:

- How each typing tool contributes different information
- How readability changes as annotations become more descriptive
- How the overall design becomes easier to understand

---

## Starter Code

```python
from typing import Literal, NewType, TypedDict


UserId = NewType("UserId", int)


class User(TypedDict):
    pass


def display_user(user):
    pass
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What problem does each annotation
solve individually?
```

---

### Question 2

```text
How do these annotations become
more valuable when combined?
```

---

### Question 3

```text
Does the code communicate more
information than basic annotations?
```

---

## Verify Your Understanding

You should be able to explain:

- Why TypedDict is useful
- Why Literal is useful
- Why NewType is useful
- How multiple typing tools can be used together

You should also observe:

```text
Typing features are most powerful
when they communicate different
parts of a design.

Some describe structure.

Some describe valid values.

Some describe meaning.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Create a custom identifier type:

```python
UserId = NewType("UserId", int)
```

---

### Hint 2

A status field might use:

```python
Literal["active", "inactive"]
```

---

### Hint 3

Combine both concepts inside a TypedDict.

```python
class User(TypedDict):
    ...
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Add another status option:

```python
Literal[
    "active",
    "inactive",
    "suspended",
]
```

What changes?

---

### Experiment 2

Create another identifier type:

```python
OrderId = NewType("OrderId", int)
```

Why might this be useful?

---

### Experiment 3

Create a second TypedDict:

```python
Product
```

using:

```text
NewType
+
Literal
```

What patterns do you notice?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- Which annotation provided the most value?
- How did multiple annotations work together?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about advanced annotation patterns?
2. Which typing feature did you find most useful?
3. How do multiple typing tools complement each other?
4. When might these combinations be useful in real code?

---

## Stretch Goal

Extend the exercise by adding:

```text
Callable
```

to process User objects.

For example:

```text
A function that accepts a User
and another function that performs
an action on that User.
```

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Web APIs
- Configuration systems
- Data validation workflows
- Application models
- Service integrations

Understanding advanced annotation patterns matters because professional Python code rarely uses typing features in isolation.

Instead, developers combine multiple typing tools to communicate:

```text
Structure
+
Meaning
+
Constraints
+
Behavior
```

The result is code that is easier to understand, easier to maintain, and easier to use correctly.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed how multiple typing tools work together
- [ ] You can explain the role of each annotation
- [ ] You explored at least one variation
- [ ] You feel comfortable combining typing features in your own code

---

## Solution

See:

```text
solutions/20-advanced-annotation-patterns.py
```