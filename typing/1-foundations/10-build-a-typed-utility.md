# Exercise 10 - Build a Typed Utility

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
✅ 04 Optional Values
✅ 05 Union Types
✅ 06 Lists and Collections
✅ 07 Dictionaries and Nested Structures
✅ 08 Type Aliases
✅ 09 Annotating Real Functions
➡️ 10 Build a Typed Utility
🏁 Foundations Complete
```

---

## Goal

Learn how to:

```text
Combine everything learned in the Foundations stage
to build a small typed utility.
```

By the end of this exercise you should understand:

- How typing concepts work together
- How type annotations improve utility functions
- How type aliases improve readability
- How Optional values fit into practical code
- How typed functions can form a small reusable tool

---

## Why This Matters

Real applications are not built from isolated functions.

Instead, multiple typed functions work together to solve a problem.

Throughout this Foundations stage, you have learned:

```text
Basic Types

Return Types

Multiple Parameters

Optional

Union

Collections

Dictionaries

Nested Structures

Type Aliases
```

This exercise combines those building blocks into a small utility.

The goal is not complexity.

The goal is integration.

This mirrors how typing is used in professional Python projects.

---

## Prerequisites

```text
Complete Exercise 09 first.
```

You should be comfortable with:

- Function annotations
- Collection annotations
- Optional values
- Type aliases
- Dictionaries
- Lists

---

## New Concept

There is no new typing feature in this exercise.

Instead, the focus is:

```text
Combining previously learned concepts.
```

This exercise acts as the capstone for the Foundations stage.

The goal is to reach the point where type annotations start feeling natural.

---

## Challenge

Build a small typed user directory utility.

Create the following type aliases.

### UserName

```python
UserName = str
```

---

### UserRecord

```python
UserRecord = dict[str, str]
```

---

### UserList

```python
UserList = list[UserRecord]
```

---

Create the following functions.

### create_user

Accepts:

```python
name: UserName
email: str
```

Returns:

```python
UserRecord
```

---

### find_user

Accepts:

```python
users: UserList
name: UserName
```

Returns:

```python
Optional[UserRecord]
```

Return the matching user.

Return:

```python
None
```

if no user exists.

---

### count_users

Accepts:

```python
users: UserList
```

Returns:

```python
int
```

---

### get_user_names

Accepts:

```python
users: UserList
```

Returns:

```python
list[UserName]
```

---

Create a small user directory containing at least three users.

Call all functions and print the results.

---

## Requirements

Your solution must:

- Create all required aliases
- Use type annotations everywhere
- Use Optional correctly
- Use collection types correctly
- Use return type annotations
- Create at least three users
- Call and demonstrate all functions

Do not:

- Use TypedDict
- Use classes
- Introduce any new typing concepts

Focus only on concepts learned during Foundations.

---

## Starter Code

```python
from typing import Optional


# Create aliases here


def create_user(name, email):
    pass


def find_user(users, name):
    pass


def count_users(users):
    pass


def get_user_names(users):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
{'name': 'Alice', 'email': 'alice@example.com'}

3

['Alice', 'Bob', 'Charlie']

{'name': 'Bob', 'email': 'bob@example.com'}
```

The exact values may differ.

You should also be able to explain:

```text
How multiple typing concepts work together
within a small utility.
```

---

## Hints

### Hint 1

Reuse ideas from Exercise 08 and Exercise 09.

---

### Hint 2

Use aliases to simplify function signatures.

Example:

```python
UserList
```

instead of:

```python
list[dict[str, str]]
```

---

### Hint 3

The search function should return:

```python
Optional[UserRecord]
```

because the requested user may not exist.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Search for a user that does not exist.

Observe the result.

---

### Try 2

Add another field such as:

```text
department
```

or

```text
city
```

to each user record.

---

### Try 3

Add additional utility functions using the same aliases.

---

## Reflection

Answer these questions:

1. Which typing concepts did you use in this exercise?
2. Which type annotations improved readability the most?
3. Why are type aliases useful in a small utility?
4. Why does `find_user()` return an Optional value?
5. Do typed function signatures feel more natural now than in Exercise 01?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
get_user_emails
```

that accepts:

```python
UserList
```

and returns:

```python
list[str]
```

containing all email addresses.

---

## Real-World Connection

Utilities like this appear in many Python applications.

Examples include:

```text
CLI Tools

Web Applications

Configuration Systems

Internal Business Tools

Automation Scripts

Developer Utilities
```

Most professional Python projects use many of the typing concepts introduced in this Foundations stage.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All required aliases are created
- [ ] All functions use type annotations
- [ ] Optional is used correctly
- [ ] Collection types are used correctly
- [ ] Type aliases are used consistently
- [ ] The utility works correctly
- [ ] You can explain every type annotation used

---

## Solution

See:

```text
solutions/10-build-a-typed-utility.py
```