# Exercise 05 - Wrap a Function

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
➡️ 05 Wrap a Function
⬜ 06 Before Execution
⬜ 07 Before and After Execution
```

---

## Goal

Learn how to:

```text
Dynamically wrap a function.
```

By the end of this exercise you should understand:

- A function can receive another function
- A function can create and return a wrapper
- Wrapping combines all the major concepts learned so far

---

## Why This Matters

In the previous exercises, you learned that:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned from other functions
- Wrapper functions can execute other functions

This exercise combines all of those ideas into a single pattern.

For the first time, you'll create a function that:

```text
Receives a function
↓
Creates a wrapper
↓
Returns the wrapper
```

This is the core pattern behind decorators.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper

---

## New Concept

A function can create a wrapper around another function.

For example:

```python
def wrap(func):
    def wrapper():
        pass

    return wrapper
```

The wrapper can access and execute the function that was originally passed in.

This pattern is one of the key building blocks behind decorators.

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

The `wrap()` function should:

1. Receive another function
2. Create a nested function named `wrapper`
3. Have the wrapper execute the received function
4. Return the wrapper

Finally:

1. Pass `say_hello` into `wrap()`
2. Store the returned wrapper in a variable
3. Execute the returned wrapper

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrap`
- Allow `wrap()` to receive a function
- Create a nested function named `wrapper`
- Execute the supplied function inside the wrapper
- Return the wrapper function
- Store the returned wrapper in a variable
- Execute the returned wrapper
- Produce the expected output

Do not:

- Call `say_hello()` directly after creating the wrapper
- Return `wrapper()` instead of `wrapper`

The goal is to execute the original function through the returned wrapper.

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
Hello!
```

You should also be able to explain:

```text
How a function can receive another function,
create a wrapper around it,
and return that wrapper for later use.
```

Avoid looking at the solution until you can explain this flow yourself.

---

## Hints

### Hint 1

The parameter:

```python
func
```

contains the function that was passed into `wrap()`.

---

### Hint 2

The wrapper should execute:

```python
func()
```

inside its body.

---

### Hint 3

Remember the difference between:

```python
return wrapper
```

and

```python
return wrapper()
```

One returns a function.

The other executes a function.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create another function:

```python
say_goodbye()
```

Wrap it using the same `wrap()` function.

---

### Try 2

Create multiple wrapped functions:

```python
wrapped_hello
wrapped_goodbye
```

Execute both.

---

### Try 3

Add a print statement inside the wrapper:

```python
print("Wrapper started")
```

What happens when the wrapped function is executed?

---

## Reflection

Answer these questions:

1. Why does `wrap()` receive a function?
2. Why does `wrap()` return a function?
3. What role does the nested `wrapper()` function play?
4. How does this exercise combine concepts from earlier exercises?

The goal is to reinforce understanding.

---

## Stretch Goal

Modify the wrapper so that it prints:

```text
Calling function...
```

before executing the wrapped function.

Expected output:

```text
Calling function...
Hello!
```

You have now started adding behavior around an existing function.

---

## Real-World Connection

Many Python libraries and frameworks use this exact pattern.

Examples include:

- Logging utilities
- Authentication systems
- Performance monitoring tools
- Retry mechanisms
- Caching systems

All of these often work by:

```text
Receiving a function
↓
Creating a wrapper
↓
Returning the wrapper
```

Once you understand this pattern, decorators become much easier to understand.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can pass a function into another function
- [ ] You can create a nested wrapper function
- [ ] You can return a wrapper function
- [ ] You understand the flow of execution
- [ ] You can explain how wrapping works
- [ ] You are ready to add behavior before a function executes

---

## Solution

See:

```text
solutions/05-wrap-a-function.py
```