# Mini Project

## Overview

The Mini Project stage is the final challenge of the Decorators topic.

Everything you have learned throughout:

- Foundations
- Exploration
- Manipulation
- Problem Solving

comes together here.

Unlike the previous exercises, the goal is no longer to learn a specific decorator concept.

The goal is to demonstrate that you can apply decorator knowledge independently to build something useful.

This project should feel closer to a real software development task than a guided exercise.

There is no single correct solution.

Focus on creating a solution that is:

- Readable
- Reusable
- Well-structured
- Easy to extend

---

## Learning Goals

By completing this mini project, you should be able to:

- Design multiple decorators from scratch
- Combine decorators effectively
- Create reusable solutions
- Apply decorators to real-world scenarios
- Structure decorator-based code cleanly
- Understand decorator trade-offs
- Confidently use decorators in future projects

---

## What You Will Practice

Topics covered in this stage:

- Decorator design
- Wrapper functions
- `*args` and `**kwargs`
- Return value handling
- Function metadata preservation
- State management
- Configurable decorators
- Decorator composition
- Real-world use cases

---

## Recommended Approach

As with earlier exercises:

1. Start simple.
2. Build one feature at a time.
3. Test frequently.
4. Refactor often.
5. Focus on readability.
6. Prefer simple solutions over clever solutions.

Remember:

```text
The goal is not to build the perfect project.

The goal is to prove that you understand decorators.
```

---

## Mini Project

### 41 Decorator Toolkit

Build a reusable toolkit of practical decorators.

Your toolkit should provide functionality that could realistically be reused across multiple projects.

Examples include:

```python
@timer
@debug
@retry
@cache
@validate
@count_calls
```

You do not need to implement every possible decorator.

The goal is to combine concepts learned throughout this topic and create something useful.

---

## Suggested Features

Consider implementing some or all of the following:

### Timer

Measure execution time.

Example:

```python
@timer
def process_data():
    ...
```

---

### Debug

Display function calls and arguments.

Example:

```python
@debug
def greet(name):
    ...
```

---

### Retry

Retry failed operations.

Example:

```python
@retry(max_attempts=3)
def fetch_data():
    ...
```

---

### Cache

Store previous function results.

Example:

```python
@cache
def expensive_calculation():
    ...
```

---

### Validation

Validate incoming arguments.

Example:

```python
@positive_numbers_only
def divide(a, b):
    ...
```

---

### Call Counter

Track how many times a function is executed.

Example:

```python
@count_calls
def save_file():
    ...
```

---

## Suggested Project Structure

```text
decorator-toolkit/
│
├── decorators.py
├── examples.py
├── tests.py
└── README.md
```

Feel free to create a different structure if it better suits your solution.

---

## Stretch Goals

If you want an additional challenge:

### Stretch Goal 1

Allow decorators to be configured with arguments.

Example:

```python
@retry(max_attempts=5)
```

---

### Stretch Goal 2

Combine multiple decorators on the same function.

Example:

```python
@debug
@timer
@retry(max_attempts=3)
def process_data():
    ...
```

---

### Stretch Goal 3

Use `functools.wraps()` everywhere appropriate.

---

### Stretch Goal 4

Create documentation for your toolkit.

---

### Stretch Goal 5

Add automated tests.

---

## Reflection

After completing this project, answer the following questions:

1. Which decorator was easiest to implement?
2. Which decorator was most difficult?
3. What concepts do decorators rely on internally?
4. How did combining multiple decorators affect execution?
5. What would you improve if starting over?
6. Which decorators would be genuinely useful in your own projects?
7. Could you explain decorators to another developer without using notes?

---

## Success Criteria

You can consider the Decorators topic complete when:

- [ ] The toolkit functions correctly
- [ ] Multiple decorators have been implemented
- [ ] Decorators can handle arguments correctly
- [ ] Return values are preserved correctly
- [ ] Function metadata is preserved where appropriate
- [ ] The code is readable and maintainable
- [ ] You understand every line of code
- [ ] You can create a new decorator without consulting earlier exercises

---

## What Comes Next?

After completing Decorators, consider exploring:

```text
context-managers
```

to learn another powerful Python mechanism for controlling behavior around blocks of code.

or

```text
generators
```

to learn how Python handles lazy and efficient data processing.

or

```text
typing
```

to improve code clarity, tooling support, and maintainability.

Each of these topics builds naturally on the skills developed while working with decorators.

---

## Final Thought

The purpose of this project is not to memorize patterns.

The purpose is to reach the point where decorators feel like a natural tool in your Python toolbox.

When you notice repeated behavior across multiple functions, your instinct should be:

> "This might be a decorator."