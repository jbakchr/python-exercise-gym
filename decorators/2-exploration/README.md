# Exploration

## Overview

The goal of the Exploration stage is to understand how decorators behave in more realistic situations.

In Foundations, you learned that decorators are simply functions that wrap other functions.

In this stage, you will explore how decorators interact with:

- Function arguments
- Keyword arguments
- Return values
- Multiple function signatures
- Function metadata
- Internal state

By the end of this stage, decorators should start feeling less like a special language feature and more like a natural extension of Python's function system.

---

## Learning Goals

By the end of this stage you should be able to:

- Decorate functions that accept arguments
- Decorate functions that accept keyword arguments
- Create decorators that work with any function signature
- Preserve return values correctly
- Understand how arguments flow through wrappers
- Store state inside decorators
- Preserve function metadata using `functools.wraps`
- Build more flexible and reusable decorators

---

## What You Will Practice

Topics covered in this stage:

- Positional arguments
- Keyword arguments
- `*args`
- `**kwargs`
- Return values
- Function metadata
- State inside decorators
- Reusable decorator patterns

---

## Recommended Approach

For every exercise:

1. Read the challenge carefully.
2. Attempt a solution without looking at hints.
3. Experiment with your own variations.
4. Refactor and improve your solution.
5. Compare against the provided solution.
6. Reflect on what you learned.
7. Move on only when the concept feels comfortable.

---

## Exercises

### 11 Handle Positional Arguments

Learn how a decorator can wrap functions that accept positional arguments.

---

### 12 Handle Keyword Arguments

Learn how decorators interact with keyword arguments.

---

### 13 Handle Any Arguments

Create a decorator that works with both positional and keyword arguments using `*args` and `**kwargs`.

---

### 14 Preserve Return Values

Learn how decorators should correctly return values from wrapped functions.

---

### 15 Forward Arguments

Practice passing all received arguments to the wrapped function without modification.

---

### 16 Decorating Different Functions

Use the same decorator with multiple functions that have different signatures.

---

### 17 Decorator That Counts Calls

Create a decorator that tracks how many times a function has been called.

---

### 18 Decorator With State

Learn how decorators can maintain information between function calls.

---

### 19 Preserve Function Metadata

Use `functools.wraps` to preserve a function's name, docstring, and metadata.

---

### 20 Build a Function Profiler

Create a reusable decorator that gathers information about function execution.

This exercise acts as the capstone for the Exploration stage.

---

## Success Criteria

You are ready to continue to the next stage when:

- [ ] All exercises are complete
- [ ] You can create decorators that work with any function signature
- [ ] You understand the purpose of `*args` and `**kwargs`
- [ ] You can correctly preserve return values
- [ ] You understand how decorators can maintain state
- [ ] You understand why `functools.wraps` is important
- [ ] You can create reusable decorators without relying on examples

---

## What Comes Next?

After completing this stage, move on to:

```text
3-manipulation
```

In the next stage you will begin using decorators to solve practical problems such as timing, logging, debugging, validation, and execution tracking.

---

## Remember

Understanding decorators is one thing.

Understanding how decorators handle *real functions with real inputs and outputs* is what makes them useful.