# Exercise 23 - Retry Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and exception handling
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable retry decorator that
automatically retries failed operations.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Decorator factories
- Wrappers
- Loops
- Function execution
- Basic exception handling

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Run a function that occasionally fails
because of temporary problems.
```

Example:

```text
A network request sometimes fails.

A database connection occasionally
times out.

A file is temporarily unavailable.
```

Instead of giving up immediately, you want to retry the operation automatically.

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Attempts to execute a function
2. Retries when an exception occurs
3. Stops retrying when the function succeeds
4. Raises the exception if all retries fail

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `retry`
- Accept a maximum retry count
- Catch exceptions raised by the decorated function
- Retry the function when a failure occurs
- Stop immediately when the function succeeds
- Re-raise the exception if all attempts fail

Your solution should not:

- Require retry logic inside every function
- Hide failures permanently

---

## Starter Code

```python
def retry(max_attempts):
    pass


@retry(3)
def unstable_operation():
    raise ValueError("Temporary failure")


unstable_operation()
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Retry failed operations automatically.
```

Example:

```text
Attempt 1 failed
Retrying...

Attempt 2 failed
Retrying...

Success
```

Another example:

```text
Attempt 1 failed
Retrying...

Attempt 2 failed
Retrying...

Attempt 3 failed

ValueError: Temporary failure
```

The operation should only raise an exception after all retry attempts have been exhausted.

You should also be able to explain:

- Why exceptions are useful here
- When retries should stop
- How the decorator improves code reuse

---

## Hints

### Hint 1

You already know how to repeat a function call from Exercise 22.

Can you combine repetition with exception handling?

---

### Hint 2

Look at:

```python
try:
    ...
except:
    ...
```

for detecting failures.

---

### Hint 3

You may need logic similar to:

```python
for attempt in range(...):
```

inside your wrapper.

---

## Possible Improvements

Once the basic solution works, consider:

- Displaying the current attempt number
- Waiting before retrying
- Supporting specific exception types
- Supporting functions with arguments
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why is retry logic useful?
3. When should retries stop?
4. What risks exist if retries continue forever?
5. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Wait one second between retry attempts.
```

Or:

```text
Display the current attempt number and
remaining retries.
```

Example output:

```text
Attempt 1 of 3 failed
Retrying...

Attempt 2 of 3 failed
Retrying...

Attempt 3 of 3 failed
```

---

## Real-World Connection

This pattern appears in:

- API clients
- Database integrations
- Cloud services
- Distributed systems
- Background job processing

Transient failures are common in real applications. Rather than failing immediately, software often retries operations because a temporary problem may disappear moments later.

Retry decorators allow developers to add this behavior without changing the business logic of individual functions.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Failed operations are retried
- [ ] Successful operations stop retrying
- [ ] Exceptions are raised after all retries fail
- [ ] You understand how decorators and exceptions work together
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/23-retry-decorator.py
```