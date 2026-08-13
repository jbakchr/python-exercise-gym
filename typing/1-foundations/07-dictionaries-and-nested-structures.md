# Exercise 07 - Dictionaries and Nested Structures

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
✅ 03 Multiple Parameters
✅ 04 Optional Values
✅ 05 Union Types
✅ 06 Lists and Collections
➡️ 07 Dictionaries and Nested Structures
⬜ 08 Type Aliases
```

---

## Goal

Learn how to:

```text
Annotate dictionaries and nested data structures.
```

By the end of this exercise you should understand:

- How to annotate dictionaries
- How to describe key types and value types
- How nested collections can be typed
- How complex data structures can be documented through type annotations

---

## Why This Matters

Real-world applications rarely work with isolated values.

Instead, they often work with structured data such as:

```text
User records

Configuration settings

API responses

Database results

Application state
```

For example:

```python
user = {
    "name": "Alice",
    "age": 30,
}
```

Without type annotations, it may not be obvious what structure is expected.

With typing:

```python
dict[str, str]
```

or

```python
dict[str, int]
```

the intent becomes clearer.

As applications grow, clear data structure definitions become increasingly important.

Future exercises will build upon this idea when working with:

```text
Type Aliases
TypedDict
Real-world models
Reusable type definitions
```

---

## Prerequisites

```text
Complete Exercise 06 first.
```

You should already understand:

- Parameter annotations
- Return annotations
- Optional values
- Union types
- Collection types

---

## New Concept

A dictionary annotation describes:

```text
The type of keys

and

The type of values
```

Example:

```python
dict[str, str]
```

means:

```text
Keys are strings

Values are strings
```

---

Another example:

```python
dict[str, int]
```

means:

```text
Keys are strings

Values are integers
```

---

Collections can also be nested.

Example:

```python
list[dict[str, str]]
```

means:

```text
A list

containing dictionaries

whose keys are strings

and whose values are strings
```

---

## Challenge

Create the following functions.

### get_user_age

Accepts:

```python
user: dict[str, int]
```

Returns:

```python
int
```

Return the value associated with:

```python
"age"
```

---

### count_settings

Accepts:

```python
settings: dict[str, str]
```

Returns:

```python
int
```

Return the number of settings.

---

### get_first_user

Accepts:

```python
users: list[dict[str, str]]
```

Returns:

```python
dict[str, str]
```

Return the first user.

You may assume the list is not empty.

---

### create_server_config

Accepts:

```python
host: str
port: int
```

Returns:

```python
dict[str, str | int]
```

Return a dictionary containing:

```text
host
port
```

---

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Use dictionary type annotations
- Use nested collection type annotations
- Use parameter and return type annotations
- Return values instead of printing inside the functions
- Call every function and print the results

Do not:

- Use TypedDict yet
- Use custom types
- Introduce advanced typing concepts

---

## Starter Code

```python
def get_user_age(user):
    pass


def count_settings(settings):
    pass


def get_first_user(users):
    pass


def create_server_config(host, port):
    pass


# Call the functions here
# Store returned values
# Print results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
30
3
{'name': 'Alice'}
{'host': 'localhost', 'port': 8000}
```

The exact values may differ.

You should also be able to explain:

```text
What dict[str, int] means.

What list[dict[str, str]] means.

How nested type annotations describe data structures.
```

---

## Hints

### Hint 1

Dictionary annotations use:

```python
dict[key_type, value_type]
```

---

### Hint 2

Example:

```python
dict[str, int]
```

means:

```text
String keys
Integer values
```

---

### Hint 3

Nested structures can be combined.

Example:

```python
list[dict[str, str]]
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Add more keys to the dictionaries.

---

### Try 2

Create a function that works with:

```python
dict[str, float]
```

---

### Try 3

Create a function that accepts:

```python
list[dict[str, int]]
```

and returns the total of all ages.

---

## Reflection

Answer these questions:

1. Why is `dict[str, int]` more useful than simply `dict`?
2. What information do key and value types provide?
3. How does `list[dict[str, str]]` describe a nested data structure?
4. Why are nested type annotations valuable in larger applications?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
create_product
```

that returns:

```python
dict[str, str | float]
```

containing product information such as name and price.

---

## Real-World Connection

Dictionary annotations appear throughout modern Python applications.

Examples include:

```text
Configuration files

API responses

JSON data

Database records

Application settings

Automation scripts
```

Many real-world systems pass dictionaries between functions, making clear type annotations extremely valuable.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All four functions are implemented
- [ ] You can annotate dictionaries
- [ ] You can annotate nested collections
- [ ] You understand both key and value types
- [ ] You can read and understand complex collection annotations

---

## Solution

See:

```text
solutions/07-dictionaries-and-nested-structures.py
```