# Exercise 04 - Create Your First Wrapper

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
➡️ 04 Create Your First Wrapper
⬜ 05 Wrap a Function
⬜ 06 Before Execution
```

---

## Goal

Learn how to:

```text
Create a wrapper function that calls another function.
```

By the end of this exercise you should understand:

- What a wrapper function is
- How one function can execute another function
- Why wrappers are the foundation of decorators

---

## Why This Matters

So far you have learned that:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned from other functions

Now you'll combine those ideas to create your first wrapper.

Wrappers are one of the fundamental building blocks behind decorators.

Later in this topic, you'll use wrappers to add behavior before and after a function executes.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function

---

## New Concept

A wrapper function is simply a function that calls another function.

Example:

```python
def wrapper():
    another_function()
```

The wrapper acts as a middleman.

Instead of calling the original function directly, you call the wrapper, which then calls the original function.

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

Then create a second function called:

```python
wrapper
```

The `wrapper()` function should execute `say_hello()`.

Finally, call `wrapper()` and verify that the original function runs.

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrapper`
- Have `wrapper()` call `say_hello()`
- Call `wrapper()`
- Produce the expected output

Do not:

- Call `say_hello()` directly outside of `wrapper()`
- Add extra behavior to the wrapper yet

The goal is simply to create a wrapper around another function.

---

## Starter Code

```python
def say_hello():
    pass


def wrapper():
    pass
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Hello!
```

You should also be able to explain:

```text
Why calling wrapper() causes say_hello()
to execute.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

The wrapper should execute:

```python
say_hello()
```

inside its body.

---

### Hint 2

Think of the wrapper as a middleman.

Instead of:

```python
say_hello()
```

being called directly, you call:

```python
wrapper()
```

which then calls the original function.

---

### Hint 3

The wrapper does not need to return anything.

Its only responsibility is to execute another function.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change the output to:

```text
Welcome!
```

Does the wrapper still work?

---

### Try 2

Create another function:

```python
say_goodbye()
```

That prints:

```text
Goodbye!
```

Update `wrapper()` to call it instead.

---

### Try 3

Make the wrapper call the function multiple times:

```python
def wrapper():
    say_hello()
    say_hello()
```

What happens?

---

## Reflection

Answer these questions:

1. What is the purpose of a wrapper function?
2. Why might someone call a function through a wrapper instead of directly?
3. How could a wrapper be modified to add extra behavior?
4. How does this exercise build on what you learned about returning functions?

The goal is to reinforce understanding.

---

## Stretch Goal

Modify the wrapper so that it prints:

```text
Starting...
```

before executing:

```python
say_hello()
```

Expected output:

```text
Starting...
Hello!
```

This small change provides a glimpse of how decorators extend the behavior of existing functions.

---

## Real-World Connection

Wrapper functions appear throughout Python code.

Examples include:

- Logging utilities
- Timing tools
- Retry mechanisms
- Authentication systems
- Web frameworks

Many of these tools work by executing additional code before or after another function runs.

Decorators are simply a structured way of creating and applying wrappers.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a wrapper function
- [ ] You understand how one function can call another
- [ ] You understand the purpose of a wrapper
- [ ] You can explain why wrappers are useful
- [ ] You are ready to add behavior around another function

---

## Solution

See:

```text
solutions/04-create-your-first-wrapper.py
```