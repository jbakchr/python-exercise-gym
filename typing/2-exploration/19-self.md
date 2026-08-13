# Exercise 19 - Self

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
➡️ Current Exploration Exercise
⬜ Exercise 20 - Advanced Annotation Patterns
```

---

## Goal

Explore how:

```text
Self
```

behaves in different situations.

By the end of this exercise you should understand:

- What Self represents
- Why Self is useful in class methods
- How Self improves method return annotations

---

## Previously Learned

Before starting this exercise you should already understand:

- Classes
- Methods
- Return type annotations
- Type inference

If not, review:

```text
Exercise 02 - Return Types
Exercise 09 - Annotating Real Functions
```

---

## Focus Area

This exercise explores:

```text
Referring to the current class type.
```

Example:

```python
class User:
    def update_name(self, name: str) -> Self:
        ...
```

The method returns:

```text
The same type as the current object.
```

This is not a new object-oriented programming concept.

Instead, this exercise investigates how Python's typing system can express relationships between methods and the objects they return.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import Self from typing
2. Create a User class
3. Add a method that updates the user's name
4. Return self from the method
5. Annotate the return type using Self

As you work, pay attention to:

- What Self refers to
- Why returning self is useful
- How method annotations become clearer

---

## Starter Code

```python
from typing import Self


class User:
    def __init__(self, name: str):
        self.name = name

    def update_name(self, name: str):
        pass
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What does Self represent
inside a class?
```

---

### Question 2

```text
Why might Self be more useful
than writing the class name
directly?
```

---

### Question 3

```text
What relationship exists between
the returned value and the current
object instance?
```

---

## Verify Your Understanding

You should be able to explain:

- What Self is
- Why Self exists
- When Self should be used

You should also observe:

```text
Self represents the current class.

Methods that return the current object
can use Self to express that relationship.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Self is imported from:

```python
from typing import Self
```

---

### Hint 2

A method can return itself:

```python
return self
```

---

### Hint 3

A return annotation might look like:

```python
def update_name(self, name: str) -> Self:
    ...
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try creating another method:

```python
def update_email(self, email: str) -> Self:
    ...
```

What benefit does returning Self provide?

---

### Experiment 2

Try:

```python
user.update_name("Bob").update_name("Charlie")
```

What becomes possible?

---

### Experiment 3

Replace:

```python
-> Self
```

with:

```python
-> User
```

How does this compare?

Why might Self be preferred?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does Self improve readability?
- What information is being communicated?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about Self?
2. How does Self differ from writing the class name directly?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a class:

```python
Product
```

with a method:

```python
update_price()
```

that returns Self.

Experiment with method chaining.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Builder patterns
- Fluent APIs
- Configuration objects
- Query builders
- Data model classes

Understanding Self matters because many modern Python APIs return the current object to support chaining operations while preserving accurate type information.

Self allows type annotations to express that relationship clearly.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what Self represents
- [ ] You understand when Self should be used
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/19-self.py
```