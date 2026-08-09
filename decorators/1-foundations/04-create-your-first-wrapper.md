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

Learn how to create a wrapper function.

In the previous exercises, you learned that:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned from other functions

Now you will combine those ideas to create a wrapper function.

A wrapper function is the key building block behind decorators.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function

---

## New Concept

A wrapper function is a function that calls another function.

Example:

```python
def greet():
    print("Hello!")


def wrapper():
    greet()
```

Calling:

```python
wrapper()
```

will execute:

```python
greet()
```

Wrappers allow us to add behavior around existing functions.

---

## Challenge

Create a function called:

```python
say_hello()
```

that prints:

```text
Hello!
```

Then create a second function called:

```python
wrapper()
```

that calls:

```python
say_hello()
```

When `wrapper()` is executed, the original function should run.

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrapper`
- Have `wrapper()` execute `say_hello()`
- Call `wrapper()`
- Produce the expected output

The goal is not to add extra behavior yet.

Simply create a wrapper around another function.

---

## Starter Code

```python
def say_hello():
    pass


def wrapper():
    pass


wrapper()
```

---

## Expected Usage

```python
def say_hello():
    print("Hello!")


def wrapper():
    say_hello()


wrapper()
```

---

## Expected Output

```text
Hello!
```

---

## Hints

### Hint 1

Your wrapper should execute:

```python
say_hello()
```

inside its body.

---

### Hint 2

Think of the wrapper as a middleman.

Instead of calling:

```python
say_hello()
```

directly, you call:

```python
wrapper()
```

which then calls:

```python
say_hello()
```

---

### Hint 3

The wrapper does not return anything yet.

Its only responsibility is to execute another function.

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Change the output:

```python
print("Welcome!")
```

Does the wrapper still work?

---

### Try 2

Create another function:

```python
say_goodbye()
```

and update the wrapper to call it.

---

### Try 3

Call the wrapped function multiple times:

```python
def wrapper():
    say_hello()
    say_hello()
```

What happens?

---

### Try 4

Create two separate wrappers:

```python
wrapper_one()
wrapper_two()
```

that both call the same function.

---

## Reflection

Answer the following questions.

1. What is the purpose of a wrapper function?
2. Why might someone want to call a function indirectly through a wrapper?
3. How could a wrapper be modified to add extra behavior?
4. How does this exercise build on returning functions from Exercise 03?

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

This small change hints at how decorators can extend behavior.

---

## Real-World Connection

Many Python tools and frameworks wrap existing functions.

For example:

- Logging systems
- Timing utilities
- Retry mechanisms
- Authentication checks

All of these often rely on wrapper functions.

Understanding wrappers is essential because decorators are essentially a way of automatically wrapping functions.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a wrapper function
- [ ] You understand how one function can call another
- [ ] You understand why wrappers are useful
- [ ] You can modify a wrapper to perform additional work
- [ ] You are ready to wrap functions dynamically

---

## Solution

See:

```text
solutions/04-create-your-first-wrapper.py
```