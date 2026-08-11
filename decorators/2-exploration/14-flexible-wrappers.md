# Exercise 14 - Flexible Wrappers

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
✅ 13 Keyword Arguments
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
A single decorator can support both positional
arguments and keyword arguments.
```

By the end of this exercise you should understand:

- Why `*args` alone is not always enough
- Why `**kwargs` alone is not always enough
- How flexible wrappers work
- Why many real-world decorators use both

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Wrapper functions
- `*args`
- `**kwargs`

If not, review:

```text
Exercise 11 - Functions With Arguments
Exercise 12 - Multiple Arguments
Exercise 13 - Keyword Arguments
```

---

## Focus Area

This exercise explores:

```text
How a wrapper can handle any combination of
positional and keyword arguments.
```

Example:

```python
greet("Alice")
```

and:

```python
create_user(name="Alice")
```

and:

```python
create_account("Alice", active=True)
```

using the same decorator.

This is not a new concept.

It is a deeper look at how decorators can become more flexible.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Apply it to several different functions
3. Make the decorator work in every case

As you work, pay attention to:

- What is stored in `args`
- What is stored in `kwargs`
- How both are forwarded to the original function

---

## Starter Code

```python
def announce(func):
    def wrapper(*args):
        print("Calling function...")
        func(*args)

    return wrapper


@announce
def create_account(username, active=True):
    print(f"{username} ({active})")


create_account("Alice", active=False)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Why does the previous solution fail?
```

---

### Question 2

```text
What information is stored in args?
```

---

### Question 3

```text
What information is stored in kwargs?
```

---

### Question 4

```text
How can both be passed to the wrapped function?
```

---

## Verify Your Understanding

You should be able to explain:

- What `args` contains
- What `kwargs` contains
- Why both may be needed
- How a flexible wrapper forwards information

You should also observe:

```text
A flexible wrapper can support many different
function signatures without modification.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Review how you solved Exercise 12.

---

### Hint 2

Review how you solved Exercise 13.

---

### Hint 3

The wrapper may need both:

```python
*args
```

and:

```python
**kwargs***
```

---

### Hint 4

The original function may need to receive both:

```python
func(*args, **kwargs)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
@announce
def greet(name):
    print(f"Hello {name}")
```

Call:

```python
greet("Alice")
```

What changes?

---

### Experiment 2

Try:

```python
@announce
def create_user(name):
    print(f"Created user: {name}")
```

Call:

```python
create_user(name="Alice")
```

What stays the same?

---

### Experiment 3

Try:

```python
@announce
def create_account(username, active=True):
    print(username, active)
```

Call:

```python
create_account("Alice", active=False)
```

What appears in:

```python
args
```

and:

```python
kwargs
```

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- What goes into `args`?
- What goes into `kwargs`?
- Why is the wrapper now more flexible?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about wrapper functions?
2. Why do many decorators use both `*args` and `**kwargs`?
3. How does a flexible wrapper differ from previous wrappers?
4. When might this be useful in real code?

---

## Stretch Goal

Create three decorated functions:

```python
greet(name)
```

```python
add(a, b)
```

```python
create_account(username, active=True)
```

Verify that the same decorator works correctly for all of them.

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

These decorators are often designed to work with many different functions.

Flexible wrappers allow a single decorator to be reused throughout an application.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You identified the limitations of earlier wrappers
- [ ] You created a flexible wrapper
- [ ] You can explain the purpose of `*args`
- [ ] You can explain the purpose of `**kwargs`
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/14-flexible-wrappers.py
```