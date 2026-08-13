# Exercise 03 - Multiple Parameters

## Progression

```text
✅ 01 Basic Parameter Types
✅ 02 Return Types
➡️ 03 Multiple Parameters
⬜ 04 Optional Values
```

---

## Goal

Learn how to:

```text
Annotate functions that accept multiple parameters.
```

By the end of this exercise you should understand:

- How to annotate multiple parameters
- How different parameter types can work together
- How a complete function signature communicates intent

---

## Why This Matters

Most real-world functions do not accept a single value.

Instead, they often require multiple pieces of information.

For example:

```python
def create_user(name: str, age: int) -> str:
    ...
```

The function signature tells us:

```text
name should be a string
age should be an integer
the function returns a string
```

Without reading any implementation details, we already know how the function should be used.

As functions become larger and more complex, type annotations become increasingly valuable.

Future exercises will build upon this foundation when working with:

```text
Optional values
Union types
Collection types
Type aliases
Complex data structures
```

---

## Prerequisites

```text
Complete Exercise 02 first.
```

You should already understand:

- Parameter type annotations
- Return type annotations

---

## New Concept

Functions can have multiple parameters.

Each parameter can have its own type annotation.

Example:

```python
def introduce(name: str, age: int) -> str:
    return f"{name} is {age} years old."
```

Notice that each parameter has its own type:

```python
name: str
age: int
```

and the function also has a return type:

```python
-> str
```

Together, these form a complete description of the function's contract.

---

## Challenge

Create the following functions.

### create_full_name

Accepts:

```python
first_name: str
last_name: str
```

Returns:

```python
str
```

containing the full name.

---

### calculate_area

Accepts:

```python
width: float
height: float
```

Returns:

```python
float
```

containing the calculated area.

---

### create_login_message

Accepts:

```python
username: str
login_count: int
```

Returns:

```python
str
```

containing a message about the user's login activity.

---

### can_purchase

Accepts:

```python
age: int
has_permission: bool
```

Returns:

```python
bool
```

indicating whether the purchase is allowed.

---

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Create all four functions
- Use type annotations for every parameter
- Use a return type annotation for every function
- Return values instead of printing inside the functions
- Call all functions and print their results

Do not:

- Use Optional
- Use Union
- Import anything from `typing`

---

## Starter Code

```python
def create_full_name(first_name, last_name):
    pass


def calculate_area(width, height):
    pass


def create_login_message(username, login_count):
    pass


def can_purchase(age, has_permission):
    pass


# Call the functions here
# Store the returned values
# Print the results
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Alice Smith
12.0
alice has logged in 5 times.
True
```

The exact values may differ.

You should also be able to explain:

```text
How multiple parameter annotations help describe
what a function expects.
```

---

## Hints

### Hint 1

Each parameter needs its own annotation.

Example:

```python
name: str
age: int
```

---

### Hint 2

You can combine multiple annotated parameters like this:

```python
def example(name: str, age: int):
    ...
```

---

### Hint 3

A complete function signature includes:

```python
parameters
+
return type
```

Example:

```python
def example(name: str, age: int) -> str:
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Add an extra parameter to one of the functions.

---

### Try 2

Create a function that accepts three different types.

Example:

```python
str
int
bool
```

---

### Try 3

Read each function signature without looking at its body.

Can you predict what the function does?

---

## Reflection

Answer these questions:

1. Why is it useful to annotate each parameter individually?
2. What information can you learn from a function signature alone?
3. How do parameter annotations and return annotations work together?
4. Did you find the functions easier to understand with type hints?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
create_profile
```

that accepts:

```python
name: str
age: int
active: bool
```

and returns:

```python
str
```

containing a formatted profile description.

---

## Real-World Connection

Functions with multiple parameters appear everywhere in Python.

Examples include:

```text
Web APIs

CLI applications

Configuration systems

Data processing scripts

Testing helpers

Business applications
```

Type annotations make these function signatures easier to understand, use, and maintain.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All four functions are implemented
- [ ] Every parameter has a type annotation
- [ ] Every function has a return type annotation
- [ ] You can confidently annotate functions with multiple parameters
- [ ] You understand how a function signature communicates intent

---

## Solution

See:

```text
solutions/03-multiple-parameters.py
```