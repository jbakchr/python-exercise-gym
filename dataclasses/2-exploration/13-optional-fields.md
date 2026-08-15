# Exercise 13 - Optional Fields

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
➡️ Current Exploration Exercise
⬜ Exercise 14 - Frozen Dataclasses
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Optional fields
```

behave in dataclasses.

By the end of this exercise you should understand:

- How a field can intentionally have no value
- How Optional communicates that a value may be missing
- How None is commonly used in dataclass models

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Default values
- Type annotations

If not, review:

```text
Exercise 12 - Default Factories
```

---

## Focus Area

This exercise explores:

```text
Fields that may or may not contain a value.
```

Example:

```text
A user account may have a phone number.

Some users provide one.

Others do not.
```

This is not a new concept.

It is a deeper look at how dataclasses model incomplete or optional information.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create dataclass objects with missing values.
2. Create dataclass objects with supplied values.
3. Observe how Optional fields behave.

As you work, pay attention to:

- When None is used
- When a real value is present
- How Optional communicates intent

---

## Starter Code

```python
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    email: Optional[str] = None


user1 = User("alice")
user2 = User("bob", "bob@example.com")

print(user1)
print(user2)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What value does email contain when
no value is provided?
```

---

### Question 2

```text
Why is Optional[str] being used instead
of just str?
```

---

### Question 3

```text
What changes when an email address
is supplied?
```

---

## Verify Your Understanding

You should be able to explain:

- What Optional means
- Why None is commonly used as a default value
- When optional fields are useful

You should also observe:

```text
The email field can safely contain
either a string or None.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look at the value of email for each object.

---

### Hint 2

None is often used when information is not yet available.

---

### Hint 3

Optional[str] means:

```text
str or None
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
user = User("charlie")

print(user.email)
```

What value is displayed?

---

### Experiment 2

Try:

```python
user = User(
    "diana",
    "diana@example.com"
)

print(user.email)
```

What changes?

---

### Experiment 3

Try:

```python
user = User(
    username="erik",
    email=None
)

print(user)
```

Why is this allowed?

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

1. What did this exercise reveal about Optional fields?
2. How does this behavior relate to default values?
3. What patterns do you notice when modelling incomplete data?
4. When might Optional fields be useful in real applications?

---

## Stretch Goal

Add another optional field:

```python
phone_number: Optional[str] = None
```

Create several users with different combinations of missing information.

Observe how the dataclass behaves.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User profiles
- Customer records
- Product information
- Application settings
- API responses

Many real-world data models contain information that is not always available.

For example:

```text
A user may not provide a phone number.

A customer may not have supplied an address.

An API response may omit optional fields.
```

Understanding Optional fields helps you build realistic data models that accurately represent incomplete or missing information.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what Optional means
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/13-optional-fields.py
```