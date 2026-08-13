# Exercise 06 - Lists and Collections

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
✅ 04 Optional Values
✅ 05 Union Types
➡️ 06 Lists and Collections
⬜ 07 Dictionaries and Nested Structures
```

---

## Goal

Learn how to:

```text
Annotate collections that contain multiple values.
```

By the end of this exercise you should understand:

- How to annotate lists
- How to annotate sets
- How to annotate tuples
- How collection type annotations describe contained values
- Why collection annotations improve readability

---

## Why This Matters

Most real-world applications work with groups of values.

Examples:

```text
A list of usernames

A set of permissions

A tuple representing coordinates

A collection of products

A collection of file paths
```

Without type annotations:

```python
def process_users(users):
    ...
```

we don't know:

```text
What kind of collection is expected?

What kinds of values are inside it?
```

With type annotations:

```python
def process_users(users: list[str]):
    ...
```

the intent becomes much clearer.

We now know:

```text
users is a list

Each item is a string
```

This becomes increasingly valuable as programs grow larger.

---

## Prerequisites

```text
Complete Exercise 05 first.
```

You should already understand:

- Parameter annotations
- Return annotations
- Optional values
- Union types

---

## New Concept

Collection type annotations describe both:

```text
The collection type

and

The type of values stored inside it
```

Examples:

```python
list[str]
```

```text
A list containing strings
```

---

```python
set[str]
```

```text
A set containing strings
```

---

```python
tuple[int, int]
```

```text
A tuple containing two integers
```

---

Example:

```python
def count_names(names: list[str]) -> int:
    return len(names)
```

This tells us:

```text
names is a list

every item inside the list is a string

the function returns an integer
```

---

## Challenge

Create the following functions.

### count_names

Accepts:

```python
names: list[str]
```

Returns:

```python
int
```

containing the number of names.

---

### get_first_score

Accepts:

```python
scores: list[int]
```

Returns:

```python
int
```

containing the first score.

You may assume the list is not empty.

---

### count_permissions

Accepts:

```python
permissions: set[str]
```

Returns:

```python
int
```

containing the number of permissions.

---

### create_coordinate

Accepts:

```python
x: int
y: int
```

Returns:

```python
tuple[int, int]
```

containing both values.

---

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Use collection type annotations
- Use `list[str]`
- Use `list[int]`
- Use `set[str]`
- Use `tuple[int, int]`
- Use return type annotations on all functions
- Call every function and print the results

Do not:

- Import anything from `typing`
- Use dictionaries yet
- Introduce new typing concepts

---

## Starter Code

```python
def count_names(names):
    pass


def get_first_score(scores):
    pass


def count_permissions(permissions):
    pass


def create_coordinate(x, y):
    pass


# Call the functions here
# Store returned values
# Print results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
3
95
2
(10, 20)
```

The exact values may differ.

You should also be able to explain:

```text
What list[str] means.

What set[str] means.

What tuple[int, int] means.
```

---

## Hints

### Hint 1

A list annotation looks like:

```python
list[str]
```

---

### Hint 2

A set annotation looks like:

```python
set[str]
```

---

### Hint 3

A tuple annotation looks like:

```python
tuple[int, int]
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create a function that accepts:

```python
list[float]
```

---

### Try 2

Create a function that returns:

```python
tuple[str, int]
```

---

### Try 3

Change the values in your collections and verify that the type annotations stay the same.

---

## Reflection

Answer these questions:

1. Why is `list[str]` more informative than simply `list`?
2. What information does `set[str]` provide?
3. How does `tuple[int, int]` describe the structure of a value?
4. Why are collection type annotations useful in larger projects?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
calculate_average
```

that accepts:

```python
list[float]
```

and returns:

```python
float
```

containing the average value.

---

## Real-World Connection

Collection type annotations appear throughout modern Python code.

Examples include:

```text
API responses

Configuration data

Database records

Data processing pipelines

CLI applications

Automation scripts
```

Being able to describe collections clearly is one of the most common uses of Python's typing system.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All four functions are implemented
- [ ] You can use list type annotations
- [ ] You can use set type annotations
- [ ] You can use tuple type annotations
- [ ] You understand how collection annotations describe contained values

---

## Solution

See:

```text
solutions/06-lists-and-collections.py
```