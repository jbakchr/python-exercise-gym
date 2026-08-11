# Exercise 15 - Return Values

## Progression

```text
✅ Foundations Complete
✅ 11 Functions With Arguments
✅ 12 Multiple Arguments
✅ 13 Keyword Arguments
✅ 14 Flexible Wrappers
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
Decorators interact with return values.
```

By the end of this exercise you should understand:

- Why decorated functions can lose return values
- How wrappers receive return values
- How wrappers can pass return values back to callers
- Why many decorators return the result of the wrapped function

---

## Previously Learned

Before starting this exercise you should already understand:

- Decorators
- Wrapper functions
- `*args`
- `**kwargs`
- Flexible wrappers

If not, review:

```text
Exercise 14 - Flexible Wrappers
```

---

## Focus Area

This exercise explores:

```text
What happens when a decorated function returns a value.
```

Example:

```python
def add(a, b):
    return a + b
```

A function call can produce a result that another part of the program depends on.

What happens to that result when the function is decorated?

This is not a new concept.

It is a deeper look at how decorators affect function behavior.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Decorate a function that returns a value
2. Observe what happens to the return value
3. Modify the decorator so the value is preserved

As you work, pay attention to:

- What the wrapped function returns
- What the wrapper returns
- What the caller ultimately receives

---

## Starter Code

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("Call*ng function...")
        func(*args, **kwargs)

    return wrapper

@announce
def add(a, b):
    return a + b


result = add(2, 3)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What value does result contain?
```

---

### Question 2

```text
Why is the return value missing?
```

---

### Question 3

```text
What value does the wrapper return?
```

---

### Question 4

```text
How can the original return value be preserved?
```

---

## Verify Your Understanding

You should be able to explain:

- What the wrapped function returns
- What the wrapper returns
- Why return values can disappear
- How return values can be forwarded

You should also observe:

```text
A wrapper controls not only how a function
is called, but also what value is returned
to the caller.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Look carefully at:

```python
result = add(2, 3)
```

What value is assigned to `result`?

---

### Hint 2

The wrapped function returns a value.

Is the wrapper doing anything with it?

---

### Hint 3

Try storing the result of:

```python
func(*args, **kwargs)
```

inside the wrapper.

---

### Hint 4

The wrapper may need its own:

```python
return
```

statement.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
@announce
def multiply(a, b):
    return a * b
```

What value is returned?

---

### Experiment 2

Try:

```python
@announce
def greet(name):
   return f"Hello {name}"
```

What stays the same?

---

### Experiment 3
Print the value returned by:

```python
func(*args, **kwargs)
```

outside the wrapper.

What do you observe?

---

## Observations

Write your own findings.

Consider:

- What surprised you?
- What behaved as expected?
- Where did the return value go?
- How was the return value preserved?

---

## Reflection
Answer the following questions.

1 What did this exercise reveal about return values?
2. Why can a decorator accidentally break a function?
3. What responsibilities does a wrapper have?
4. When might preserving return values be important?

---

### Stretch Goal

Create several decorated functions that return different types of values.

Example:

```python
@announce
def get_number():
    return 42
```

```python
@announce
def get_message():
    return "hello"
```

```python
@announce
def get_items():
    return [1, 2, 3]
```

Verify that the decorator preserves all of them.

Observe:

- What values are returned?
- Does the decorator change the returned value?
- Does the wrapper behave differently for different return types?

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Logging decorators
- Timing decorators
- Caching decorators
- Authentication decorators
- Monitoring decorators

These decorators often need to preserve the behavior of the original function.

Understanding return values helps ensure a decorator enhances a function without breaking it.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed a missing return value
- [ ] You fixed the decorator to preserve the return value
- [ ] You can explain why the problem occurred
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/15-return-values.py
```