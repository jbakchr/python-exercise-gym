# Exercise 11 - Decorating Functions With Arguments

## Progression

```text
✅ Foundations Complete
➡️ Current Exploration Exercise
⬜ Next Exploration Exercise
⬜ Future Exercise
```

---

## Goal

Explore how:

```text
Decorators behave when the decorated function accepts arguments.
```

By the end of this exercise you should understand:

- Why some decorators break when arguments are introduced
- How wrapper functions receive arguments
- How arguments can be passed to the original function

---

## Previously Learned

Before starting this exercise you should already understand:

- Functions are objects
- Wrapper functions
- Basic decorators
- The `@` syntax

If not, review:

```text
Exercise 10 - Build a Simple Announcer
```

---

## Focus Area

This exercise explores:

```text
How decorators behave when functions have arguments.
```

Example:

```python
@announce
def greet(name):
    print(f"Hello {name}")
```

This is not a new concept.

It is a deeper look at a concept you already know.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a decorator named `announce`
2. Apply it to a function that accepts an argument
3. Make the decorated function work correctly

As you work, pay attention to:

- What arguments the wrapper receives
- What arguments the original function receives
- What happens if arguments are not passed correctly

---

## Starter Code

```python
def announce(func):
    def wrapper():
        print("Calling function...")
        func()

    return wrapper


@announce
def greet(name):
    print(f"Hello {name}")


greet("Alice")
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
What happens when greet("Alice") is called?
```

---

### Question 2

```text
Why does the wrapper fail to handle the argument?
```

---

### Question 3

```text
What changes if the wrapper accepts *args?
```

---

## Verify Your Un*erstanding

You should be able to explain:

- Why the original decorator fails
- What `*args` collects
- How arguments reach the wrapped function

You should also observe:

```text
The wrapper receives arguments first.
The wrapper decides what to do with them.
The original function only receives arguments that are explicitly forwarded.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

The prob*em is not inside `greet()`.

Investigate the wrapper instead.

---

### Hint 2

Try printing what the wrapper receives.

Example:

```python
print(args)
```

---

### Hint 3
*The wrapper may need this paramete*:

```python
*args
```

and may need to pass those arguments to:

```*ython
func(...)
```

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
greet("Bob")
```

What changes?

---

### Experiment 2

Try:
```python
@announce
def goodbye(name):
    print(f"Goodbye {name}")
```

Does the decorator still work?
What stays the same?

---

### Experiment 3

Try:

```python
@announce
def add(a, b):
    print(a + b)
```

Call:

```python
add(10, 20)
```

Why do you think this works?

---

## Observations*
Write down your findings.

Consider:

- What surprised you?
- What b*haved as expected?
- What patterns*are starting to emerge?
- What do you think Python is doing behind the scenes?

---

## Reflection

Answ*r the following questions.

1. Wha* did this exercise reveal about wr*pper functions?
2. How does this behavior relate to previous decorator exercises?
3. What pattern do you notice between the wrapper and the wrapped function?
4. When might this be useful in real code?

---

## Stretch Goal

Create and decorate a function that accepts three argum*nts.

Example:

```python
@announce
def multiply(a, b, c):
    print(a * b * c)
```

Observe whether your decorator needs any modifications.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-Wo*ld Connection

This behavior appea*s in situations such as:

- Loggin* decorators
- Timing decorators
- *uthentication decorators
- Validat*on decorators

These decorators of*en need to work with many differen* functions.

Understanding how arg*ments are received and forwarded a*lows a single decorator to be reus*d throughout an application.

---
*## Success Criteria

You can consi*er this exercise complete when:

-*[ ] You completed the investigatio*
- [ ] You observed the decorator *ailing initially
- [ ] You fixed t*e decorator to handle arguments
- * ] You can explain how `*args` wor*s
- [ ] You explored at least one *ariation
- [ ] You feel comfortabl* experimenting further

---

## So*ution

See:

```text
*olutions/01-decorating-functions-w*th-arguments.py
```