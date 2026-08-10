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

Learn how to:

```text
Pass a function to another function.
```

By the end of this exercise you should understand:

- Functions can be passed as arguments
- A function can receive another function and execute it
- Functions can be treated like other values in Python

---

## Why This Matters

In the previous exercise, you learned that functions are objects.

Now you'll take the next step and use that fact in a practical way.

Decorators rely on receiving functions as arguments.

Later in this topic you will write code that looks like:

```python
def decorator(func):
    ...
```

To understand why that works, you first need to understand how functions can be passed between other functions.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects

---

## New Concept

Functions can be passed to other functions as arguments.

For example:

```python
run(my_function)
```

In this example, the function is being passed as a value.

Notice that the function name is used without parentheses.

Adding parentheses would execute the function immediately instead of passing it.

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

Then create another function called:

```python
run
```

The `run()` function should:

- Accept a function as an argument
- Execute the function it receives

Finally, pass `say_hello` into `run()` and verify that it executes correctly.

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `run`
- Allow `run()` to receive a function as an argument
- Execute the received function
- Produce the expected output

Do not:

- Call `say_hello()` directly outside of `run()`
- Hardcode the output inside `run()`

The goal is for `run()` to execute whichever function it receives.

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

## Verify Your Solution

When your program runs successfully, you should see:

```text
Hello!
```

You should also be able to explain:

```text
Why run(say_hello) passes a function,
while run(say_hello()) executes a function.
```

Avoid looking at the solution until you can explain this concept yourself.

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

Compare these carefully:

```python
run(say_hello)
```

and

```python
run(say_hello())
```

One passes a function.

The other executes a function before `run()` is called.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create another function:

```python
say_goodbye()
```

Pass it into `run()`.

What happens?

---

### Try 2

Call `run()` several times using different functions.

Can the same `run()` function execute all of them?

---

### Try 3

Create a function that prints your name.

Can `run()` execute it without any modifications?

---

## Reflection

Answer these questions:

1. What is being passed into `run()`?
2. Why does `action()` execute the received function?
3. What is the difference between `say_hello` and `say_hello()`?
4. Why is it useful for one function to receive another function?

The goal is to reinforce understanding.

---

## Stretch Goal

Create a function called:

```python
run_twice(action)
```

that executes the received function two times.

For example:

```python
run_twice(say_hello)
```

should produce:

```text
Hello!
Hello!
```

---

## Real-World Connection

Passing functions as arguments is common throughout Python.

Examples include:

- Decorators
- Event handlers
- Sorting functions
- Callback functions
- Testing frameworks

Many powerful Python features are built on the idea that functions can be passed around like any other value.

Understanding this concept is an important step toward building your first decorator.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can pass a function to another function
- [ ] You understand the difference between `say_hello` and `say_hello()`
- [ ] You can execute a received function
- [ ] You understand why functions can be used as arguments
- [ ] You are ready to learn how functions can be returned from other functions

---

## Solution

See:

```text
solutions/02-pass-function-as-argument.py
```