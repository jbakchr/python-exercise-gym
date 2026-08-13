# Exercise 39 - Background Task Tracking

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete

✅ 31 - Slow API Calls
✅ 32 - Rate Limited Service
✅ 33 - Expensive Calculations
✅ 34 - Audit Trail System
✅ 35 - Production Debugging
✅ 36 - Function Monitoring
✅ 37 - Data Validation Pipeline
✅ 38 - Secure Operations

➡️ Current Problem Solving Exercise

⬜ 40 - Decorator Design Challenge

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Logging Decorators
Timing Decorators
Decorator Composition
Function Wrapping
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A Python application performs long-running background tasks.

Examples include:

- Generating reports
- Importing data
- Processing files
- Creating backups

Users often ask whether a task has started,
whether it has completed,
and how long it took to run.

Currently, developers add status messages and timing code
inside individual functions.

As the system grows, this approach is becoming repetitive
and difficult to maintain.
```

Example:

```text
A monthly report may take several seconds to generate.

Users want to see:

- When it starts
- When it finishes
- How long it took

without developers repeatedly writing the same code.
```

The development team wants a reusable solution that makes task execution easier to monitor.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Display when a task starts
- Display when a task finishes
- Display how long the task took to execute
- Preserve the original function behaviour

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Duplicate tracking logic inside every task function
- Change the return value of wrapped functions
- Mix monitoring concerns with business logic

---

## Example Usage

The completed solution should support behaviour similar to:

```python
generate_monthly_report()

backup_database()
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Starting generate_monthly_report...

Generating monthly report...

Finished generate_monthly_report

Execution time: 2.00 seconds
```

And:

```text
Starting backup_database...

Backing up database...

Finished backup_database

Execution time: 1.00 seconds
```

Developers should be able to monitor long-running tasks without modifying the task implementations themselves.

---

## Constraints

Consider the following constraints:

- Multiple background tasks may use the solution
- Some tasks may take longer than others
- Monitoring logic should remain separate from business logic

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
import time


def generate_monthly_report():
    print("Generating monthly report...")

    time.sleep(2)


def backup_database():
    print("Backing up database...")

    time.sleep(1)
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What visibility do users and developers need?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Timing Decorator
Logging Decorator
Decorator Composition
```

---

### Hint 3

You already built several decorators in previous exercises.

Could multiple decorators work together to solve this problem?

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

- A task completes very quickly
- Multiple tasks use the monitoring solution
- Additional background jobs are added later
- A task returns a value

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about monitoring long-running operations?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Display task arguments
- Display task return values
- Record task history
- Warn when tasks exceed a specified duration

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Data processing systems

Many systems perform scheduled jobs, report generation, backups, and data-processing tasks that can take significant time to complete. Developers often build reusable monitoring solutions that provide visibility into the lifecycle of these operations while keeping business logic clean and focused.

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
solutions/39-background-task-tracking.py
```