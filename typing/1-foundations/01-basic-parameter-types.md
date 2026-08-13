# Exercise 01 - Basic Parameter Types

## Progression

```text
✅ Start Here
➡️ 01 Basic Parameter Types
⬜ 02 Return Types
⬜ Future Exercises
```

---

## Goal

Learn how to:

```text
Add basic type annotations to function parameters.
```

By the end of this exercise you should understand:

- How to annotate function parameters
- How type hints describe expected values
- How type annotations improve code readability

---

## Why This Matters

When you read a function, one of the first questions you have is:

```text
What kind of values can I pass to it?
```

Type annotations allow developers to answer that question immediately.

For example:

```python
def greet(name: str):
    print(f"Hello, {name}")
```

Without looking at the implementation, you can already see that:

```text
name should be a string
```

This makes code easier to understand and use.

In future exercises, parameter annotations will become the foundation for:

```text
Return types
Optional values
Union types
Collection types
Type aliases
```

---

## Prerequisites

```text
None.
```

This is the first exercise in the typing topic.

---

## New Concept

Function parameters can be annotated with expected types.

Example:

```python
def greet(name: str):
    print(f"Hello, {name}")
```

The annotation:

```python
name: str
```

means:

```text
This function expects a string.
```

Python will still run even if the wrong type is passed.

Type hints are primarily intended to:

- Improve readability
- Improve editor support
- Help catch mistakes earlier

---

## Challenge

Create the following functions:

```python
greet
```

Accepts:

```python
name: str
```

and prints a greeting.

---

```python
double
```

Accepts:

```python
number: int
```

and prints the number multiplied by two.

---

```python
show_price
```

Accepts:

```python
price: float
```

and prints the price.

---

```python
show_status
```

Accepts:

```python
active: bool
```

and prints the value.

Your task is to focus on correctly annotating the parameters.

---

## Requirements

Your solution must:

- Create all four functions
- Use type annotations on every parameter
- Call every function at least once
- Produce output showing that each function works

Do not:

- Add return type annotations yet
- Import anything from `typing`
- Skip any of the required parameter types

---

## Starter Code

```python
def greet(name):
    pass


def double(number):
    pass


def show_price(price):
    pass


def show_status(active):
    pass


# Call your functions here
```

---

## Verify Your Solution

When your program runs successfully, you should see something similar to:

```text
Hello, Alice
20
19.99
True
```

The exact values may differ.

You should also be able to explain:

```text
How parameter annotations communicate the expected type
for a function argument.
```

Avoid looking ahead to return types.

This exercise focuses only on function parameters.

---

## Hints

### Hint 1

A type annotation is written after the parameter name.

Example pattern:

```python
parameter_name: type
```

---

### Hint 2

The built-in types you need are:

```python
str
int
float
bool
```

---

### Hint 3

Your first function should look similar to:

```python
def greet(name: str):
    ...
```

Use the same pattern for the remaining functions.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change the parameter names while keeping the type annotations.

---

### Try 2

Add another function using a string parameter.

Example:

```python
city: str
```

---

### Try 3

Hover over your functions in your editor and observe how the type information is displayed.

---

## Reflection

Answer these questions:

1. What information does a parameter type annotation provide?
2. Does Python enforce parameter types at runtime?
3. Why might type annotations be useful even if Python still runs without them?
4. Which type annotations did you use in this exercise?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a fifth function:

```python
calculate_area
```

that accepts:

```python
width: float
height: float
```

and prints the calculated area.

---

## Real-World Connection

Parameter type annotations appear throughout modern Python code.

Examples include:

```text
FastAPI applications

Data processing scripts

Automation tools

Open-source libraries

Testing code

Internal business applications
```

When reading professional Python projects, you'll frequently see function signatures that clearly describe the expected inputs through type annotations.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] All four functions are implemented
- [ ] Every parameter has a type annotation
- [ ] You understand what `str`, `int`, `float`, and `bool` annotations mean
- [ ] You can explain why parameter annotations improve readability

---

## Solution

See:

```text
solutions/01-basic-parameter-types.py
```