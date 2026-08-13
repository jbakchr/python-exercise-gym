# Exercise 09 - Annotating Real Functions

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
➡️ 09 Annotating Real Functions
⬜ 10 Build a Typed Utility
```

---

## Goal

Learn how to:

```text
Apply type annotations to realistic utility functions.
```

By the end of this exercise you should understand:

- How multiple typing concepts work together
- How type annotations appear in real code
- How type aliases improve readability
- How function signatures communicate intent

---

## Why This Matters

So far, each exercise has focused on one specific typing concept.

Real-world functions rarely use just one concept.

A typical function may use:

```text
Multiple parameters

Collection types

Type aliases

Return types

Optional values
```

at the same time.

For example:

```python
def find_user(
    users: UserList,
    username: UserName,
) -> Optional[UserRecord]:
    ...
```

This function combines many ideas from previous exercises.

The goal of this exercise is to begin working with realistic function signatures similar to those found in professional Python projects.

---

## Prerequisites

```text
Complete Exercise 08 first.
```

You should already understand:

- Parameter annotations
- Return annotations
- Optional
- Union
- Collections
- Dictionaries
- Type aliases

---

## New Concept

Real-world typing often combines multiple concepts.

Example:

```python
UserName = str
UserRecord = dict[str, str]
UserList = list[UserRecord]
```

```python
def create_user(name: UserName) -> UserRecord:
    return {"name": name}
```

Notice how:

```text
Type aliases

Function parameters

Return types

Dictionaries
```

work together to create a clear and readable function signature.

---

## Challenge

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

Use these aliases in the following functions.

### create_user

Accepts:

```python
name: UserName
```

Returns:

```python
UserRecord
```

Return:

```python
{"name": name}
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

Return the matching user if found.

Otherwise return:

```python
None
```

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

Return the number of users.

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

Return a list containing all usernames.

---

Create a small collection of users.

Call all functions and print the returned values.

---

## Requirements

Your solution must:

- Create all required type aliases
- Use `Optional`
- Use collection type annotations
- Use type aliases in function signatures
- Return values instead of printing inside functions
- Call all functions and print the results

Do not:

- Use TypedDict
- Create classes
- Introduce new typing concepts

---

## Starter Code

```python
from typing import Optional


# Create aliases here


def create_user(name):
    pass


def find_user(users, name):
    pass


def count_users(users):
    pass


def get_user_names(users):
    pass


# Create some users
# Call the functions
# Print the results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
{'name': 'Alice'}

{'name': 'Bob'}

3

['Alice', 'Bob', 'Charlie']
```

The exact values may differ.

You should also be able to explain:

```text
How multiple typing concepts can be combined
to create clear and useful function signatures.
```

---

## Hints

### Hint 1

Reuse the type aliases from Exercise 08.

---

### Hint 2

The search function should return:

```python
Optional[UserRecord]
```

because a matching user may not exist.

---

### Hint 3

Loop through the users and compare names.

If no match is found:

```python
return None
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Search for a user that does not exist.

Observe the returned value.

---

### Try 2

Add additional fields to each user dictionary.

Examples:

```text
email

city

department
```

---

### Try 3

Modify the aliases and see how the function signatures become easier or harder to read.

---

## Reflection

Answer these questions:

1. Which typing concepts were combined in this exercise?
2. Why are type aliases useful in larger functions?
3. Why is `Optional` appropriate for `find_user`?
4. How do typed function signatures improve readability?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
remove_user
```

that accepts:

```python
users: UserList
name: UserName
```

and returns:

```python
UserList
```

containing all users except the removed user.

---

## Real-World Connection

Functions like these appear in many Python applications.

Examples include:

```text
CLI tools

Web applications

Configuration systems

Business applications

Automation scripts

Internal developer tools
```

The ability to combine multiple typing concepts into clear function signatures is one of the most valuable practical skills in modern Python development.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All required aliases are created
- [ ] All functions use type annotations
- [ ] Optional is used correctly
- [ ] Collection types are used correctly
- [ ] You understand how multiple typing concepts work together
- [ ] Function signatures feel easier to read and understand

---

## Solution

See:

```text
solutions/09-annotating-real-functions.py
```