# Exercise 02 - Pass Function as Argument

## Progression

```text
✅ 01 Functions Are Objects
➡️ 02 Pass Function as Argument
⬜ 03 Return a Function
⬜ 04 Create Your First Wrapper
```

---

## Goal

Learn that functions can be passed as arguments to other functions.

In the previous exercise, you learned that functions are objects and can be assigned to variables.

In this exercise, you will take the next step and discover that functions can also be passed to other functions.

This is one of the most important ideas behind decorators.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects

---

## New Concept

Functions can be passed as arguments.

For example:

```python
def greet():
    print("Hello!")


def run(action):
    action()


run(greet)
```

Notice that:

```python
greet
```

is passed into:

```python
run()
```

just like you could pass:

```python
42
"hello"
True
```

---

## Challenge

Create:

```python
say_hello()
```

and:

```python
run()
```

The `run()` function should:

1. Accept a function as an argument.
2. Execute the function it receives.

Then call:

```python
run(say_hello)
```

and verify that the function is executed.

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `run`
- Allow `run()` to receive another function
- Execute the received function
- Produce the expected output

Do **not** call `say_hello()` directly outside of `run()`.

The goal is for `run()` to execute it.

---

## Starter Code

```python
def say_hello():
    pass


def run(action):
    pass


run(say_hello)
```

---

## Expected Usage

```python
def say_hello():
    print("Hello!")


def run(action):
    action()


run(say_hello)
```

---

## Expected Output

```text
Hello!
```

---

## Hints

### Hint 1

The parameter:

```python
action
```

will refer to the function passed into `run()`.

---

### Hint 2

To execute a function stored in a variable, use:

```python
action()
```

---

### Hint 3

Remember the difference:

```python
run(say_hello)
```

passes the function.

But:

```python
run(say_hello())
```

executes the function immediately.

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Create another function:

```python
say_goodbye()
```

and pass it into:

```python
run()
```

---

### Try 2

Call:

```python
run()
```

multiple times with different functions.

---

### Try 3

Create a function:

```python
say_name()
```

that prints your name.

Can `run()` execute it without modification?

---

### Try 4

Modify `run()` so it prints:

```text
Running function...
```

before executing the function.

---

## Reflection

Answer the following questions.

1. What argument is being passed to `run()`?
2. How is passing a function different from passing a string or number?
3. Why does `action()` execute the passed function?
4. Why is this concept important for decorators?

---

## Stretch Goal

Create a function:

```python
run_twice(action)
```

that executes the received function two times.

Example:

```python
run_twice(say_hello)
```

Expected output:

```text
Hello!
Hello!
```

---

## Real-World Connection

Decorators rely on receiving functions as arguments.

Later in this topic, you will create code similar to:

```python
def decorator(func):
    ...
```

The reason this works is because Python allows functions to be passed around just like other objects.

Understanding this concept is a critical step toward building your first decorator.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can pass a function to another function
- [ ] You understand the difference between `say_hello` and `say_hello()`
- [ ] You can execute a received function
- [ ] You understand how higher-order functions work
- [ ] You are ready to learn how functions can be returned from other functions

---

## Solution

See:

```text
solutions/02-pass-function-as-argument.py
```