# Exercise 12 - Multiple Arguments

## Progres*ion

```text
✅ Foundations Complet*
✅ 11 Functions With Arguments
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exer*ise
```

---

## Goal

Explore how:

```text
Decorators behave when functions accept different numbers of positional arguments.
```

By the end of this exercise*you should understand:

- How `*args` handles multiple arguments
- Why one decorator can work with many different functions
- How positional arguments move through a wrapper

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Wrapper functions
- How `*args` can receive arguments passed to a decorated function

If not, revi*w:

```text
Exercise 11 - Function* With Arguments
```

---

## Focus Area

This exercise explores:

```text
How a single decorator can handle functions with different argument counts.
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
def multiply(a, b, c):
    ...
```

This is not a new concept.

It is a deeper look at how `*args` behaves.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Apply it to functions with different numbers of arguments
3. Observe how the wrapper receives those argumeets

As you work, pay attention to:

- What is stored in `args`
- How `args` changes for each function call
- Why the same decorator still works

---

## Starter Code

```python
def announce(func):
    def wrapper(*args):
        print("Calling function...")
        func(*args)

    return wrapper


@announce
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## Questions To Investi*ate

As you complete the exercise, try to answer:

### Question 1

```text
What is stored inside args when add(10, 20) is called?
```

---

### Question 2

```text
How does args change when more arguments are provided?
```

---

### Questio* 3

```text
Why can the same decorator work with several different functions?
```

---

## Verify Your Understanding

You sho*ld be able to explain:

- What `args` contains
- How positional arguments are collected
- Why forwarding `*args` works

You should also observe:

```text
The wrapper receives all positional arguments
as a tuple.

the number of values inside the tuple depends
on the function call
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Print:

```python
args
```

inside the wrapper

---

### Hint 2

Check the type of:

```python
args
```

---

### Hint 3

Call decorated functions with different numbers of arguments and compare the results.

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
def mu*tiply(a, b, c):
    print(a * b * c)
```

call:

```python
multiply(2, 3, 4)
```

What stays the same?

---

### Experiment 3

Add:

```python
print(args)
```

inside the wrapper.

Compare:

```python
greet("Alice")
add(0, 20)
multiply(2, 3, 4)
```

Why do you think the output differs?

---

## Observations

Write down your findings.

Consider:

- What surprised you? - What behaved as expected?
- How does `args` change?
- What patterns are starting to emerge?

---

## Reflection

Answer the following q*estions.

1. What did this exercise reveal about `*args`?
2. Why can one decorator work with functions that accept different numbers of arguments?
3. What pattern do you notice in the values stored inside `args`?
4. When might this flexibility be useful in real code?

---

## Stretch Goal

Create a decorated function that accepts four positional arguments.

Observe what happens inside:

```python
args
```

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connecti*n

This behavior appears in situat*ons such as:

- Logging decorators
- Performance monitoring decorators
- Debugging decorators
- Function*call tracking

These decorators are often written once and reused across many different functions.

Unde*standing how positional arguments *re collected allows decorators to remain flexible and reusable.

---

### Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed how `args` changes between function calls
- [ ] You can explain why one decorator works with multiple functions
- [ ] You explored at least one variation
* [ ] You feel comfortable using `*args` with decorators

---

## Solution

See:

```text
solutions/12-multiple-arguments.py
```