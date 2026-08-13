# Exercise 32 - Rate Limited Service

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31 - Slow API Calls

➡️ Current Problem Solving Exercise

⬜ 33 - Expensive Calculations
⬜ 34 - Audit Trail System
⬜ 35 - Production Debugging
⬜ 36 - Function Monitoring
⬜ 37 - Data Validation Pipeline
⬜ 38 - Secure Operations
⬜ 39 - Background Task Tracking
⬜ 40 - Decorator Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Decorator Factories
State Management
Access Counters
Function Wrapping
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A Python application integrates with a third-party weather service.

The service only allows a limited number of requests.

If too many requests are sent, the service begins rejecting them.

Several parts of the application use the service, and the
development team wants a reusable way to enforce request limits.
```

Example:

```text
The free version of the service allows:

3 requests

After the third request, additional requests should be blocked.
```

The team wants a solution that can be applied to multiple functions without duplicating logic.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Allow a configurable maximum number of function calls
- Track how many times a function has been called
- Prevent execution once the limit has been reached
- Display a message when the limit is exceeded

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Store counting logic inside every function
- Require manual tracking of requests
- Duplicate access-control logic

---

## Example Usage

The completed solution should support behaviour similar to:

```python
get_weather()

get_weather()

get_weather()

get_weather()
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Getting weather data...

Getting weather data...

Getting weather data...

Request limit exceeded.
```

The first three function calls should execute normally.

Subsequent calls should be blocked.

---

## Constraints

Consider the following constraints:

- Different functions may require different limits
- Multiple functions may use the solution
- The request count must persist between calls

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def get_weather():
    print("Getting weather data...")


def get_forecast():
    print("Getting forecast data...")
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What rule is the application trying to enforce?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Access Counter
Decorator Factories
State Management
```

---

### Hint 3

Think about where call-tracking information should be stored.

The count must survive between function calls.

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

- The maximum number of calls is one
- Multiple functions use different limits
- The request limit has already been reached

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about protecting limited resources?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Reset the request count after a period of time
- Display the remaining number of allowed requests
- Raise an exception when the limit is exceeded
- Collect usage statistics

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Many external APIs enforce request limits to protect infrastructure and ensure fair usage. Developers frequently build reusable rate-limiting solutions to prevent applications from exceeding those limits and triggering service errors.

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
solutions/32-rate-limited-service.py
```