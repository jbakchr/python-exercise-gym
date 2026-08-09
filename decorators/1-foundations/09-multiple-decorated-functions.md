# Exercise 09 - Multiple Decorated Functions

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
➡️ 09 Multiple Decorated Functions
⬜ 10 Build a Simple Announcer
```

---

## Goal

Learn how a single decorator can be reused across multiple functions.

In the previous exercise, you learned that:

```python
@wrap
```

is simply shorthand for:

```python
function = wrap(function)
```

In this exercise, you will discover one of the biggest benefits of decorators:

> Reusability.

Instead of manually adding the same behavior to every function, a single decorator can be applied to many functions.

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

---

## New Concept

A decorator can be applied to many different functions.

Example:

```python
@wrap
def greet():
    print("Hello!")


@wrap
def goodbye():
    print("Goodbye!")
```

Both functions gain the decorator's behavior.

---

## Challenge

Create a decorator named:

```python
announce
```

that:

1. Prints:

```text
Before
```

2. Executes the wrapped function

3. Prints:

```text
After
```

Then create three decorated functions:

```python
say_hello()
say_goodbye()
say_welcome()
```

Each function should print a unique message.

Call all three functions and verify that the decorator behavior appears around each one.

---

## Requirements

Your solution must:

- Create a decorator named `announce`
- Use `@announce`
- Create three decorated functions
- Execute all three functions
- Display the decorator's behavior around each function call

---

## Starter Code

```python
def announce(func):
    def wrapper():
        pass

    return wrapper


@announce
def say_hello():
    pass


@announce
def say_goodbye():
    pass


@announce
def say_welcome():
    pass
```

---

## Expected Usage

```python
@announce
def say_hello():
    print("Hello!")


@announce
def say_goodbye():
    print("Goodbye!")


@announce
def say_welcome():
    print("Welcome!")


say_hello()
say_goodbye()
say_welcome()
```

---

## Expected Output

```text
Before
Hello!
After

Before
Goodbye!
After

Before
Welcome!
After
```

---

## Hints

### Hint 1

You've already built this type of decorator in previous exercises.

Focus on applying it to multiple functions.

---

### Hint 2

The same decorator can be reused many times.

Example:

```python
@announce
def function_one():
    ...
```

```python
@announce
def function_two():
    ...
```

---

### Hint 3

The decorator should not care what the function does.

It should simply execute:

```python
func()
```

---

### Hint 4

Only the decorated function changes.

The decorator remains exactly the same.

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Add a fourth decorated function.

Example:

```python
@announce
def say_thanks():
    print("Thanks!")
```

---

### Try 2

Change the decorator messages.

Example:

```text
Starting...
Finished...
```

Notice that all decorated functions automatically inherit the new behavior.

---

### Try 3

Create one function that is decorated and one that is not.

Compare the output.

---

### Try 4

Add several print statements inside one of the decorated functions.

Does the decorator still work?

---

## Reflection

Answer the following questions.

1. Why is reusability one of the biggest advantages of decorators?
2. How many functions can use the same decorator?
3. How would you add the same behavior without decorators?
4. What happens if you change the decorator implementation?
5. Why is this useful in large projects?

---

## Stretch Goal

Modify the decorator so it prints the function name.

Expected output:

```text
Before calling say_hello
Hello!
After calling say_hello
```

Hint:

```python
func.__name__
```

may be useful.

---

## Real-World Connection

The primary benefit of decorators is code reuse.

Imagine you have 50 functions that all need:

- Logging
- Timing
- Validation
- Authentication

Without decorators, you would repeat the same code in all 50 functions.

With decorators:

```python
@logger
@timer
@validator
```

you can reuse the same behavior everywhere.

This is why decorators are widely used in Python frameworks and libraries.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can apply the same decorator to multiple functions
- [ ] You understand the reusability benefit of decorators
- [ ] You can modify a decorator and affect multiple functions
- [ ] You understand how decorators reduce repetition
- [ ] You are ready to build your first reusable decorator utility

---

## Solution

See:

```text
solutions/09-multiple-decorated-functions.py
```