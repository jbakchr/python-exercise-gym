# Exercise 18 - Post Initialization

## Progression

```text
✅ Foundations Complete
✅ Exercise 11 - Default Values Revisited
✅ Exercise 12 - Default Factories
✅ Exercise 13 - Optional Fields
✅ Exercise 14 - Immutable Dataclasses
✅ Exercise 15 - Field Customization
✅ Exercise 16 - Ordering Objects
✅ Exercise 17 - Sorting Dataclass Instances
➡️ Current Exploration Exercise
⬜ Exercise 19 - Nested Dataclasses
⬜ Exercise 20 - Dataclass Design Patterns
```

---

## Goal

Explore how:

```text
__post_init__()
```

behaves in dataclasses.

By the end of this exercise you should understand:

- When __post_init__ is executed
- Why additional initialization may be needed
- How dataclass objects can be adjusted after creation

---

## Previously Learned

Before starting this exercise you should already understand:

- Dataclass fields
- Default values
- Field customization
- Object creation

If not, review:

```text
Exercise 17 - Sorting Dataclass Instances
```

---

## Focus Area

This exercise explores:

```text
How dataclasses perform additional work
immediately after initialization.
```

Example:

```text
A user enters a name.

The application automatically converts
the name to title case.
```

This is not a new concept.

It is a deeper look at what happens after the automatically generated __init__ method finishes.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a dataclass with a __post_init__ method.
2. Create several objects.
3. Observe how field values change during initialization.

As you work, pay attention to:

- When __post_init__ runs
- What values exist before and after initialization
- How object state can be adjusted automatically

---

## Starter Code

```python
from dataclasses import dataclass


@dataclass
class User:
    username: str

    def __post_init__(self):
        self.username = self.username.strip().lower()


user = User("  Alice  ")

print(user)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What does the username contain
after the object is created?
```

---

### Question 2

```text
When does __post_init__ run?
```

---

### Question 3

```text
Why might this behavior be useful?
```

---

## Verify Your Understanding

You should be able to explain:

- What __post_init__ does
- When __post_init__ executes
- Why additional initialization logic may be needed

You should also observe:

```text
The username value is automatically
cleaned after object creation.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look closely at the value passed into the constructor.

Compare it with the value that is printed.

---

### Hint 2

The dataclass creates the object first.

Then __post_init__ is called.

---

### Hint 3

__post_init__ exists because some initialization
logic cannot easily be expressed using field
definitions alone.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
user = User("   BOB   ")

print(user)
```

What changes?

---

### Experiment 2

Try:

```python
def __post_init__(self):
    self.username = self.username.title()
```

What happens now?

---

### Experiment 3

Try:

```python
@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        self.name = self.name.upper()
```

Create a product and print it.

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

1. What did this exercise reveal about __post_init__?
2. How does it differ from normal field definitions?
3. What kinds of adjustments are useful during initialization?
4. When might this be valuable in real applications?

---

## Stretch Goal

Add another field:

```python
email: str
```

Use __post_init__ to normalize the email address.

Example:

```python
alice@example.com
```

instead of:

```python
ALICE@EXAMPLE.COM
```

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User account creation
- Configuration loading
- Data validation
- Data normalization
- API data processing

Many applications need data to be cleaned or adjusted immediately after object creation.

For example:

```text
Remove extra whitespace

Normalize email addresses

Standardize names

Convert values into consistent formats
```

Post-initialization allows dataclasses to automatically prepare data before the object is used elsewhere in the application.

Understanding __post_init__ is important because it provides a bridge from simple data containers toward intelligent application models.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain when __post_init__ runs
- [ ] You understand why post-initialization exists
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/18-post-initialization.py
```