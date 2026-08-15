# Exercise 15 - Field Customization

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
✅ Exercise 14 - Immutable Dataclasses
➡️ Current Exploration Exercise
⬜ Exercise 16 - Ordering Objects
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
field()
```

can be used to customize dataclass fields.

By the end of this exercise you should understand:

- How field() changes field behavior
- How fields can be excluded from representations
- How customization affects generated dataclass methods

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Default values
- Default factories
- Immutable dataclasses

If not, review:

```text
Exercise 14 - Immutable Dataclasses
```

---

## Focus Area

This exercise explores:

```text
Customizing individual dataclass fields
using field().
```

Example:

```text
Some fields may be important for storage
but should not appear when the object is
printed.
```

This is not a new concept.

It is a deeper look at controlling how dataclass fields participate in automatically generated behavior.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a dataclass using field().
2. Print the created object.
3. Observe which fields appear in the output.

As you work, pay attention to:

- Which fields are displayed
- Which fields are hidden
- How field customization changes generated behavior

---

## Starter Code

```python
from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str = field(repr=False)


user = User(
    username="alice",
    password="secret123",
)

print(user)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What happens when the User object
is printed?
```

---

### Question 2

```text
Why does the password field not appear
in the output?
```

---

### Question 3

```text
What changes if repr=False is removed?
```

---

## Verify Your Understanding

You should be able to explain:

- What field() does
- What repr=False means
- Why certain fields may be hidden

You should also observe:

```text
The password value exists on the object
but is excluded from the generated string
representation.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

The password field still exists.

Only its representation is changing.

---

### Hint 2

Look closely at the output produced by print().

---

### Hint 3

repr=False affects the generated __repr__()
method created by the dataclass.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
print(user.password)
```

What happens?

---

### Experiment 2

Try:

```python
password: str
```

Remove the field() customization completely.

What changes in the printed output?

---

### Experiment 3

Try:

```python
@dataclass
class ApiKey:
    name: str
    secret: str = field(repr=False)
```

Create an object and print it.

Why might this behavior be useful?

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

1. What did this exercise reveal about field customization?
2. How does field() differ from regular field definitions?
3. What benefits does repr=False provide?
4. When might this be useful in real applications?

---

## Stretch Goal

Research another option supported by field().

Examples include:

```python
compare=False
init=False
default_factory=...
```

Experiment with one of them and observe the resulting behavior.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User accounts
- API credentials
- Authentication systems
- Configuration management
- Security-sensitive applications

Many applications contain fields that should not be displayed when objects are printed.

For example:

```text
Passwords

Access tokens

API secrets

Private keys
```

Field customization allows dataclass models to expose useful information while hiding sensitive or irrelevant details.

Understanding field() is important because many advanced dataclass features are built upon it.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what field() does
- [ ] You understand repr=False
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/15-field-customization.py
```