# Exercise 25 - Access Counter

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
✅ Retry Decorator
✅ Debug Decorator
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and state management
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable decorator that tracks
how many times a function has been called.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Decorator factories
- Wrappers
- Return values
- Flexible wrappers
- Positional arguments
- Keyword arguments

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Track how frequently important
functions are used.
```

Example:

```text
A reporting function is heavily used.

You want to know how often it runs.

A menu option is available to users.

You want to measure which options
are used most frequently.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Tracks how many times a function is called
2. Displays the current count
3. Continues to return the original function result
4. Works with functions that accept arguments

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `count_calls`
- Track the number of times the function is executed
- Display the current call count
- Work with positional and keyword arguments
- Return the original function result unchanged

Your solution should not:

- Modify the decorated function
- Store counts in global variables

---

## Starter Code

```python
def count_calls(func):
    pass


@count_calls
def greet(name):
    return f"Hello {name}"


print(greet("Jonas"))
print(greet("Jonas"))
print(greet("Jonas"))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Track function usage automatically.
```

Example:

```text
greet has been called 1 time(s)
Hello Jonas

greet has been called 2 time(s)
Hello Jonas

greet has been called 3 time(s)
Hello Jonas
```

Another example:

```python
@count_calls
def add(a, b):
    return a + b
```

Output:

```text
add has been called 1 time(s)

add has been called 2 time(s)

add has been called 3 time(s)
```

You should also be able to explain:

- Where the count is stored
- Why the count persists between calls
- How the decorator remains reusable

---

## Hints

### Hint 1

The decorator needs to remember information between function calls.

Think about where that information could live.

---

### Hint 2

The wrapper function can access variables defined in the surrounding scope.

---

### Hint 3

The call count should increase every time the wrapper executes.

Something similar to:

```python
count += 1
```

may be useful.

---

## Possible Improvements

Once the basic solution works, consider:

- Tracking successful calls separately from failed calls
- Recording the timestamp of each call
- Making the count accessible from outside the decorator
- Combining the decorator with the debug decorator
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Where is the count stored?
3. Why does the count continue increasing across calls?
4. How does the wrapper gain access to the stored count?
5. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Display the total number of calls
only after the function completes.
```

Or:

```text
Track both successful and failed calls.
```

Example output:

```text
Successful Calls: 8
Failed Calls: 2
```

---

## Real-World Connection

This pattern appears in:

- Usage analytics
- Monitoring systems
- API tracking
- Application metrics
- Performance investigations

Developers often need visibility into how frequently specific functions are used. Usage counts can reveal bottlenecks, identify popular features, and help guide optimization efforts.

Many monitoring and observability platforms collect similar metrics automatically.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Function calls are counted correctly
- [ ] The count persists between calls
- [ ] The original result is preserved
- [ ] The decorator works with function arguments
- [ ] You understand where the state is stored
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/25-access-counter.py
```