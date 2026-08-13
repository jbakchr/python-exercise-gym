# Exercise 29 - Logging Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
✅ Retry Decorator
✅ Debug Decorator
✅ Access Counter
✅ Cache Decorator
✅ Permission Decorator
✅ Validation Decorator
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
```

---

## Goal

Use:

```text
decorators and file handling
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable logging decorator that
records function activity to a log file.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Flexible wrappers
- Return values
- Function arguments
- Conditional execution
- State management
- Validation decorators
- Permission decorators

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Keep a record of important actions
performed by an application.
```

Example:

```text
A user account is created.

A report is generated.

A file is deleted.

You want a permanent record of
when those actions occurred.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Records function activity
2. Saves information to a log file
3. Includes the function name
4. Keeps logging logic reusable

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `log_calls`
- Accept a log file name
- Record the function name
- Append log entries to the file
- Execute the original function normally
- Work with function arguments

Your solution should not:

- Duplicate logging code in every function
- Overwrite previous log entries

---

## Starter Code

```python
def log_calls(filename):
    pass


@log_calls("app.log")
def create_user(username):
    print(f"Creating user: {username}")


create_user("jonas")
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Execute a function normally.

Record the function call in a log file.
```

Example console output:

```text
Creating user: jonas
```

Example log file contents:

```text
create_user called
```

Another example:

```python
@log_calls("app.log")
def generate_report():
    print("Generating report")
```

Log file:

```text
create_user called
generate_report called
```

You should also be able to explain:

- Why append mode is useful
- Why logging is handled by the decorator
- How the decorator remains reusable

---

## Hints

### Hint 1

This exercise combines decorators with file handling.

---

### Hint 2

You may need to open the file using:

```python
with open(...):
```

before calling the original function.

---

### Hint 3

A log entry might look like:

```text
create_user called
```

Use the function name when creating the entry.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding timestamps
- Recording arguments
- Recording return values
- Logging exceptions
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why is append mode important?
3. Why should logging be separated from business logic?
4. How does this approach reduce duplicated code?
5. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Include timestamps in every log entry.
```

Example:

```text
2026-08-13 10:15:02 - create_user called
```

Or:

```text
Record function arguments.
```

Example:

```text
create_user called with ('jonas',)
```

---

## Real-World Connection

This pattern appears in:

- Web applications
- APIs
- Background jobs
- Monitoring systems
- Audit systems

Most production applications keep logs of important activity. Logging helps developers investigate problems, monitor system behavior, and understand how software is being used.

Python's built-in:

```python
logging
```

module provides a far more powerful solution, but the ideas explored in this exercise help build intuition for how logging systems work.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Function calls are written to a file
- [ ] Existing log entries are preserved
- [ ] The original function still executes
- [ ] The decorator works with function arguments
- [ ] You understand how decorators and file handling work together
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/29-logging-decorator.py
```