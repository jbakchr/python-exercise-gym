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

Learn what Python's `@decorator` syntax actually does.

Up until now, you have manually wrapped functions using code like:

```python
wrapped_hello = wrap(say_hello)
```

In this exercise, you'll discover that the `@` syntax is simply a shortcut for the same process.

One of the biggest misconceptions about decorators is that the `@` syntax is some special magic.

It isn't.

This exercise will help remove that mystery.

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

These two examples are equivalent:

### Manual Wrapping

```python
def say_hello():
    print("Hello!")


say_hello = wrap(say_hello)
```

### Decorator Syntax

```python
@wrap
def say_hello():
    print("Hello!")
```

Python automatically performs the assignment for you.

---

## Challenge

Create a function named:

```python
wrap()
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

Then:

### Part 1

Use manual wrapping:

```python
say_hello = wrap(say_hello)
```

and verify that it works.

### Part 2

Replace the manual wrapping with:

```python
@wrap
```

and verify that the output remains identical.

---

## Requirements

Your solution must:

- Create a function named `wrap`
- Create a function named `say_hello`
- Demonstrate manual wrapping
- Demonstrate `@wrap`
- Produce identical output in both cases
- Explain what the `@` syntax does

---

## Starter Code

```python
def wrap(func):
    def wrapper():
        pass

    return wrapper


def say_hello():
    print("Hello!")


# Manual wrapping


# Decorator syntax version
```

---

## Expected Usage

### Manual Wrapping

```python
def say_hello():
    print("Hello!")


say_hello = wrap(say_hello)

say_hello()
```

### Decorator Syntax

```python
@wrap
def say_hello():
    print("Hello!")


say_hello()
```

---

## Expected Output

```text
Before
Hello!
After
```

---

## Hints

### Hint 1

Start by making your existing wrapper work.

You already built one in Exercise 07.

---

### Hint 2

Remember:

```python
say_hello = wrap(say_hello)
```

returns a new function and assigns it back to:

```python
say_hello
```

---

### Hint 3

Python automatically performs the assignment when you write:

```python
@wrap
```

above a function definition.

---

### Hint 4

The following are equivalent:

```python
@wrap
def greet():
    ...
```

and:

```python
def greet():
    ...

greet = wrap(greet)
```

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Create another function:

```python
say_goodbye()
```

and decorate it using `@wrap`.

---

### Try 2

Decorate multiple functions with the same wrapper.

---

### Try 3

Change the messages:

```text
Starting...
Finished...
```

and verify that all decorated functions inherit the change.

---

### Try 4

Compare the readability of:

```python
function = wrap(function)
```

versus:

```python
@wrap
```

Which do you prefer?

Why?

---

## Reflection

Answer the following questions.

1. What does `@wrap` actually do?
2. Why does Python provide decorator syntax?
3. Which version is easier to read?
4. Is the `@` syntax required for decorators?
5. Why might some people mistakenly think decorators are magical?

---

## Stretch Goal

Create two versions of the same program:

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

Verify that both produce identical output.

Then explain in your own words why this happens.

---

## Real-World Connection

Most decorator code you encounter in Python projects uses:

```python
@decorator_name
```

Examples:

```python
@app.route("/")
```

```python
@dataclass
```

```python
@cache
```

```python
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

makes these patterns much easier to understand.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You understand what `@decorator` does
- [ ] You can manually wrap a function
- [ ] You can use decorator syntax
- [ ] You understand that both approaches produce the same result
- [ ] The `@` syntax no longer feels magical
- [ ] You are ready to apply the same decorator to multiple functions

---

## Solution

See:

```text
solutions/08-understanding-at-syntax.py
```