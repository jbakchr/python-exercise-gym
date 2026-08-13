# Exercise 31 - Slow API Calls

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

➡️ Current Problem Solving Exercise

⬜ 32 - Rate Limited Service
⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Timing Decorators
Logging Decorators
Function Wrapping
Return Values
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A Python application communicates with multiple external APIs.

Users have started reporting that some features feel slow.

Developers suspect that certain API requests take much longer than others,
but nobody knows exactly which operations are causing the delays.

The team wants a reusable way to measure execution times without inserting
timing code into every function.
```

Example:

```text
An application retrieves:

- Users
- Orders
- Products

from different services.

The team wants to identify slow operations and gather timing information
before attempting any optimizations.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Measure how long API operations take to execute
- Display the function name
- Display the execution time
- Preserve the original return value

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Duplicate timing code inside every API function
- Change the behaviour of the wrapped functions

---

## Example Usage

The completed solution should support behaviour similar to:

```python
fetch_users()

fetch_orders()

fetch_products()
```

Example output:

```text
fetch_users completed in 1.00 seconds

fetch_orders completed in 2.00 seconds

fetch_products completed in 0.50 seconds
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Execution times are displayed automatically.

Functions continue to return their normal results.

New API functions can easily be monitored without copying timing logic.
```

---

## Constraints

Consider the following constraints:

- Additional API functions may be added later
- Some functions may complete very quickly
- Return values must remain unaffected

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
import time


def fetch_users():
    time.sleep(1)
    return ["Alice", "Bob"]


def fetch_orders():
    time.sleep(2)
    return ["Order 1", "Order 2"]


def fetch_products():
    time.sleep(0.5)
    return ["Laptop", "Keyboard"]
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What problem is the team actually trying to solve?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about Exercise 21 and Exercise 29.

---

### Hint 3

Think about how you could reduce duplication.

Would you really want timing code inside every API function?

---

## Design Questions

As you work, consider:

1. Why did you choose your approach?
2. Were there alternative solutions?
3. What trade-offs exist?
4. Which previous exercises influenced your design?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- A function returns a value
- A function completes almost instantly
- Additional API functions are added later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about monitoring application performance?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Display a warning for slow operations
- Allow a configurable timing threshold
- Record timing results for later analysis
- Include function arguments in the output

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Developers regularly monitor execution times to identify performance bottlenecks. Modern observability and monitoring platforms often build upon the same basic idea: measuring how long important operations take and highlighting unusually slow behaviour.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The solution handles the important edge cases
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You feel prepared for more open-ended challenges

---

## Solution

See:

```text
solutions/31-slow-api-calls.py
```
