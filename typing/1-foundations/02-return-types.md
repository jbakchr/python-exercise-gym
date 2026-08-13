# Exercise 02 - Return Types

## Progression

```text
✅ 01 Basic Parameter Types
➡️ 02 Return Types
⬜ 03 Multiple Parameters
⬜ Future Exercises
```

---

## Goal

Learn how to:

```text
Add return type annotations to functions.
```

By the end of this exercise you should understand:

- How to annotate return values
- Why return types are useful
- How parameter types and return types work together

---

## Why This Matters

In Exercise 01, you learned how to describe the values a function receives.

The next question is:

```text
What kind of value does the function give back?
```

Return type annotations answer that question.

For example:

```python
def square(number: int) -> int:
    return number * number
```

From the function signature alone, you can see:

```text
Input:
int

Output:
int
```

This makes functions easier to understand without reading their implementation.

Future exercises will build on this idea when working with:

```text
Optional values
Union types
Collections
Type aliases
More complex data structures
```

---

## Prerequisites

```text
Complete Exercise 01 first.
```

You should already be comfortable adding type annotations to function parameters.

---

## New Concept

Return type annotations are written after the parameter list.

Example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

The annotation:

```python
-> str
```

means:

```text
This function returns a string.
```

Together, parameter and return annotations describe the full contract of a function.

---

## Challenge

Create the following functions.

### greet

Accepts:

```python
name: str
```

Returns:

```python
str
```

containing a greeting message.

---

### double

Accepts:

```python
number: int
```

Returns:

```python
int
```

containing the doubled value.

---

### apply_discount

Accepts:

```python
price: float
```

Returns:

```python
float
```

containing the price after subtracting 10%.

---

### is_adult

Accepts:

```python
age: int
```

Returns:

```python
bool
```

indicating whether the age is at least 18.

Store the returned values in variables and print them.

---

## Requirements

Your solution must:

- Create all four functions
- Add parameter type annotations
- Add return type annotations
- Return values instead of printing inside the functions
- Print the returned values outside the functions

Do not:

- Use Optional
- Use Union
- Import anything from `typing`

---

## Starter Code

```python
def greet(name):
    pass


def double(number):
    pass


def apply_discount(price):
    pass


def is_adult(age):
    pass


# Call the functions here
# Store the returned values
# Print the returned values
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Hello, Alice
20
18.0
True
```

The exact values may differ.

You should also be able to explain:

```text
The difference between a parameter type annotation
and a return type annotation.
```

---

## Hints

### Hint 1

Return type annotations appear after the closing parenthesis.

Pattern:

```python
def function_name(parameter: type) -> type:
```

---

### Hint 2

Use the `return` keyword.

Example:

```python
return value
```

---

### Hint 3

One function signature should look similar to:

```python
def double(number: int) -> int:
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change the return values and observe how the annotations remain the same.

---

### Try 2

Create a new function that accepts a float and returns a float.

---

### Try 3

Look at the function signatures and see if you can understand what each function does without reading its implementation.

---

## Reflection

Answer these questions:

1. What does a return type annotation describe?
2. Why is it useful to know what a function returns?
3. How do parameter annotations differ from return annotations?
4. Could you understand a function more quickly if both are present?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
to_uppercase
```

that accepts:

```python
text: str
```

and returns:

```python
str
```

containing the uppercase version of the text.

---

## Real-World Connection

Return type annotations appear throughout modern Python code.

Examples include:

```text
FastAPI endpoints

Configuration loaders

Data processing pipelines

Testing utilities

CLI applications

Open-source libraries
```

Being able to quickly understand what a function returns is a key part of reading professional Python code.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All four functions are implemented
- [ ] Every parameter has a type annotation
- [ ] Every function has a return type annotation
- [ ] The functions return values instead of printing them
- [ ] You understand the purpose of `-> type`

---

## Solution

See:

```text
solutions/02-return-types.py
```