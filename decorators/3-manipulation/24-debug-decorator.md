# Exercise 24 - Debug Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
✅ Retry Decorator
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and flexible wrappers
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable debugging decorator that
displays function calls, arguments,
and return values.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Decorator factories
- Wrappers
- Return values
- Function arguments
- Positional arguments
- Keyword arguments
- Exception handling

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Understand how functions are being
called while debugging an application.
```

Example:

```text
A calculation produces an unexpected result.

You want to see:

- Which function was called
- Which arguments were passed
- What value was returned
```

without modifying each function manually.

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Displays the function name
2. Displays the arguments used
3. Displays the returned value
4. Returns the original result unchanged

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `debug`
- Display the decorated function name
- Display positional arguments
- Display keyword arguments
- Display the returned value
- Return the original result

Your solution should not:

- Modify the decorated function
- Duplicate debugging code inside multiple functions

---

## Starter Code

```python
def debug(func):
    pass


@debug
def add(a, b):
    return a + b


result = add(3, 5)

print(result)
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Display information before and after
a function executes.
```

Example:

```text
Calling add
Arguments: (3, 5)
Keyword Arguments: {}

Returned: 8

8
```

Another example:

```python
@debug
def greet(name, excited=False):
    if excited:
        return f"Hello {name}!"
    return f"Hello {name}"
```

Output:

```text
Calling greet
Arguments: ('Jonas',)
Keyword Arguments: {'excited': True}

Returned: Hello Jonas!
```

You should also be able to explain:

- Why the wrapper needs `*args`
- Why the wrapper needs `**kwargs`
- How the return value is preserved

---

## Hints

### Hint 1

Unlike previous exercises, your decorator should work with functions that accept any combination of arguments.

---

### Hint 2

Look at:

```python
*args
```

and:

```python
**kwargs
```

inside the wrapper.

---

### Hint 3

You will likely need something similar to:

```python
result = func(*args, **kwargs)
```

before display*ng the returned value.

## Possible Improvements

Once the basic solution works, consider:

- Formatting arguments more neatly
- Adding timestamps
- Displaying execution duration
- Logging to a file instead of the console
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why are `*args` and `**kwargs` useful here?
3. Why should the return value still be returned?
4. How could this decorator help during debugging?
5. How might this utility be reused in larger projects?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Display timestamps for every function call.
```

Example output:

```text
[10:32:15] Calling add
Arguments: (3, 5)

Returned: 8
```

Or:

```text
Display execution time alongside the
debug information.
```

Example:

```text
Calling add
Arguments: (3, 5)

Returned: 8
Execution Time: 0.0001 seconds
```

---

## Real-World Connection

This pattern appears in:

- Application debugging
- API development
- Testing
- Performance investigations
- Logging frameworks

Developers often need visibility into how functions are being used. Debug decorators make it easy to inspect function behavior without modifying the original implementation.

Many logging and observability tools use similar techniques behind the scenes.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Function names are displayed
- [ ] Arguments are displayed
- [ ] Return values are displayed
- [ ] The original result is preserved
- [ ] You understand how `*args` and `**kwargs` work
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/24-debug-decorator.py
```