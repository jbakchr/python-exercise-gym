# Exercise 15 - NewType

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
✅ Exercise 14 - Any
➡️ Current Exploration Exercise
⬜ Exercise 16 - NamedTuple
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
NewType
```

behaves in different situations.

By the end of this exercise you should understand:

- How NewType creates domain-specific types
- How NewType improves code readability
- How NewType helps distinguish values that share the same underlying type

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Type aliases
- Literal
- Any

If not, review:

```text
Exercise 08 - Type Aliases
Exercise 12 - Literal
Exercise 14 - Any
```

---

## Focus Area

This exercise explores:

```text
Creating meaningful types from existing types.
```

Example:

```text
UserId
OrderId
ProductId
```

Each of these may internally be an integer, but they represent different concepts.

This is not a completely new concept.

You have already used type aliases to create more descriptive names.

This exercise investigates how NewType provides stronger distinctions between similar values.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import NewType from typing
2. Create a UserId type based on int
3. Create a function that accepts a UserId
4. Display the user ID
5. Create a UserId value and pass it to the function

As you work, pay attention to:

- How NewType is defined
- How NewType differs from a type alias
- How NewType communicates intent

---

## Starter Code

```python
from typing import NewType


def display_user(user_id):
    print(f"User ID: {user_id}")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Why might UserId be more descriptive
than a plain int?
```

---

### Question 2

```text
How is NewType different from
a type alias?
```

---

### Question 3

```text
What problem is NewType trying
to solve?
```

---

## Verify Your Understanding

You should be able to explain:

- What NewType is
- Why NewType exists
- How NewType differs from TypeAlias

You should also observe:

```text
A NewType value behaves like its
underlying type at runtime.

However, type checkers treat it as
a distinct type.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

NewType is imported from:

```python
from typing import NewType
```

---

### Hint 2

A NewType is created like this:

```python
UserId = NewType("UserId", int)
```

---

### Hint 3

Creating a value looks like:

```python
user_id = UserId(123)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
OrderId = NewType("OrderId", int)
```

Create a value and compare it with UserId.

Why might keeping these types separate be useful?

---

### Experiment 2

Try:

```python
print(type(user_id))
```

What do you observe?

---

### Experiment 3

Create:

```python
CustomerId = NewType("CustomerId", int)
ProductId = NewType("ProductId", int)
```

Imagine a function that accidentally receives the wrong ID.

Why might NewType help prevent mistakes?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does NewType improve readability?
- How does NewType improve communication?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about NewType?
2. How does NewType differ from a type alias?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create additional domain-specific types:

```python
EmailAddress
AccountId
SessionId
```

Then use them in function signatures.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User identifiers
- Database record identifiers
- Account numbers
- API resource identifiers
- Domain-specific business objects

Understanding NewType matters because many systems contain values that share the same underlying type but represent different concepts.

Distinct types make code easier to understand and help prevent accidental misuse of values.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what NewType does
- [ ] You understand how it differs from a type alias
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/15-newtype.py
```