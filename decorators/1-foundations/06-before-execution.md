# Exercise 06 - Before Execution

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
✅ 05 Wrap a Function
➡️ 06 Before Execution
⬜ 07 Before and After Execution
```

---

## Goal

Learn how to:

```text
Execute code before a wrapped function runs.
```

By the end of this exercise you should understand:

- A wrapper can perform work before another function executes
- Wrappers can extend behavior without changing the original function
- Decorators are commonly used to add behavior before execution

---

## Why This Matters

In the previous exercise, you built a wrapper that simply called another function.

Now you'll make the wrapper more useful.

Instead of only executing the wrapped function, the wrapper will perform an additional action before the function runs.

This is the first time you're using a wrapper to modify behavior.

Many real-world decorators use this exact pattern.

For example:

- Logging function calls
- Checking permissions
- Measuring execution time
- Validating inputs

All of these often perform work before the original function runs.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper
- Exercise 05 - Wrap a Function

---

## New Concept

A wrapper can do more than simply call another function.

It can execute additional code before the wrapped function runs.

For example:

```python
def wrapper():
    print("Starting...")
    
    some_function()
```

This allows behavior to be added without modifying the original function.

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
- Print a message before executing the function
- Execute the supplied function
- Return the wrapper
- Execute the returned wrapper

Use this message:

```text
Starting...
```

Do not:

- Modify the original `say_hello()` function
- Print the message outside the wrapper

The goal is for the wrapper to add the behavior.

---

## Starter Code

```python
def say_hello():
    pass


def wrap(func):
    pass
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Starting...
Hello!
```

You should also be able to explain:

```text
How the wrapper adds new behavior
without changing the original function.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

The wrapper should contain more than one statement.

One statement can print a message.

Another can execute the function.

---

### Hint 2

The supplied function is available through:

```python
func
```

You can execute it using:

```python
func()
```

---

### Hint 3

Think about the order of execution.

What should happen first?

```text
Starting...
```

or

```text
Hello!
```

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change the message.

For example:

```text
Preparing to run function...
```

What changes?

---

### Try 2

Add a second wrapped function:

```python
say_goodbye()
```

Can the same wrapper add the message to both functions?

---

### Try 3

Create different wrapper messages for different situations.

For example:

```text
Running task...
Executing action...
Starting process...
```

---

## Reflection

Answer these questions:

1. Why is the message printed by the wrapper instead of the original function?
2. How does the wrapper change the behavior of the function?
3. What advantages does this approach provide?
4. Where might you use this pattern in real applications?

The goal is to reinforce understanding.

---

## Stretch Goal

Create two different wrapping functions.

One should print:

```text
INFO:
```

before execution.

The other should print:

```text
WARNING:
```

before execution.

Can both wrappers be used with the same function?

---

## Real-World Connection

Adding behavior before execution is one of the most common uses of decorators.

Examples include:

- Logging function calls
- Recording audit events
- Authorization checks
- Input validation
- Performance monitoring

Instead of modifying every function individually, developers often use wrappers and decorators to add these behaviors automatically.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can add behavior before a function executes
- [ ] You understand the role of the wrapper
- [ ] You can explain why the original function remains unchanged
- [ ] You understand how wrappers extend behavior
- [ ] You are ready to add behavior both before and after execution

---

## Solution

See:

```text
solutions/06-before-execution.py
```