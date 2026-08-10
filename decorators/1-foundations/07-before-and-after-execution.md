# Exercise 07 - Before and After Execution

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
✅ 05 Wrap a Function
✅ 06 Before Execution
➡️ 07 Before and After Execution
⬜ 08 Understanding @ Syntax
⬜ 09 Multiple Decorated Functions
```

---

## Goal

Learn how to:

```text
Execute code both before and after a wrapped function runs.
```

By the end of this exercise you should understand:

- A wrapper can perform work before a function executes
- A wrapper can perform work after a function executes
- Wrappers can add behavior around a function without modifying it

---

## Why This Matters

In the previous exercise, you learned how a wrapper can execute code before a function runs.

Now you'll take the next step.

A wrapper can surround a function with additional behavior:

```text
Before
↓
Function execution
↓
After
```

This is one of the most common decorator patterns in real-world Python applications.

Many decorators:

- Log function activity
- Measure execution time
- Open and close resources
- Track success and failure

by executing code before and after the original function.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper
- Exercise 05 - Wrap a Function
- Exercise 06 - Before Execution

---

## New Concept

A wrapper can execute code around another function.

For example:

```python
def wrapper():
    print("Before")

    some_function()

    print("After")
```

The wrapper surrounds the original function with additional behavior.

The original function remains unchanged.

---

## Challenge

Create a function called:

```python
say_hello
```

that prints:

```text
Hello!
```

Then create a function called:

```python
wrap
```

that receives another function and returns a wrapper.

The wrapper should:

1. Print a message before execution
2. Execute the wrapped function
3. Print a message after execution

Finally:

1. Wrap `say_hello`
2. Store the returned wrapper
3. Execute the wrapper

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrap`
- Receive a function as an argument
- Create a nested wrapper function
- Print `"Before"`
- Execute the wrapped function
- Print `"After"`
- Return the wrapper
- Execute the returned wrapper

Do not:

- Modify the original `say_hello()` function
- Print the messages outside the wrapper

The wrapper should be responsible for the additional behavior.

---

## Starter Code

```python
def say_hello():
    pass


def wrap(func):
    def wrapper():
        pass

    return wrapper
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Before
Hello!
After
```

You should also be able to explain:

```text
How the wrapper adds behavior around
the original function without modifying it.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

The wrapped function should still be executed using:

```python
func()
```

---

### Hint 2

Code written before:

```python
func()
```

runs first.

Code written after:

```python
func()
```

runs afterwards.

---

### Hint 3

Think carefully about execution order.

The wrapper should:

```text
Print message
↓
Execute function
↓
Print message
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Replace the messages with:

```text
Starting...
Finished.
```

Does the behavior remain the same?

---

### Try 2

Create another function:

```python
say_goodbye()
```

Wrap it and observe the output.

---

### Try 3

Add additional messages:

```text
Preparing...
Before
Hello!
After
Cleaning up...
```

How does this change the execution flow?

---

## Reflection

Answer these questions:

1. Why does the wrapper execute code before and after the function?
2. How does the wrapper change behavior without changing the original function?
3. Why is execution order important?
4. What kinds of tasks might be performed before execution? After execution?

The goal is to reinforce understanding.

---

## Stretch Goal

Modify the wrapper so that it includes the function name in its messages.

Example output:

```text
Starting say_hello...
Hello!
Finished say_hello.
```

Hint:

```python
func.__name__
```

may be useful.

---

## Real-World Connection

Many production decorators follow this exact pattern.

Examples include:

- Logging when a function starts and ends
- Measuring execution time
- Opening and closing database connections
- Creating audit logs
- Tracking successful and failed operations

A common pattern looks like:

```text
Do something before
↓
Execute function
↓
Do something after
```

You are now working with one of the most widely used decorator patterns in Python.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can execute code before a wrapped function
- [ ] You can execute code after a wrapped function
- [ ] You understand execution order
- [ ] You can explain why the original function remains unchanged
- [ ] You understand how wrappers can surround existing behavior
- [ ] You are ready to learn how Python's `@` syntax works

---

## Solution

See:

```text
solutions/07-before-and-after-execution.py
```