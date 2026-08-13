# Exercise 08 - Type Aliases

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
✅ 04 Optional Values
✅ 05 Union Types
✅ 06 Lists and Collections
✅ 07 Dictionaries and Nested Structures
➡️ 08 Type Aliases
⬜ 09 Annotating Real Functions
```

---

## Goal

Learn how to:

```text
Create reusable names for complex type annotations.
```

By the end of this exercise you should understand:

- What a type alias is
- Why type aliases improve readability
- How type aliases reduce repetition
- When type aliases are useful

---

## Why This Matters

As type annotations become more complex, they can become difficult to read.

For example:

```python
list[dict[str, str]]
```

is understandable.

However, after seeing it repeatedly throughout a codebase:

```python
def save_users(users: list[dict[str, str]]):
    ...

def load_users() -> list[dict[str, str]]:
    ...

def validate_users(users: list[dict[str, str]]):
    ...
```

the type annotation starts to become noisy.

A type alias allows us to give that structure a meaningful name.

Example:

```python
UserList = list[dict[str, str]]
```

Now the code becomes:

```python
def save_users(users: UserList):
    ...
```

which is easier to read and understand.

Type aliases become increasingly valuable as applications grow.

---

## Prerequisites

```text
Complete Exercise 07 first.
```

You should already understand:

- Collections
- Dictionaries
- Nested type annotations
- Function annotations

---

## New Concept

A type alias creates a reusable name for an existing type.

Example:

```python
UserId = int
```

Now:

```python
def get_user(user_id: UserId):
    ...
```

means exactly the same thing as:

```python
def get_user(user_id: int):
    ...
```

but communicates intent more clearly.

Type aliases are especially useful for:

```text
Complex collection types

Nested structures

Common business concepts

Shared application models
```

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
UserList = list[dict[str, str]]
```

---

Use these aliases in the following functions.

### create_username

Accepts:

```python
name: UserName
```

Returns:

```python
UserName
```

Return the supplied name.

---

### create_user

Accepts:

```python
name: UserName
```

Returns:

```python
UserRecord
```

Return a dictionary containing:

```text
name
```

---

### get_first_user

Accepts:

```python
users: UserList
```

Returns:

```python
UserRecord
```

Return the first user.

You may assume the list is not empty.

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

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Create all required type aliases
- Use type aliases in function signatures
- Avoid repeating complex type annotations
- Use return type annotations
- Call every function and print the results

Do not:

- Use TypedDict
- Use custom classes
- Introduce any new typing concepts

---

## Starter Code

```python
# Create your type aliases here


def create_username(name):
    pass


def create_user(name):
    pass


def get_first_user(users):
    pass


def count_users(users):
    pass


# Call the functions here
# Store returned values
# Print results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Alice
{'name': 'Alice'}
{'name': 'Alice'}
2
```

The exact values may differ.

You should also be able to explain:

```text
Why a type alias can make code easier to read.
```

---

## Hints

### Hint 1

A type alias is just a variable assignment.

Example:

```python
UserId = int
```

---

### Hint 2

You can create aliases for complex types.

Example:

```python
UserList = list[dict[str, str]]
```

---

### Hint 3

Once an alias exists, use it everywhere instead of the original type.

Example:

```python
def get_users() -> UserList:
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create an alias for:

```python
dict[str, int]
```

---

### Try 2

Create an alias for:

```python
list[str]
```

---

### Try 3

Refactor one of your previous exercises to use a type alias.

---

## Reflection

Answer these questions:

1. What problem do type aliases solve?
2. How do aliases improve readability?
3. When does a type alias become more useful?
4. Why might a project prefer `UserList` over `list[dict[str, str]]`?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a new alias called:

```python
ServerConfig
```

representing:

```python
dict[str, str | int]
```

and use it in a small function.

---

## Real-World Connection

Type aliases appear throughout professional Python code.

Examples include:

```text
API models

Configuration structures

Database records

Application settings

Library development

Large Python applications
```

They help developers communicate intent and reduce repetition when working with complex types.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All required aliases are created
- [ ] Function signatures use aliases instead of raw types
- [ ] You understand why aliases improve readability
- [ ] You can create aliases for nested structures
- [ ] You can explain when aliases are useful

---

## Solution

See:

```text
solutions/08-type-aliases.py
```