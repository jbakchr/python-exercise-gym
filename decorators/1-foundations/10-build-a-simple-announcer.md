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

Build your first reusable decorator.

This exercise acts as the capstone exercise for the Foundations stage.

Rather than focusing on a single new concept, this exercise combines everything you have learned so far:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions
- Decorator syntax
- Reusable decorators

By the end of this exercise, you will have built a decorator that can be applied to multiple functions to announce when those functions are executed.

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

## New Concept

This exercise does not introduce a major new concept.

Instead, it focuses on combining previously learned concepts into a reusable solution.

This is an important transition:

```text
Learning concepts
↓
Combining concepts
↓
Building something useful
```

---

## Challenge

Create a decorator named:

```python
announce
```

that:

1. Prints a message before a function executes
2. Prints a message after a function executes
3. Includes the function name in both messages

The decorator should produce output similar to:

```text
Starting say_hello...
Hello!
Finished say_hello.
```

Apply the decorator to at least three different functions.

For example:

```python
say_hello()
say_goodbye()
say_welcome()
```

---

## Requirements

Your solution must:

- Create a decorator named `announce`
- Use `@announce`
- Display the wrapped function's name before execution
- Display the wrapped function's name after execution
- Decorate at least three different functions
- Produce readable output
- Avoid duplicating code within the decorated functions

---

## Starter Code

```python
def announce(func):
    def wrapper():
        pass

    return wrapper


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

## Expected Usage

```python
@announce
def say_hello():
    print("Hello!")


say_hello()
```

---

## Expected Output

```text
Starting say_hello...
Hello!
Finished say_hello.
```

---

## Example Output

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

---

## Hints

### Hint 1

You already created wrappers that execute code before and after a function.

---

### Hint 2

The wrapped function is available through:

```python
func
```

inside the decorator.

---

### Hint 3

The function name can be accessed with:

```python
func.__name__
```

---

### Hint 4

Your wrapper's general structure will resemble:

```python
def wrapper():
    print(...)
    func()
    print(...)
```

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Decorate five functions instead of three.

---

### Try 2

Customize the start and finish messages.

Example:

```text
Launching...
Completed.
```

---

### Try 3

Add separators.

Example:

```text
----------------------------------------
Starting say_hello...
Hello!
Finished say_hello.
----------------------------------------
```

---

### Try 4

Create functions with multiple print statements.

Does the decorator still work?

---

## Reflection

Answer the following questions.

1. Which concepts from earlier exercises did you use?
2. Why is the decorator reusable?
3. What benefits does the decorator provide?
4. How would the code look if the decorator didn't exist?
5. What parts of decorators feel comfortable now?
6. What parts still feel confusing?

---

## Stretch Goal

Add a timestamp before execution.

Example:

```text
[2026-08-09 10:15:42]
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

Many real-world decorators perform actions very similar to this exercise.

Examples include:

- Logging function calls
- Recording execution times
- Tracing application behavior
- Monitoring API endpoints
- Auditing user actions

The pattern is almost always:

```python
Before
↓
Run function
↓
After
```

The difference is simply what work happens before and after execution.

---

## Success Criteria

You can consider the Foundations stage complete when:

- [ ] All 10 exercises are complete
- [ ] You understand how decorators work internally
- [ ] You understand what `@decorator` actually does
- [ ] You can build a simple decorator from memory
- [ ] You can explain wrapper functions to another developer
- [ ] You understand why functions being objects makes decorators possible
- [ ] Decorators no longer feel like magic

---

## What Comes Next?

Next:

```text
2-exploration
```

In the Exploration stage, you will learn how decorators work with:

- Positional arguments
- Keyword arguments
- Return values
- State
- Function metadata

The concepts become more realistic and more powerful.

---

## Solution

See:

```text
solutions/10-build-a-simple-announcer.py
```

---

## Remember

The goal of Foundations was never to memorize decorator syntax.

The goal was to understand the ideas that make decorators possible:

```text
Functions are objects
↓
Functions can be passed around
↓
Functions can be returned
↓
Functions can wrap other functions
↓
Decorators become obvious
```

If you've reached that understanding, you've successfully completed the Foundations stage.