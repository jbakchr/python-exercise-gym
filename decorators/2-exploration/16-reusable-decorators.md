# Exercise 16 - Reusable Decorators

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
✅ 13 Keyword Arguments
✅ 14 Flexible Wrappers
✅ 15 Return Values
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
A single decorator can be reused across many
different functions.
```

By the end of this exercise you should understand:

- What makes a decorator reusable
- Why flexible wrappers are useful
- How one decorator can support many functions
- Why decorators are often written once and reused

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Flexible wrappers
- Return values
- `*args`
- `**kwargs`

If not, review:

```text
Exercise 14 - Flexible Wrappers
Exercise 15 - Return Values
```

---

## Focus Area

This exercise explores:

```text
How the same decorator can be applied to
different functions without modification.
```

Example:

```python
@announce
def greet(name):
    ...
```

```python
@announce
def add(a, b):
    ...
```

```python
@announce
def create_account(username, active=True):
    ...
```

The decorator remains unchanged.

Only the decorated functions differ.

This is not a new concept.

It is a deeper look at one of the biggest advantages of decorators.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Apply it to several different functions
3. Observe how the same decorator behaves in each case

As you work, pay attention to:

- What changes between functions
- What stays the same
- Why the decorator can be reused

---

## Starter Code

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)

    return wrapper


@announce
def greet(name):
    return f"Hello {name}"


print(greet("Alice"))
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What part of the behavior comes from the decorator?
```

---

### Question 2

```text
What part of the behavior comes from the original function?
```

---

### Question 3

```text
Why can one decorator work with several different functions?
```

---

### Question 4

```text
What would happen if each function required its own decorator?
```

---

## Verify Your Understanding

You should be able to explain:

- Why the decorator works for multiple functions
- What makes the wrapper flexible
- Why reusability is valuable
- How decorators reduce repeated code

You should also observe:

```text
The same behavior can be added to many
functions by applying the same decorator.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Try decorating functions with different signatures.

---

### Hint 2

Try decorating functions that return different types of values.

---

### Hint 3

Observe what the decorator does that is independent of the function being decorated.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
@announce
def add(a, b):
    return a + b
```

Call:

```python
print(add(2, 3))
```

What changes?

---

### Experiment 2

Try:

```python
@announce
def create_user(name):
    return {"name": name}
```

Call:

```python
print(create_user("Alice"))
```

What stays the same?

---

### Experiment 3

Create a third decorated function with a completely different purpose.

Observe:

```text
What behavior is shared?

What behavior is unique?
```

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What behavior came from the decorator?
- What behavior came from the original function?
- Why is reusability valuable?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about decorators?
2. Why is reusability useful?
3. What role does the wrapper play in making reuse possible?
4. When might you reuse the same decorator in a real application?

---

## Stretch Goal

Create three different functions and decorate all of them.

Examples:

```python
greet(name)
```

```python
add(a, b)
```

```python
create_account(username)
```

Observe how the same decorator can be applied repeatedly without modification.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Logging decorators
- Timing decorators
- Authorization decorators
- Validation decorators
- Monitoring decorators

These decorators are often written once and reused throughout an application.

Reusability is one of the primary reasons decorators are so powerful.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You applied the same decorator to multiple functions
- [ ] You identified which behavior comes from the decorator
- [ ] You identified which behavior comes from the wrapped function
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/16-reusable-decorators.py
```