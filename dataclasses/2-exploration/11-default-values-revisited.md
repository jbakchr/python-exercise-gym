# Exercise 11 - Default Values Revisited

## Progression

```text
✅ Foundations Complete
➡️ Current Exploration Exercise
⬜ Exercise 12 - Default Factories
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Dataclass Default Values
```

behave in different situations.

By the end of this exercise you should understand:

- How default values are assigned to dataclass fields
- When defaults are used
- How provided values override defaults
- The limitations of simple default values

---

## Previously Learned

Before starting this exercise you should already understand:

- Creating dataclasses
- Defining fields
- Creating dataclass instances
- Using default values

If not, review:

```text
Exercise 09 - Using Default Values
```

---

## Focus Area

This exercise explores:

```text
How dataclass fields behave when some values
are provided and others rely on defaults.
```

Example:

```text
A field with a default value is used only
when no value is supplied during object creation.
```

This is not a new concept.

It is a deeper look at a concept you already know.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create several instances of the same dataclass.
2. Provide different combinations of field values.
3. Observe which values come from defaults and which come from constructor arguments.

As you work, pay attention to:

- Which fields use defaults
- Which fields use supplied values
- How Python decides which value to assign

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass
class User:
    username: str
    role: str = "member"
    active: bool = True


user1 = User("alice")
user2 = User("bob", "admin")
user3 = User("charlie", "moderator", False)

print(user1)
print(user2)
print(user3)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Which values come from the dataclass defaults?
```

---

### Question 2

```text
What happens when a value is supplied for a field
that already has a default?
```

---

### Question 3

```text
Can some fields use defaults while others use
provided values?
```

---

## Verify Your Understanding

You should be able to explain:

- How default values are assigned
- How supplied values override defaults
- Why dataclass defaults make object creation easier

You should also observe:

```text
Fields with defaults are only used when
no value is provided during object creation.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look at each object separately.

Which values were explicitly provided?

---

### Hint 2

Compare the constructor arguments with the printed output.

---

### Hint 3

A default value acts as a fallback.

If you supply a value yourself, Python uses that value instead.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
user = User("diana", active=False)

print(user)
```

What changes?

---

### Experiment 2

Try:

```python
user = User(
    username="erik",
    role="manager"
)

print(user)
```

What stays the same?

---

### Experiment 3

Try:

```python
user = User(
    username="frank",
    role="owner",
    active=True,
)

print(user)
```

Are any defaults still being used?

Why do you think this happens?

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

1. What did this exercise reveal about default values?
2. How does this behavior relate to Exercise 09?
3. What patterns do you notice when creating dataclass objects?
4. When might default values be useful in real code?

---

## Stretch Goal

Create a dataclass representing an application user.

Requirements:

```text
username
email
role (default: member)
active (default: True)
```

Create multiple users using different combinations of supplied and default values.

Observe which values Python chooses.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User accounts
- Application configuration
- Product catalog entries

Many application models contain sensible defaults.

For example:

```text
New users are active by default.
Products may be in stock by default.
Configuration values may have fallback settings.
```

Understanding how defaults behave makes it easier to design clean and predictable data models.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain why default values are used
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/11-default-values-revisited.py
```