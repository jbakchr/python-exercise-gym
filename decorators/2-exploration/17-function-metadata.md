# Exercise 17 - Function Metadata

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
✅ 13 Keyword Arguments
✅ 14 Flexible Wrappers
✅ 15 Return Values
✅ 16 Reusable Decorators
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
Decorators can affect information about a function.
```

By the end of this exercise you should understand:

- What function metadata is
- Where function names are stored
- What happens to metadata when a function is decorated
- Why this behavior can be surprising

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Wrapper functions
- Flexible wrappers
- Return values

If not, review:

```text
Exercise 16 - Reusable Decorators
```

---

## Focus Area

This exercise explores:

```text
Information that belongs to a function.
```

Examples include:

```python
__name__
```

and:

```python
__doc__
```

Functions carry information about themselves.

What happens to that information after decoration?

This is not a new decorator feature.

It is an investigation into how decorators affect existing behavior.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Decorate a function
3. Inspect information about the decorated function

As you work, pay attention to:

- The function name before decoration
- The function name after decoration
- What information seems to change

---

## Starter Code

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
    return func(*args, **kwargs)

    return wrapper


@announce
def greet():
    """Display a greeting."""
    print("Hello")


print(greet.__name__)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What value is printed?
```

---

### Question 2

```text
Is the value what you expected?
```

---

### Question 3

```text
Why is the original function name missing?
```

---

### Question 4

```text
What object is greet referring to after decoration?
```

---

## Verify Your Understanding

You should be able to explain:

- What function metadata is
- What `__name__` represents
- Why the function name changes
- What object replaces the original function

You should also observe:

```text
After decoration, the original function
is no longer called directly.

The wrapper becomes the callable object.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Try printing:

```python
greet.__name__
```

---

### Hint 2

Compare the printed value with the original function name.

---

### Hint 3

The decorated function may not be the object you expect.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Print:

```python
greet.__doc__
```

What value is displayed?

---

### Experiment 2

Rename:

```python
def greet():
```

to:

```python
def say_hello():
```

What changes?

---

### Experiment 3

Decorate another function:

```python
@announce
def add(a, b):
    return a + b
```

Print:

```python
add.__name__
```

Does the same behavior occur?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What information changed?
- What information was lost?
- Why might this be a problem?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about decorated functions?
2. Why does the function name change?
3. What object is actually being called after decoration?
4. Why might metadata be important in real applications?

---

## Stretch Goal

Inspect the following attributes:

```python
greet.__name__
```

```python
greet.__doc__
```

Compare them before and after applying the decorator.

What differences do you observe?

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Debugging
- Logging
- Testing
- Documentation tools
- Frameworks that inspect functions

Many tools rely on metadata to understand functions.

Losing that metadata can make debugging and introspection harder.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You inspected function metadata
- [ ] You observed metadata changing after decoration
- [ ] You can explain why the behavior occurs
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/17-function-metadata.py
```