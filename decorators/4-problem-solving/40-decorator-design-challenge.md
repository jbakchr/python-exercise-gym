# Exercise 40 - Decorator Design Challenge

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
✅ 39 - Background Task Tracking

➡️ Current Problem Solving Exercise

⬜ Mini Project
```

---

## Goal

Apply your understanding of:

```text
Timing Decorators
Caching Decorators
Logging Decorators
Debug Decorators
Validation Decorators
Permission Decorators
Decorator Composition
Decorator Design
```

to solve a realistic problem.

This exercise focuses on reasoning, design decisions, and applying previously learned techniques.

---

## Scenario

You are working on the following problem:

```text
You have joined a team that maintains an internal
business application.

The application already contains many functions,
but management has introduced several new requirements.

The team wants to:

- Monitor performance
- Track usage
- Validate incoming data
- Protect sensitive functionality
- Improve debugging
- Reduce duplicated code

You have learned many decorator techniques throughout
this topic.

Your task is to determine how those techniques can be
combined to solve the application's problems.
```

Example:

```text
Different functions have different concerns.

Some operations are expensive.

Some require validation.

Some require authorization.

Some need additional monitoring.

A single solution will not fit every situation.
```

The team needs someone who can evaluate requirements and choose appropriate solutions.

---

## Problem

Your task is to create a solution that satisfies the requirements below.

No single technique has been prescribed.

Part of the challenge is deciding how to apply the concepts you've already learned.

You must determine:

```text
Which decorators should be applied?

Which functions need them?

Can multiple decorators be combined?

Does decorator order matter?
```

This exercise is intentionally more open-ended than previous exercises.

---

## Requirements

Your solution must:

- Use decorators to address the application's requirements
- Apply decorators to multiple functions
- Demonstrate at least two situations where decorator choice matters
- Preserve the original behaviour of the application

Your solution should:

- Encourage clean code
- Avoid unnecessary duplication

Your solution must not:

- Place repeated monitoring, validation, or security logic directly inside functions
- Apply decorators without a clear reason
- Ignore the trade-offs introduced by your design

---

## Example Usage

The completed solution should support behaviour similar to:

```python
create_user("Alice")

generate_report("customer-123")

delete_user("admin")

delete_user("guest")
```

This demonstrates the desired outcome, not the implementation.

---

## Expected Behaviour

When the solution is working correctly:

```text
Validation occurs automatically.

Sensitive operations are protected.

Important operations are monitored.

Repeated work can be optimized.

Developers receive useful diagnostic information.
```

Different functions may behave differently depending on the decorators you choose.

---

## Constraints

Consider the following constraints:

- Different functions solve different problems
- Not every function needs the same decorators
- Multiple decorators may need to work together

These constraints are part of the problem.

Your solution should account for them.

---

## Starter Code

```python
def create_user(name):
    print(f"Creating user: {name}")


def generate_report(customer_id):
    print(f"Generating report for {customer_id}")


def delete_user(user_role):
    print("Deleting user...")


def calculate_statistics():
    print("Calculating statistics...")
```

---

## Hints

### Hint 1

Focus on the high-level problems first.

Do not start by choosing decorators.

Start by identifying application requirements.

---

### Hint 2

Consider which concepts from previous exercises may help.

Think about:

```text
Timing
Caching
Logging
Debugging
Validation
Permissions
Monitoring
```

---

### Hint 3

Some functions may benefit from more than one decorator.

Think carefully about whether decorators should be combined.

---

## Design Questions

As you work, consider:

1. Why did you choose each decorator?
2. Were there alternative solutions?
3. What trade-offs exist?
4. Does decorator order matter?
5. Which previous exercises influenced your design?

You do not need to formally answer these questions, but you should think about them.

---

## Edge Cases

Consider what happens when:

- Invalid data is provided
- Unauthorized users attempt restricted operations
- Expensive functions are called repeatedly
- Multiple decorators interact with one another

A robust solution should handle these situations appropriately.

---

## Reflection

Answer the following questions.

1. What made this problem challenging?
2. Which decorators were most useful?
3. Did you change your design while solving the problem?
4. What trade-offs did you encounter?
5. What did this exercise teach you about choosing solutions rather than simply implementing techniques?

---

## Stretch Goal

Extend your solution to support an additional requirement.

Examples:

- Introduce a new application feature
- Add additional monitoring
- Add new validation rules
- Support more advanced authorization requirements

The stretch goal should build upon the existing solution rather than replacing it.

---

## Real-World Connection

Problems like this appear in:

- Production applications
- Internal tools
- Enterprise software
- Web services
- Frameworks

Professional developers rarely create decorators in isolation. Instead, they evaluate requirements and apply decorators to solve cross-cutting concerns such as logging, monitoring, validation, security, caching, and debugging. Choosing the right solution is often more important than implementing the individual technique.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All requirements are satisfied
- [ ] The solution handles the important edge cases
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can identify alternative approaches
- [ ] You can justify why each decorator was chosen
- [ ] You feel prepared for the mini project

---

## Solution

See:

```text
solutions/40-decorator-design-challenge.py
```