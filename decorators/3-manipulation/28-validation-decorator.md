# Exercise 28 - Validation Decorator

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
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and input validation
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable validation decorator that
checks function inputs before execution.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Flexible wrappers
- Return values
- Function arguments
- Positional arguments
- Keyword arguments
- Conditional logic
- Permission decorators

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Prevent invalid data from reaching
important business logic.
```

Example:

```text
A banking application should not allow
withdrawal amounts below zero.

A shopping system should not allow
negative quantities.

A reporting tool should reject invalid
numeric values.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Checks a value before function execution
2. Allows valid inputs to continue
3. Prevents invalid inputs from reaching the function
4. Keeps validation logic reusable

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `validate_positive`
- Verify that numeric values are positive
- Execute the function only when validation succeeds
- Display a message when validation fails
- Work with function arguments

Your solution should not:

- Duplicate validation code in every function
- Execute the function when validation fails

---

## Starter Code

```python
def validate_positive(func):
    pass


@validate_positive
def withdraw(amount):
    print(f"Withdrawing {amount}")


withdraw(100)
withdraw(-50)
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Allow valid values.

Reject invalid values.
```

Example:

```text
Withdrawing 100
```

Example:

```text
Validation Failed
Amount must be positive
```

Another example:

```python
@validate_positive
def add_points(points):
    print(f"Adding {points} points")
```

Output:

```text
Adding 25 points
```

and:

```text
Validation Failed
Points must be positive
```

You should also be able to explain:

- Why validation occurs before function execution
- Why invalid values should be blocked
- How validation logic can be reused

---

## Hints

### Hint 1

The wrapper can inspect function arguments before calling the original function.

---

### Hint 2

You may need a condition similar to:

```python
if amount <= 0:
```

before executing the function.

---

### Hint 3

If validation succeeds:

```python
return func(*args, **kwargs)
```

Otherwise:

```text
display a validation message
```

and stop execution.

---

## Possible Improvements

Once the basic solution works, consider:

- Supporting multiple validation rules
- Raising exceptions instead of displaying messages
- Validating keyword arguments
- Making the validation rule configurable
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why should validation occur before the function runs?
3. What happens when validation fails?
4. How does this approach reduce duplicated code?
5. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Allow the decorator to validate
a minimum value supplied by the user.
```

Example:

```python
@validate_minimum(10)
def process_score(score):
    ...
```

Or:

```text
Support multiple validation checks.
```

Example:

```text
Must be positive
Must be less than 100
```

---

## Real-World Connection

This pattern appears in:

- Banking systems
- E-commerce platforms
- APIs
- Form processing systems
- Data validation frameworks

Many applications must verify data before processing it. Rather than placing validation logic inside every function, developers often centralize the logic using decorators.

Validation helps protect systems from bad data and keeps business logic focused on its primary responsibility.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Valid values are accepted
- [ ] Invalid values are rejected
- [ ] The original function only executes when validation succeeds
- [ ] The decorator works with function arguments
- [ ] You understand how validation occurs inside a wrapper
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/28-validation-decorator.py
```