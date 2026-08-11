# Exercise 08 - Understanding @ Syntax

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
✅ 05 Wrap a Function
✅ 06 Before Execution
✅ 07 Before and After Execution
➡️ 08 Understanding @ Syntax
⬜ 09 Multiple Decorated Functions
⬜ 10 Build a Simple Announcer
```

---

## Goal

Learn how to:

```text
Use Python's @ decorator syntax.
```

By the end of this exercise you should understand:

- What `@decorator` syntax does
- How decorator syntax relates to manual wrapping
- Why the `@` syntax is simply a shortcut

---

## Why This Matters

In the previous exercises, you manually wrapped functions using code like:

```python
say_hello = wrap(say_hello)
```

Python provides a more convenient way of writing the same thing:

```python
@wrap
def say_hello():
    ...
```

Many developers first encounter decorators through the `@` syntax.

Understanding that the syntax is simply a shortcut makes decorators much easier to learn and reason about.

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

---

## New Concept

Decorator syntax is shorthand for wrapping a function.

These two patterns are equivalent:

```python
say_hello = wrap(say_hello)
```

and:

```python
@wrap
def say_hello():
    ...
```

Python performs the wrapping automatically.

---

## Challenge

Create a function named:

```python
wrap
```

The `wrap()` function should:

1. Receive another function as an argument
2. Create a nested function named `wrapper`
3. Print:

```text
Before
```

4. Execute the received function
5. Print:

```text
After
```

6. Return the `wrapper` function

---

Create a function named:

```python
say_hello
```

that prints:

```text
Hello!
```

---

### Part 1 - Manual Wrapping

Wrap the function manually using:

```python
say_hello = wrap(say_hello)
```

Then execute the wrapped function.

---

### Part 2 - Decorator Syntax

Create another function that prints:

```text
Hello!
```

Use:

```python
@wrap
```

to decorate it.

Then execute the decorated function.

---

## Requirements

Your solution must:

- Create a function named `wrap`
- Allow `wrap()` to receive another function
- Create a nested function named `wrapper`
- Print `"Before"` inside the wrapper
- Execute the wrapped function
- Print `"After"` inside the wrapper
- Return the wrapper function
- Create a function named `say_hello`
- Demonstrate manual wrapping
- Demonstrate decorator syntax
- Produce identical output for both approaches

Do not:

- Create separate wrapper implementations
- Change the behavior between Part 1 and Part 2

The goal is to demonstrate that both approaches perform the same operation.

---

## Starter Code

```python
def wrap(func):
    pass


def say_hello():
    print("Hello!")


# Part 1
# Manual wrapping


# Part 2
# Decorator syntax
```

---

## Verify Your Solution

For both Part 1 and Part 2, you should see:

```text
Before
Hello!
After
```

You should also be able to explain:

```text
How Python transforms:

@wrap

into:

function = wrap(function)
```

Avoid looking at the solution until you can explain this relationship yourself.

---

## Hints

### Hint 1

You already built a wrapper with identical behavior in Exercise 07.

---

### Hint 2

Remember:

```python
say_hello = wrap(say_hello)
```

returns a new function.

---

### Hint 3

When Python sees:

```python
@wrap
```

it automatically performs the wrapping during function definition.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create:

```python
say_goodbye()
```

and decorate it using:

```python
@wrap
```

---

### Try 2

Decorate multiple functions using the same wrapper.

---

### Try 3

Change the wrapper messages to:

```text
Starting...
Finished...
```

Do all decorated functions inherit the new behavior?

---

## Reflection

Answer these questions:

1. What does `@wrap` actually do?
2. Why is it equivalent to `say_hello = wrap(say_hello)`?
3. Why might the decorator version be easier to read?
4. Why does the `@` syntax sometimes seem magical to new Python developers?

The goal is to reinforce understanding.

---

## Stretch Goal

Create two complete examples:

### Version 1

Uses:

```python
say_hello = wrap(say_hello)
```

### Version 2

Uses:

```python
@wrap
```

Verify that they produce identical output.

Then explain in your own words why they behave the same way.

---

## Real-World Connection

Decorator syntax appears throughout the Python ecosystem.

Examples include:

```python
@app.route("/")
@dataclass
@cache
@property
```

Understanding that:

```python
@decorator
```

is simply shorthand for:

```python
function = decorator(function)
```

makes these patterns much easier to understand and use.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You understand what `@decorator` does
- [ ] You can manually wrap a function
- [ ] You can use decorator syntax
- [ ] You understand that both approaches are equivalent
- [ ] The `@` syntax no longer feels mysterious
- [ ] You are ready to decorate multiple functions

---

## Solution

See:

```text
solutions/08-understanding-at-syntax.py
```