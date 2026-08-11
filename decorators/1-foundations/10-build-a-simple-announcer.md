# Exercise 10 - Build a Simple Announcer

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
✅ 05 Wrap a Function
✅ 06 Before Execution
✅ 07 Before and After Execution
✅ 08 Understanding @ Syntax
✅ 09 Multiple Decorated Functions
➡️ 10 Build a Simple Announcer
```

---

## Goal

Learn how to:

```text
Combine everything you've learned to build a reusable decorator.
```

By the end of this exercise you should understand:

- How decorators are built from smaller concepts
- How a decorator can be reused across multiple functions
- How wrapper functions can add behavior before and after execution

---

## Why This Matters

The previous nine exercises introduced the building blocks of decorators:

```text
Functions are objects
↓
Functions can be passed as arguments
↓
Functions can be returned
↓
Functions can wrap other functions
↓
Decorator syntax
```

This exercise brings everything together.

Instead of learning a new idea, you'll use everything you've already learned to build a simple but useful decorator.

This serves as the capstone exercise for the Foundations stage.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper
- Exercise 05 - Wrap a Function
- Exercise 06 - Before Execution
- Exercise 07 - Before and After Execution
- Exercise 08 - Understanding @ Syntax
- Exercise 09 - Multiple Decorated Functions

---

## Combining Previous Concepts

This exercise does not introduce a major new concept.

Instead, it combines concepts you've already learned:

- Wrapper functions
- Decorators
- Function references
- Reusable behavior
- Decorator syntax

The goal is to move from understanding individual pieces to building something useful.

---

## Challenge

Create a decorator named:

```python
announce
```

The `announce()` decorator should:

1. Receive another function as an argument
2. Create a nested function named `wrapper`
3. Display a start message before the function executes
4. Execute the wrapped function
5. Display a finish message after the function executes
6. Include the wrapped function's name in both messages
7. Return the wrapper function

---

Create the following decorated functions:

```python
say_hello()
say_goodbye()
say_welcome()
```

Each function should print a unique message.

For example:

```text
Hello!
Goodbye!
Welcome!
```

Decorate all three functions using:

```python
@announce
```

Then execute all three functions.

---

## Requirements

Your solution must:

- Create a decorator named `announce`
- Allow `announce()` to receive another function
- Create a nested `wrapper()` function
- Display a start message before execution
- Display a finish message after execution
- Include the wrapped function name in both messages
- Return the wrapper function
- Decorate at least three functions
- Use `@announce`
- Execute all decorated functions

Do not:

- Duplicate announcement logic inside the decorated functions
- Create a separate decorator for each function

The goal is to create one reusable decorator.

---

## Starter Code

```python
def announce(func):
    pass


@announce
def say_hello():
    print("Hello!")


@announce
def say_goodbye():
    print("Goodbye!")


@announce
def say_welcome():
    print("Welcome!")
```

---

## Verify Your Solution

Your output should resemble:

```text
Starting say_hello...
Hello!
Finished say_hello.

Starting say_goodbye...
Goodbye!
Finished say_goodbye.

Starting say_welcome...
Welcome!
Finished say_welcome.
```

You should also be able to explain:

```text
How the decorator combines everything learned
throughout the Foundations stage.
```

Avoid looking at the solution until you understand how all the pieces fit together.

---

## Hints

### Hint 1

You've already created wrappers that execute code before and after a function.

---

### Hint 2

The wrapped function is available through:

```python
func
```

inside the decorator.

---

### Hint 3

The function name can be accessed using:

```python
func.__name__
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Decorate five different functions.

---

### Try 2

Customize the messages.

Example:

```text
Launching...
Completed.
```

---

### Try 3

Add separators around each execution.

---

## Reflection

Answer these questions:

1. Which earlier exercises helped you complete this challenge?
2. Why is the decorator reusable?
3. What benefits does this decorator provide?
4. How would the code look without the decorator?

The goal is to reinforce understanding.

---

## Stretch Goal

Add a timestamp before execution.

Example:

```text
[2026-08-11 10:15:42]
Starting say_hello...
Hello!
Finished say_hello.
```

Hint:

```python
from datetime import datetime
```

may be useful.

---

## Real-World Connection

Many real-world decorators perform similar tasks.

Examples include:

- Logging function calls
- Monitoring applications
- Measuring execution time
- Recording audit information
- Tracing program behavior

The common pattern is:

```text
Do something before
↓
Execute function
↓
Do something after
```

This exercise uses the same structure.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can build a reusable decorator
- [ ] You can decorate multiple functions
- [ ] You understand how wrapper functions work
- [ ] You understand what `@decorator` does
- [ ] You can explain how decorators work internally
- [ ] Decorators no longer feel like magic

---

## What Comes Next?

Next:

```text
2-exploration
```

In the Exploration stage, you'll investigate how decorators work with:

- Function arguments
- Keyword arguments
- Return values
- Function metadata
- More realistic use cases

---

## Solution

See:

```text
solutions/10-build-a-simple-announcer.py
```