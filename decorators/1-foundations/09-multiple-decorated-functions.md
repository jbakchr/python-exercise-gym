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

Learn how to:

```text
Reuse the same decorator across multiple functions.
```

By the end of this exercise you should understand:

- A single decorator can be applied to many different functions
- Decorators promote code reuse
- Changes made to a decorator automatically affect all decorated functions

---

## Why This Matters

In the previous exercise, you learned that:

```python
@decorator
```

is simply shorthand for:

```python
function = decorator(function)
```

Now you'll explore one of the biggest benefits of decorators:

```text
Reusability
```

Instead of adding the same behavior to every function manually, you can create one decorator and apply it to many functions.

This is one of the reasons decorators are widely used in Python projects and frameworks.

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

A single decorator can be reused across multiple functions.

For example:

```python
@announce
def first():
    ...

@announce
def second():
    ...
```

The decorator only needs to be written once.

Every decorated function automatically gains its behavior.

---

## Challenge

Create a decorator named:

```python
announce
```

The `announce()` decorator should:

1. Receive another function as an argument
2. Create a nested function named `wrapper`
3. Print:

```text
Before
```

4. Execute the wrapped function
5. Print:

```text
After
```

6. Return the wrapper function

---

Create the following decorated functions:

```python
say_hello()
say_goodbye()
say_welcome()
```

Decorate all three functions using:

```python
@announce
```

Each function should print a different message:

```text
Hello!
Goodbye!
Welcome!
```

Finally, execute all three functions.

---

## Requirements

Your solution must:

- Create a decorator named `announce`
- Allow `announce()` to receive another function
- Create a nested function named `wrapper`
- Print `"Before"` before the wrapped function executes
- Execute the wrapped function
- Print `"After"` after the wrapped function executes
- Return the wrapper function
- Create `say_hello()`
- Create `say_goodbye()`
- Create `say_welcome()`
- Decorate all three functions using `@announce`
- Execute all three functions

Do not:

- Duplicate the decorator logic inside each function
- Create separate decorators for each function

The goal is to reuse the same decorator across multiple functions.

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


# Execute all three functions
```

---

## Verify Your Solution

When your program runs successfully, you should see:

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

You should also be able to explain:

```text
How one decorator can add the same
behavior to many different functions.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

You've already built this type of decorator in previous exercises.

Focus on applying it to multiple functions.

---

### Hint 2

The same decorator can be reused:

```python
@announce
def first():
    ...

@announce
def second():
    ...
```

---

### Hint 3

The decorator should not care what the function does.

Its job is simply to:

```python
func()
```

and add behavior around it.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Add another decorated function:

```python
@announce
def say_thanks():
    print("Thanks!")
```

---

### Try 2

Change the decorator messages:

```text
Starting...
Finished...
```

How many functions inherit the change?

---

### Try 3

Create one decorated function and one undecorated function.

Compare the output.

---

## Reflection

Answer these questions:

1. Why is reusability one of the biggest advantages of decorators?
2. How many functions can use the same decorator?
3. How would you add the same behavior without a decorator?
4. What happens if you change the decorator implementation?

The goal is to reinforce understanding.

---

## Stretch Goal

Modify the decorator so that it prints the function name.

Example output:

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

The biggest benefit of decorators is code reuse.

Imagine you have dozens of functions that all need:

- Logging
- Timing
- Validation
- Authentication

Without decorators, you would repeat the same code in every function.

With decorators, you can write the behavior once and reuse it everywhere.

This is why decorators are common in:

- Web frameworks
- Testing frameworks
- Logging systems
- Caching libraries
- Authentication systems

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can apply the same decorator to multiple functions
- [ ] You understand the reusability benefit of decorators
- [ ] You can modify one decorator and affect many functions
- [ ] You understand how decorators reduce repetition
- [ ] You are ready to build a reusable decorator utility

---

## Solution

See:

```text
solutions/09-multiple-decorated-functions.py
```