# Decorators

Learn decorators through deliberate practice.

The goal of this topic is not simply to understand what decorators are, but to become comfortable creating and using them in real-world Python projects.

By the end of this exercise path, you should be able to:

- Understand how decorators work
- Create your own decorators
- Handle arguments and return values
- Build decorators with configuration
- Combine multiple decorators
- Solve practical problems using decorators
- Recognize common decorator patterns used in professional Python code

---

## What Are Decorators?

A decorator is a function that takes another function and extends or modifies its behavior without changing the original function's code. Decorators are commonly used for logging, timing, caching, validation, authentication, and many other cross-cutting concerns. 【1-8c76ff】【2-3f3ec6】

A simple example:

```python
def announce(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@announce
def greet():
    print("Hello")


greet()
```

Output:

```text
Before
Hello
After
```

Decorators are built on top of Python's ability to treat functions as first-class objects and often use a nested wrapper function to add behavior around an existing function. 【1-8c76ff】【3-894633】

---

## Exercise Philosophy

The exercises in this topic are designed to build on each other.

Instead of learning many decorator concepts at once, every exercise introduces one new idea while reinforcing previous knowledge.

```text
Exercise 01
↓
Exercise 02 requires Exercise 01

Exercise 03 requires Exercise 01 + 02

Exercise 04 requires Exercise 01 + 02 + 03

...
```

Knowledge accumulates.

Nothing is thrown away.

---

## Structure

```text
decorators/
│
├── 1-foundations/
├── 2-exploration/
├── 3-manipulation/
├── 4-problem-solving/
├── 5-mini-project/
└── README.md
```

Each stage introduces new concepts and new challenges.

---

## 1. Foundations

Goal:

```text
Understand basic decorator syntax.
```

Topics include:

- Functions as objects
- Simple wrappers
- Using the `@decorator` syntax
- Decorating functions without arguments
- Before/after execution behavior

Example exercises:

```text
01 Wrap a function
02 Print before execution
03 Print before and after execution
```

---

## 2. Exploration

Goal:

```text
Understand how decorators behave in different situations.
```

Topics include:

- Function arguments
- Keyword arguments
- Return values
- Flexible wrappers using `*args` and `**kwargs`

Example exercises:

```text
04 Handle positional arguments
05 Handle keyword arguments
06 Preserve return values
```

---

## 3. Manipulation

Goal:

```text
Use decorators to solve useful problems.
```

Topics include:

- Timing functions
- Counting calls
- Logging execution
- Debugging outputs

Example exercises:

```text
07 Timer decorator
08 Call counter
09 Logger decorator
```

---

## 4. Problem Solving

Goal:

```text
Apply decorators to realistic scenarios.
```

Topics include:

- Retry logic
- Caching
- Validation
- Decorator composition

Example exercises:

```text
10 Retry on failure
11 Cache results
12 Validate inputs
```

---

## 5. Mini Project

Goal:

```text
Combine everything learned throughout the topic.
```

Example project:

```text
Decorator Toolkit
```

Possible features:

```python
@timer
@retry
@cache
@debug
```

The project should require knowledge from all previous sections.

---

## Recommended Workflow

For each exercise:

1. Read the challenge.
2. Attempt a solution without looking at hints.
3. Experiment with your own variations.
4. Refactor your solution.
5. Compare with the provided solution.
6. Move on only when the concept feels comfortable.

---

## Mastery Checklist

Before leaving this topic, you should be able to confidently explain:

- [ ] What a decorator is
- [ ] Why wrapper functions are needed
- [ ] How `@decorator` syntax works
- [ ] How `*args` and `**kwargs` are used in decorators
- [ ] How to preserve return values
- [ ] How to create configurable decorators
- [ ] How multiple decorators interact
- [ ] When decorators are a good solution
- [ ] When decorators make code harder to understand

If you can build the mini project without referring to previous exercises, you've likely achieved a solid working understanding of decorators.

---

## Remember

The goal is not to memorize decorator syntax.

The goal is to reach the point where, when you need logging, retry logic, timing, caching, or validation in one of your own projects, your instinct is:

> "This could be a decorator."