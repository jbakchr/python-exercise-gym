# Exercise 21 - Timing Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable timing decorator that measures
how long a function takes to execute.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Wrappers
- Functions with arguments
- Return values
- Preserving behavior with wrappers

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Measure how long certain functions take
to run without changing the functions
themselves.
```

Example:

```text
A data processing function is becoming slow.

You want to see its execution time without
adding timing code inside the function.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Measures how long a function takes to execute
2. Displays the execution time
3. Returns the original function result unchanged

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a `timer` decorator
- Display the function name
- Display execution time in seconds
- Return the original result

Your solution should not:

- Modify the decorated function
- Duplicate timing logic inside every function

---

## Starter Code

```python
import time


def timer(func):
    pass


@timer
def process_data():
    time.sleep(1)
    return "Processing complete"


result = process_data()

print(result)
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Execute a function

Measure how long the function took

Display the timing information

Return the original result
```

Example:

```text
process_data took 1.00 seconds
Processing complete
```

You should also be able to explain:

- Why the solution works
- Which concepts are being used
- How the utility could be reused

---

## Hints

### Hint 1

The `time` module contains functions for measuring time.

---

### Hint 2

Capture the start time before calling the original function.

Capture the end time afterward.

---

### Hint 3

Store the result of:

```python
func()
```

Calculate the elapsed time and then return the stored result.

---

## Possible Improvements

Once the basic solution works, consider:

- Displaying milliseconds
- Formatting output more cleanly
- Measuring functions with arguments
- Supporting keyword arguments
- Preserving function metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this solution solve?
2. Which previous exercises helped you complete it?
3. Why is a decorator useful in this situation?
4. How could this utility be reused in larger projects?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Allow the decorator to optionally display
a custom label instead of the function name.
```

Or:

```text
Support functions that accept any number
of positional and keyword arguments.
```

---

## Real-World Connection

This pattern appears in:

- Performance monitoring
- Profiling applications
- Debugging slow code
- API performance tracking
- Data processing pipelines

Developers often use timing decorators to identify bottlenecks without modifying the business logic of their functions. This keeps timing concerns separate from the function's primary responsibility.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] The execution time is displayed
- [ ] The original return value is preserved
- [ ] You understand how the wrapper works
- [ ] You can explain how the decorator could be reused
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/21-timing-decorator.py
```