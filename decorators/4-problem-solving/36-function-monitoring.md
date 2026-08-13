# Exercise 36 - Function Monitoring

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

➡️ Current Problem Solving Exercise

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
Access Counters
State Management
Function Wrapping
Decorator Factories
Reusable Utilities
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
A team has developed an internal application used by
employees across the company.

Management wants to understand how the application
is being used.

They would like to know which features are being used
most frequently so they can prioritize future
improvements.

Currently, developers have no visibility into feature
usage.
```

Example:

```text
The application contains features such as:

- Generate Reports
- Export Data
- Create Users

Management asks:

"Which features are used most often?"

The development team needs a reusable solution that
tracks feature usage automatically.
```

The team wants to gather usage information without adding tracking code to every function.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

---

## Requirements

Your solution must:

- Track how many times a function has been executed
- Display usage information
- Work with multiple functions
- Preserve the original function behaviour

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Place counting logic inside every function
- Change the return value of wrapped functions
- Require manual tracking by developers

---

## Example Usage

The completed solution should support behaviour similar to:

```python
generate_report()
generate_report()
generate_report()

export_data()

show_usage()
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
generate_report: 3 calls

export_data: 1 call
```

The application should automatically collect usage information as functions are executed.

The original functions should continue working normally.

---

## Constraints

Consider the following constraints:

- Multiple functions may require monitoring
- New features may be added in the future
- Usage counts should persist during program execution

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def generate_report():
    print("Generating report...")


def export_data():
    print("Exporting data...")


def create_user():
    print("Creating user...")
```

---

## Hints

### Hint 1

Focus on the high-level problem first.

What information does management want to collect?

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Access Counter
State Management
Decorator Factories
```

---

### Hint 3

The application should collect information automatically.

Developers should not need to update counters manually.

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

- A function is never called
- A function is called many times
- Multiple functions use monitoring
- Additional monitored functions are added later

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which concepts were most useful?
3. Did you need to modify an earlier approach?
4. How would you improve the solution?
5. What did this exercise teach you about collecting usage data in software applications?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Display functions sorted by usage
- Track the most frequently used feature
- Store usage information in a file
- Display usage percentages

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Automation scripts
- Web services
- Frameworks

Many organizations collect feature-usage metrics to understand user behaviour and make better product decisions. Monitoring systems often track how frequently important features are used so teams can identify popular functionality, unused features, and opportunities for improvement.

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
solutions/36-function-monitoring.py
```