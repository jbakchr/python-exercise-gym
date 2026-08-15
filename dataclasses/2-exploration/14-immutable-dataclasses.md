# Exercise 14 - Immutable Dataclasses

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
➡️ Current Exploration Exercise
⬜ Exercise 15 - Field Customization
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Immutable Dataclasses
```

behave in different situations.

By the end of this exercise you should understand:

- How frozen dataclasses prevent modification
- What happens when you try to change a field
- When immutable objects are useful

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Default values
- Optional fields

If not, review:

```text
Exercise 13 - Optional Fields
```

---

## Focus Area

This exercise explores:

```text
How a dataclass behaves when it is
marked as frozen.
```

Example:

```text
A configuration object should not be
modified after it is created.
```

This is not a new concept.

It is a deeper look at controlling how dataclass objects can be used.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a frozen dataclass.
2. Create an object from it.
3. Attempt to modify one of its fields.

As you work, pay attention to:

- What operations succeed
- What operations fail
- The error that Python produces

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Configuration:
    environment: str
    debug: bool


config = Configuration(
    environment="production",
    debug=False,
)

print(config)

config.debug = True
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What happens when you try to assign
a new value to debug?
```

---

### Question 2

```text
Why does Python prevent the change?
```

---

### Question 3

```text
What changes if frozen=True is removed?
```

---

## Verify Your Understanding

You should be able to explain:

- What frozen=True does
- Why field assignment is blocked
- The difference between mutable and immutable dataclasses

You should also observe:

```text
Dataclass fields cannot be reassigned
after object creation when frozen=True
is used.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look closely at the exception raised by Python.

---

### Hint 2

The object itself is being protected from modification.

---

### Hint 3

The @dataclass decorator changes how attribute assignment behaves when frozen=True is enabled.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
@dataclass(frozen=True)
class User:
    username: str
```

Create a user and attempt to change the username.

What happens?

---

### Experiment 2

Try:

```python
@dataclass
class User:
    username: str
```

Remove frozen=True and repeat the assignment.

What changes?

---

### Experiment 3

Try:

```python
config = Configuration(
    environment="development",
    debug=True,
)

print(config)
```

Can you still create different objects?

Why do you think this is allowed?

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

1. What did this exercise reveal about frozen dataclasses?
2. How does immutability differ from using default values or Optional fields?
3. What benefits might immutability provide?
4. When might immutable objects be useful in real applications?

---

## Stretch Goal

Create a frozen dataclass representing application settings.

Example:

```python
@dataclass(frozen=True)
class Settings:
    app_name: str
    version: str
```

Create an object and investigate what modifications are allowed and which are prevented.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Application configuration
- Environment settings
- Domain models
- Financial records
- Audit data

Many types of data should not change after they are created.

For example:

```text
A completed invoice should not be modified.

Application settings may be treated as read-only.

A historical audit record should remain unchanged.
```

Understanding immutable dataclasses helps you build safer models and reduces the risk of accidental changes to important application data.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what frozen=True does
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/14-immutable-dataclasses.py
```