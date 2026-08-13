# Exercise 33 - Expensive Calculations

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31 - Slow API Calls
✅ 32 - Rate Limited Service

➡️ Current Problem Solving Exercise

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
Caching Decorators
Function Arguments
Return Values
State Management
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A reporting system generates statistics for users.

Some calculations take a long time to complete.

Users frequently request the same reports using the same
inputs, causing the application to repeat identical work.

The development team wants to improve performance without
rewriting the calculation logic.
```

Example:

```text
A report for customer 123 requires several seconds to
generate.

If another user requests the same report immediately
afterwards, the entire calculation currently runs again.

The team would prefer to reuse previous results whenever
possible.
```

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Avoid repeating identical calculations
- Return previously generated results when appropriate
- Preserve the original function behaviour
- Improve performance for repeated requests

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Store caching logic inside every function
- Change the result returned by the function
- Require manual result tracking

---

## Example Usage

The completed solution should support behaviour similar to:

```python
generate_report("customer-123")

generate_report("customer-123")

generate_report("customer-456")

generate_report("customer-123")
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Generating report for customer-123...

Using cached result for customer-123

Generating report for customer-456...

Using cached result for customer-123
```

Repeated requests with the same input should avoid re-running the expensive calculation.

Requests with different inputs should still generate new results.

---

## Constraints

Consider the following constraints:

- Different arguments may produce different results
- Cached results should only be reused when appropriate
- Multiple functions may eventually require the same optimization

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
import time


def generate_report(customer_id):
    print(f"Generating report for {customer_id}...")

    time.sleep(2)

    return {
        "customer_id": customer_id,
        "score": 95
    }
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What work is being repeated unnecessarily?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Cache Decorator
State Management
Function Arguments
```

---

### Hint 3

Think about how previous results might be stored and reused.

The application should remember work it has already completed.

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

- Different arguments are provided
- The same argument is provided many times
- Multiple functions eventually require caching

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about performance optimization?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Limit the size of the cache
- Display cache statistics
- Clear old cache entries
- Cache results for multiple functions

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Many applications perform expensive calculations, database queries, API requests, or report generation tasks. Developers often use caching techniques to avoid repeating work that has already been completed, significantly improving system performance and responsiveness.

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
solutions/33-expensive-calculations.py
```