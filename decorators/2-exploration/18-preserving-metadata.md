# Exercise 18 - Preserving Metadata

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
✅ 13 Keyword Arguments
✅ 14 Flexible Wrappers
✅ 15 Return Values
✅ 16 Reusable Decorators
✅ 17 Function Metadata
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
Function metadata can be preserved when using decorators.
```

By the end of this exercise you should understand:

- Why metadata is lost during decoration
- What `functools.wraps` does
- How metadata can be preserved
- Why many production decorators use `@wraps`

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Wrapper functions
- Function metadata
- `__name__`
- `__doc__`

If not, review:

```text
Exercise 17 - Function Metadata
```

---

## Focus Area

This exercise explores:

```text
How to preserve information that belongs
to the original function.
```

In the previous exercise you observed:

```python
greet.__name__
```

producing:

```text
wrapper
```

instead of:

```text
greet
```

Can decorators preserve the original metadata?

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Import `wraps` from `functools`
2. Apply it to a wrapper function
3. Observe how function metadata changes

As you work, pay attention to:

- The value of `__name__`
- The value of `__doc__`
- What changes after adding `@wraps`

---

## Starter Code

```python
from functools import wraps


def announce(func):
    @wraps(func)
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
What value is now printed?
```

---

### Question 2

```text
How does the result differ from the previous exercise?
```

---

### Question 3

```text
What happened to the original metadata?
```

---

### Question 4

```text
Why might preserving metadata be useful?
```

---

## Verify Your Understanding

You should be able to explain:

- What `functools.wraps` does
- Why metadata was lost previously
- How metadata is preserved
- Why many decorators use `@wraps`

You should also observe:

```text
The wrapper still executes.

However, metadata now appears to belong
to the original function.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Import:

```python
wraps
```

from:

```python
functools
```

---

### Hint 2

Apply:

```python
@wraps(func)
```

directly above the wrapper function.

---

### Hint 3

Compare the results before and after adding `@wraps`.

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

Remove:

```python
@wraps(func)
```

What changes?

---

### Experiment 3

Create another decorated function:

```python
@announce
def add(a, b):
    """Add two numbers."""
    return a + b
```

Print:

```python
add.__name__
```

and:

```python
add.__doc__
```

What do you observe?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What information was preserved?
- How did `@wraps` affect the result?
- Why might this matter in larger applications?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about function metadata?
2. How does `@wraps` differ from a regular wrapper?
3. Why is preserving metadata important?
4. When might this be useful in real code?

---

## Stretch Goal

Inspect both:

```python
greet.__name__
```

and:

```python
greet.__doc__
```

with and without:

```python
@wraps(func)
```

Compare the results.

What differences do you observe?

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Logging frameworks
- Testing frameworks
- Documentation generators
- Web frameworks
- Debugging tools

Many tools inspect functions to understand how they should behave.

Preserving metadata helps those tools work correctly.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You used `@wraps`
- [ ] You observed metadata being preserved
- [ ] You can explain what `@wraps` does
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/18-preserving-metadata.py
```