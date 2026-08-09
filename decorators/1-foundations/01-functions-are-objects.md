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

Learn that functions in Python are objects.

This means they can:

- Be assigned to variables
- Be passed around
- Be stored and referenced
- Be used just like other values

Understanding this concept is the first step toward understanding decorators.

---

## Prerequisites

None.

This is the first exercise in the Decorators topic.

---

## New Concept

Functions are first-class objects.

Just like:

```python
name = "Jonas"
age = 42
```

you can also do:

```python
greet = say_hello
```

where `greet` now refers to the same function as `say_hello`.

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

1. Assign the function to a new variable called `greet`
2. Call the function using `greet`
3. Verify that the output is still produced

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Assign the function to a variable named `greet`
- Call the function using `greet`
- Produce the expected output

Do **not** call:

```python
say_hello()
```

after creating `greet`.

The goal is to call the function through the new variable.

---

## Starter Code

```python
def say_hello():
    pass


# Assign the function to greet

# Call the function using greet
```

---

## Expected Usage

```python
def say_hello():
    print("Hello!")


greet = say_hello

greet()
```

---

## Expected Output

```text
Hello!
```

---

## Hints

### Hint 1

Functions can be assigned to variables.

Example:

```python
my_variable = 42
```

The same idea works for functions.

---

### Hint 2

Do not use parentheses when assigning the function.

Correct:

```python
greet = say_hello
```

Incorrect:

```python
greet = say_hello()
```

---

### Hint 3

Adding `()` executes a function.

Without `()`, you are referring to the function itself.

---

## Things to Try

After completing the exercise, experiment with the following.

### Try 1

Add another variable:

```python
hello_again = say_hello
```

Can both variables call the function?

---

### Try 2

Print the function itself:

```python
print(say_hello)
```

What do you see?

---

### Try 3

Check whether two variables reference the same function:

```python
print(greet is say_hello)
```

What is the result?

---

## Reflection

Answer the following questions.

1. What is being stored in the variable `greet`?
2. Why is `greet = say_hello` different from `greet = say_hello()`?
3. What happens when you call `greet()`?
4. Why might it be useful to store a function in a variable?

---

## Stretch Goal

Create two functions:

```python
say_hello
say_goodbye
```

Assign one of them to a variable named:

```python
current_action
```

and call it.

Then change:

```python
current_action
```

to reference the other function and call it again.

Example output:

```text
Hello!
Goodbye!
```

---

## Real-World Connection

Decorators depend on the fact that functions are objects.

Later in this topic you will see code like:

```python
def decorator(func):
    ...
```

The reason this works is that a function can receive another function as an argument.

This exercise is the first step toward understanding that pattern.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can assign a function to a variable
- [ ] You understand why parentheses matter
- [ ] You can call a function through another variable
- [ ] You understand that functions are objects
- [ ] You are ready to pass functions to other functions

---

## Solution

See:

```text
solutions/01-functions-are-objects.py
```