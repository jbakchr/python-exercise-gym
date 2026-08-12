# Exercise 22 - Repeat Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators with parameters
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable decorator that can execute
a function multiple times automatically.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Wrappers
- Return values
- Timing decorators
- Functions with arguments

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Repeat an action several times without
writing loops everywhere in your code.
```

Example:

```text
A testing utility needs to run the same
function multiple times.

A notification system needs to send
the same message repeatedly.

A data generator needs to create
multiple sample records.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Accepts a repeat count
2. Executes the decorated function multiple times
3. Keeps the implementation reusable

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `repeat`
- Accept a number specifying how many times to run the function
- Execute the function the requested number of times
- Work with the `@repeat(n)` syntax

Your solution should not:

- Require manual loops around function calls
- Duplicate repetition logic throughout the program

---

## Starter Code

```python
def repeat(times):
    pass


@repeat(3)
def greet():
    print("Hello")


greet()
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Run a decorated function multiple times
using a configurable repeat count.
```

Example:

```text
Hello
Hello
Hello
```

Another example:

```python
@repeat(5)
def show_line():
    print("-" * 20)

show_line()
```

Output:

```text
--------------------
--------------------
--------------------
--------------------
--------------------
```

You should also be able to explain:

- Why a decorator factory is needed
- How the repeat count reaches the wrapper
- How the utility could be reused

---

## Hints

### Hint 1

A basic decorator receives a function.

This exercise needs something extra:

```python
@repeat(3)
```

Where does the `3` go?

---

### Hint 2

You may need more than one nested function.

Think about:

```python
repeat()
    decorator()
        wrapper()
```

---

### Hint 3

The wrapper can execute the original function inside a loop.

Something similar to:

```python
for _ in range(...):
    ...
```

---

## Possible Improvements

Once the basic solution works, consider:

- Supporting any function arguments
- Returning collected results
- Displaying which repetition is currently running
- Validating that the repeat count is positive
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why can't a normal decorator handle `@repeat(3)`?
3. How many nested functions are required?
4. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Display progress information for each run.
```

Example output:

```text
Run 1 of 3
Hello

Run 2 of 3
Hello

Run 3 of 3
Hello
```

Or:

```text
Collect and return all results generated
by the repeated function calls.
```

---

## Real-World Connection

This pattern appears in:

- Test automation
- Data generation
- Retry mechanisms
- Scheduled task execution
- Batch processing systems

Developers frequently create parameterized decorators when a utility needs configuration. The caller can customize behavior while still keeping the underlying implementation reusable.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] The repeat count is configurable
- [ ] The decorator uses `@repeat(n)` syntax
- [ ] You understand why multiple nested functions are needed
- [ ] You can explain how the repeat count reaches the wrapper
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/22-repeat-decorator.py
```