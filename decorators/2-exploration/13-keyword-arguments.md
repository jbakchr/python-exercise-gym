# Exercise 13 - Keyword Arguments

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
Decorators behave when functions receive keyword arguments.
```

By the end of this exercise you should understand:

- What keyword arguments are
- Why `*args` alone is not always enough
- How wrappers receive keyword arguments
- How keyword arguments can be forwarded to the wrapped function

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Wrapper functions
- Positional arguments
- `*args`

If not, review:

```text
Exercise 12 - Multiple Arguments
```

---

## Focus Area

This exercise explores:

```text
How decorators behave when functions are called using keyword arguments.
```

Example:

```python
create_user(name="Alice")
```

instead of:

```python
create_user("Alice")
```

This is not a new concept.

It is a deeper look at how decorators receive information from function calls.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Apply it to a function that uses keyword arguments
3. Make the decorated function work correctly

As you work, pay attention to:

- What the wrapper receives
- What information is stored in keyword arguments
- How keyword arguments reach the original function

---

## Starter Code

```python
def announce(func):
    def wrapper(*args):
        pass
    return wrapper


@announce
def create_user(name):
    print(f"Created user: {name}")


create_user(name="Alice")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What happens when create_user(name="Alice")
is called?
```

---

### Question 2

```text
Why is *args unable to handle this situation?
```

---

### Question 3

```text
What changes when the wrapper accepts **kwargs?
```

---

## Verify Your Understanding

You should be able to explain:

- What keyword arguments are
- What `**kwargs` collects
- How keyword arguments are forwarded

You should also observe:

```text
Positional arguments and keyword arguments
are handled differently.

A wrapper must explicitly support both if it
needs to work with every kind of function call.
```

Avoid checking the solution until you can explain why the behavior occurs.
---

## Hints

### Hint 1

Look carefully at how the function is called:

```python
create_user(name="Alice")
```

---

### Hint 2

Try printing what the wrapper receives.

---

### Hint 3

You may need a parameter similar to:

```python
**kwargs
```

and you may need to pass those values to:

```python
func(...)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
create_user(name="Bob")
```

What changes?

---

### Experiment 2

Create another decorated function:

```python
@announce
def display_book(title):
    print(title)
```

Call:

```python
display_book(title="Python Basics")
```

What stays the same?

---

### Experiment 3

Print:

```python
kwargs
```

inside the wrapper.

What type of object is it?

Why do you think Python uses that structure?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How are keyword arguments stored?
- How does this differ from `args`?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about keyword arguments?
2. Why is `*args` not sufficient by itself?
3. What pattern do you notice in `kwargs`?
4. When might this be useful in real code?

---

## Stretch Goal

Create a decorated function that accepts both positional and keyword arguments.

Example:

```python
def create_account(username, active=True):
    ...
```

Observe what happens inside the wrapper.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Logging decorators
- Timing decorators
- Validation decorators
- Authentication decorators

These decorators often need to support functions that use keyword arguments.

Understanding `**kwargs` helps make decorators more flexible and reusable.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the decorator fail initially
- [ ] You fixed the decorator to handle keyword arguments
- [ ] You can explain how `**kwargs` works
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/13-keyword-arguments.py
```