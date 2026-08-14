# Exercise 25 - Typed Validation Helpers

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
✅ Exercise 23 - Typed API Responses
✅ Exercise 24 - Generic Container
➡️ Current Manipulation Exercise
⬜ Exercise 26 - Reusable Type Utilities
```

---

## Goal

Use:

```text
Type Aliases
TypedDict
Literal
Callable
Function Type Annotations
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable typed validation helper.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Function parameter and return types
- Type aliases
- Literal
- TypedDict
- Callable
- Generics
- Reusable utility design

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are building a registration system.

Before accepting data, you must validate it.

For example:

```text
Usernames cannot be empty.

Email addresses must contain "@".

Passwords must have a minimum length.
```

Without reusable validation helpers, the same validation logic often becomes scattered throughout an application.

Instead, you want to define validation functions and a utility that can execute them consistently.

The goal is to create a small reusable validation framework using Python's typing system.

---

## Challenge

Build a solution that:

1. Defines a reusable validator type.
2. Accepts validation functions.
3. Executes a validator against a value.
4. Returns whether the value is valid.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type alias named:

```python
Validator
```

- Use:

```python
Callable
```

to describe a validation function

- A validator should:

```python
Accept a string
Return a bool
```

- Create a function:

```python
def validate(value: str, validator: Validator) -> bool:
```

that runs the validator against the value

- Create at least one validator function named:

```python
is_not_empty
```

- Demonstrate the validation helper using a sample value

Your solution should not:

- Use `Any`
- Duplicate validation logic
- Hardcode validation results

---

## Starter Code

```python
from typing import Callable


# Create a Validator type alias


def is_not_empty(value):
    pass


def validate(value, validator):
    pass


print(validate("alice", is_not_empty))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Accept a validation function.
Run the validation function.
Return the validation result.
Reuse the same helper for different validators.
```

Expected output:

```text
True
```

You should also be able to explain:

- Why Callable is useful
- Why validator functions are reusable
- How typing improves validation helpers
- How the design could grow in a larger application

---

## Hints

### Hint 1

A validator is simply a function.

Think about the signature:

```python
Callable[[str], bool]
```

---

### Hint 2

The helper function should execute the validator passed to it.

---

### Hint 3

Your validation helper should not know how validation works.

It should only run the validator.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding more validator functions
- Email validation
- Password validation
- Username validation
- Chaining multiple validators together

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does a validation helper solve?
2. Why is Callable useful in this exercise?
3. How does this design promote code reuse?
4. Where might you use validator functions in a real application?

---

## Stretch Goal

Extend the utility with one additional feature.

Create another validator:

```python
def contains_at_symbol(value: str) -> bool:
```

and use it with the same validation helper.

---

## Real-World Connection

This pattern appears in:

- User registration systems
- Form validation
- API request validation
- Configuration validation
- Data processing pipelines

Developers frequently separate validation logic from business logic.

Typed validation helpers make validation easier to reuse, test, and maintain while clearly documenting the expected validator function signature.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `Validator` type alias is implemented
- [ ] `Callable` is used correctly
- [ ] `is_not_empty()` works correctly
- [ ] `validate()` works correctly
- [ ] Validator logic is reusable
- [ ] You understand the purpose of `Callable`
- [ ] You can explain how this pattern improves maintainability

---

## Solution

See:

```text
solutions/25-typed-validation-helpers.py
```