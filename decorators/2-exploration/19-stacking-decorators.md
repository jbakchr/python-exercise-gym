# Exercise 19 - Stacking Decorators

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
✅ 18 Preserving Metadata
➡️ Current Exploration Exercise
⬜ Final Exploration Exercise
```

---

## Goal

Explore how:

```text
Multiple decorators interact when applied
to the same function.
```

By the end of this exercise you should understand:

- How multiple decorators can be stacked
- The order in which decorators execute
- How wrapper functions build on one another
- Why decorator order matters

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Flexible wrappers
- Return values
- Function metadata
- `functools.wraps`

If not, review:

```text
Exercise 17 - Function Metadata
Exercise 18 - Preserving Metadata
```

---

## Focus Area

This exercise explores:

```text
What happens when multiple decorators
wrap the same function.
```

Example:

```python
@decorator_a
@decorator_b
def greet():
    ...
```

At first glance, this may appear straightforward.

However:

```text
Which decorator runs first?

Which decorator runs last?

Does the order matter?
```

This exercise investigates those questions.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create two decorators
2. Apply both to the same function
3. Observe the order of execution

As you work, pay attention to:

- Which decorator runs first
- Which decorator runs last
- How execution flows through the wrappers

---

## Starter Code

```python
from functools import wraps


def before(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)

    return wrapper


def after(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@before
@after
def greet():
    print("Hello")


greet()
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
In what order do the messages appear?
```

---

### Question 2

```text
Which decorator receives the function first?
```

---

### Question 3

```text
How does execution move through the wrappers?
```

---

### Question 4

```text
What changes if the order of the decorators is reversed?
```

---

## Verify Your Understanding

You should be able to explain:

- How decorator stacking works
- Why execution order matters
- Which decorator is applied first
- Which decorator runs first

You should also observe:

```text
Decorator order affects the final behavior
of a decorated function.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Focus on the output order.

---

### Hint 2

Try drawing the decorators like layers:

```text
before
↓
after
↓
greet
```

---

### Hint 3

Try swapping the decorators:

```python
@after
@before
```

Observe what changes.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Reverse the decorator order:

```python
@after
@before
def greet():
    print("Hello")
```

What changes?

---

### Experiment 2

Add a third decorator.

Observe how the execution order changes.

---

### Experiment 3

Have each wrapper print a unique message.

Example:

```python
Decorator A
Decorator B
Function
```

Can you predict the output before running the code?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- Which decorator executed first?
- Which decorator executed last?
- Why does the order matter?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about decorator stacking?
2. Why is execution order important?
3. How would changing decorator order affect behavior?
4. When might multiple decorators be useful in real applications?

---

## Stretch Goal

Create three decorators:

```python
log_start
```

```python
log_end
```

```python
announce
```

Apply them to the same function and predict the output before running the code.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Authentication decorators
- Authorization decorators
- Logging decorators
- Timing decorators
- Caching decorators

Real applications often combine multiple decorators on the same function.

Understanding execution order helps prevent unexpected behavior.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed stacked decorators in action
- [ ] You identified the execution order
- [ ] You explored changing the decorator order
- [ ] You can explain why the output changes
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/19-stacking-decorators.py
```