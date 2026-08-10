# Exercise 03 - Return a Function

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
➡️ 03 Return a Function
⬜ 04 Create Your First Wrapper
⬜ 05 Wrap a Function
```

---

## Goal

Learn how to:

```text
Return a function from another function.
```

By the end of this exercise you should understand:

- Functions can be created inside other functions
- Functions can be returned as values
- Returned functions can be stored and executed later

---

## Why This Matters

So far you have learned that:

- Functions are objects
- Functions can be stored in variables
- Functions can be passed as arguments

Now you'll learn the final foundational piece:

```text
Functions can be returned from other functions.
```

Decorators rely heavily on this concept.

Later in this topic you will create functions that receive a function and return a new function. Understanding this pattern is essential before building your first decorator.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument

---

## New Concept

Functions can be created inside other functions and returned.

For example:

```python
def outer():
    def inner():
        pass

    return inner
```

Notice that:

```python
return inner
```

returns the function itself.

It does not execute the function.

---

## Challenge

Create a function called:

```python
create_greeter
```

Inside it, create another function called:

```python
greet
```

The `greet()` function should print:

```text
Hello!
```

Then:

1. Return `greet` from `create_greeter()`
2. Store the returned function in a variable named `my_greeter`
3. Execute the returned function

---

## Requirements

Your solution must:

- Create a function named `create_greeter`
- Create a nested function named `greet`
- Return the nested function
- Store the returned function in a variable
- Execute the returned function
- Produce the expected output

Do not:

- Call `greet()` inside `create_greeter()`
- Return the result of calling `greet()`

The goal is to return the function itself.

---

## Starter Code

```python
def create_greeter():
    def greet():
        pass

    return
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Hello!
```

You should also be able to explain:

```text
Why create_greeter() returns a function
instead of immediately running one.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

Functions can be defined inside other functions.

Example:

```python
def outer():
    def inner():
        pass
```

---

### Hint 2

Think carefully about the difference between:

```python
return greet
```

and

```python
return greet()
```

One returns a function.

The other executes a function.

---

### Hint 3

After calling:

```python
create_greeter()
```

the returned value should be a function that you can call later.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Change the greeting:

```text
Welcome!
```

Does everything still work?

---

### Try 2

Call the returned function multiple times:

```python
my_greeter()
my_greeter()
my_greeter()
```

What happens?

---

### Try 3

Create another function:

```python
create_farewell()
```

that returns a function printing:

```text
Goodbye!
```

---

## Reflection

Answer these questions:

1. What does `create_greeter()` return?
2. Why does `return greet` work?
3. What happens if you use `return greet()` instead?
4. Why might returning a function be useful?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function named:

```python
create_message_printer()
```

that returns a nested function which prints a message.

For example:

```text
Learning decorators!
```

Can you create multiple factory functions that each return different printing functions?

---

## Real-World Connection

Returning functions is a common pattern in Python.

Examples include:

- Decorators
- Factory functions
- Configuration helpers
- Testing utilities
- Framework internals

In a decorator, you'll often see code similar to:

```python
def decorator(func):
    def wrapper():
        ...

    return wrapper
```

This works because functions can return other functions.

You are now learning one of the core building blocks behind that pattern.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a nested function
- [ ] You can return a function from another function
- [ ] You understand the difference between `greet` and `greet()`
- [ ] You can store a returned function in a variable
- [ ] You are ready to build your first wrapper function

---

## Solution

See:

```text
solutions/03-return-a-function.py
```