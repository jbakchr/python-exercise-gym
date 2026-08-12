# Exercise 20 - Build a Call Logger

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
✅ 19 Stacking Decorators
➡️ Current Exploration Exercise
✅ Exploration Complete
```

---

## Goal

Explore how:

```text
Multiple decorator concepts can be combined
to create a practical and reusable decorator.
```

By the end of this exercise you should understand:

- How decorators can be used in real-world situations
- How to combine previously learned concepts
- How decorators can collect useful information
- How reusable decorators improve visibility and debugging

---

## Previously Learned

Before starting this exercise you should already understand:

- Flexible wrappers
- Return values
- Reusable decorators
- Function metadata
- Preserving metadata
- Stacking decorators

If not, review:

```text
Exercise 14 - Flexible Wrappers
Exercise 15 - Return Values
Exercise 16 - Reusable Decorators
Exercise 18 - Preserving Metadata
Exercise 19 - Stacking Decorators
```

---

## Focus Area

This exercise explores:

```text
Building a simple decorator that logs
function calls.
```

Example:

```text
Calling greet
Calling add
Calling create_user
```

The goal is not to create a production logging system.

The goal is to combine the skills developed throughout the Exploration stage.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `call_logger`
2. Log the name of the function being called
3. Execute the wrapped function
4. Preserve the function's return value

As you work, pay attention to:

- Where the function name comes from
- How the decorator remains reusable
- How the original behavior is preserved

---

## Starter Code

```python
from functools import wraps


def call_logger(func):
    pass


@call_logger
def greet(name):
    return f"Hello {name}"


print(greet("Alice"))
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
How can the decorator access the function's name?
```

---

### Question 2

```text
What information should be logged?
```

---

### Question 3

```text
How can the decorator remain reusable?
```

---

### Question 4

```text
How can the original return value be preserved?
```

---

## Verify Your Understanding

You should be able to explain:

- How the decorator accesses function metadata
- Why the decorator can work with many functions
- How the return value is preserved
- How reusable decorators simplify debugging

You should also observe:

```text
One decorator can provide useful
information about many different functions.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

You may have already explored a function attribute that contains its name.

---

### Hint 2

The decorator should work for more than one function.

---

### Hint 3

Consider using:

```python
@wraps(func)
```

---

### Hint 4

Do not forget to return the result of:

```python
func(*args, **kwargs)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
@call_logger
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
@call_logger
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

Decorate several different functions.

Observe:

```text
What information is always logged?

What information changes?
```

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What information came from the decorator?
- What information came from the wrapped function?
- Why is this useful?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about practical decorators?
2. Which concepts from the Exploration stage were used?
3. Why is a call logger useful?
4. How did preserving metadata improve the solution?

---

## Stretch Goal

Modify the decorator so it also logs:

```text
Before the function executes
```

and:

```text
After the function executes
```

Observe how the output changes.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Application logging
- Debugging
- Monitoring
- Performance tracking
- Audit trails

Many real-world decorators exist to add visibility without modifying the original function.

This is one of the most common practical uses of decorators.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You built a reusable call logger
- [ ] You logged function names successfully
- [ ] You preserved the original return value
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/20-build-a-call-logger.py
```