# Exercise 01 - Functions Are Objects

## Progression

```text
➡️ 01 Functions Are Objects
⬜ 02 Pass Function as Argument
⬜ 03 Return a Function
⬜ 04 Create Your First Wrapper
```

---

## Goal

Learn how to:

```text
Treat functions like values.
```

By the end of this exercise you should understand:

- Functions can be assigned to variables
- Multiple variables can refer to the same function
- A function can be called through any variable that references it

---

## Why This Matters

Decorators rely on the fact that functions are objects.

Later in this topic you will see functions being:

- Passed to other functions
- Returned from functions
- Wrapped inside other functions

Before any of that makes sense, you need to understand that a function can be treated just like any other value in Python.

---

## Prerequisites

```text
None.
```

This is the first exercise in the Decorators topic.

---

## New Concept

Functions in Python are first-class objects.

This means they can be stored in variables just like strings, integers, or lists.

For example:

```python
name = "Jonas"
age = 42
```

Functions can be stored in variables too.

The variable does not store the result of calling the function.

It stores a reference to the function itself.

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

Then:

1. Assign the function to a variable called `greet`
2. Call the function using `greet`
3. Verify that the function still works

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Assign the function to a variable named `greet`
- Call the function using `greet`
- Produce the expected output

Do not:

- Call `say_hello()` after creating `greet`
- Create a second copy of the function

The goal is to call the function through the variable.

---

## Starter Code

```python
def say_hello():
    pass


# Assign the function to greet

# Call the function using greet
```

---

## Verify Your Solution

When your program runs successfully, you should see:

```text
Hello!
```

You should also be able to explain:

```text
Why greet can be used to call the function even though
the function's name is say_hello.
```

Avoid looking at the solution until you can explain this concept yourself.

---

## Hints

### Hint 1

Variables can store references to many different kinds of objects.

Functions are objects too.

---

### Hint 2

Think about the difference between:

```python
greet = say_hello
```

and

```python
greet = say_hello()
```

One stores a function.

The other executes a function.

---

### Hint 3

To call the function through the new variable, use:

```python
variable_name()
```

where `variable_name` refers to a function.

---

## Things to Try

After completing the exercise, experiment further.

### Try 1

Create another variable:

```python
hello_again = say_hello
```

Can you call the function through both variables?

---

### Try 2

Print the function itself:

```python
print(say_hello)
```

What gets displayed?

---

### Try 3

Check whether both variables refer to the same function:

```python
print(greet is say_hello)
```

What result do you get?

---

## Reflection

Answer these questions:

1. What is stored in the variable `greet`?
2. Why is `greet = say_hello` different from `greet = say_hello()`?
3. What happens when you call `greet()`?
4. Why might it be useful to store a function in a variable?

The goal is to reinforce understanding.

---

## Stretch Goal

Create two functions:

```python
say_hello
say_goodbye
```

Assign one of them to:

```python
current_action
```

Call it.

Then change `current_action` to reference the other function and call it again.

Expected output:

```text
Hello!
Goodbye!
```

---

## Real-World Connection

Many Python features rely on functions being objects.

Examples include:

- Decorators
- Event handlers
- Callback functions
- Testing frameworks
- Web frameworks

In the next exercises, you'll start passing functions to other functions. That only works because functions can be treated like values.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can assign a function to a variable
- [ ] You understand why parentheses matter
- [ ] You can call a function through a different variable
- [ ] You understand that functions are objects
- [ ] You are ready to pass functions to other functions

---

## Solution

See:

```text
solutions/01-functions-are-objects.py
```