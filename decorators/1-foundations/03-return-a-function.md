# Exercise 03 - Return a Function

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
➡️ 03 Return a Function
⬜ 04 Create Your First Wrapper
⬜ 05 Wrap a Function
```

---

## Goal

Learn that functions can return other functions.

In the previous exercises, you learned that:

- Functions are objects
- Functions can be assigned to variables
- Functions can be passed as arguments

In this exercise, you'll discover that functions can also return other functions.

This is one of the most important building blocks behind decorators.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument

---

## New Concept

Functions can be created inside other functions and returned.

Example:

```python
def outer():
    def inner():
        print("Hello!")

    return inner
```

The returned function can then be stored and executed later:

```python
greet = outer()

greet()
```

Output:

```text
Hello!
```

Notice that:

```python
outer()
```

returns a function.

---

## Challenge

Create a function named:

```python
create_greeter()
```

Inside it, create another function named:

```python
greet()
```

The `greet()` function should print:

```text
Hello!
```

Return `greet` from `create_greeter()`.

Then:

1. Store the returned function in a variable named `my_greeter`
2. Execute the returned function

---

## Requirements

Your solution must:

- Create a function called `create_greeter`
- Create a nested function called `greet`
- Return the nested function
- Store the returned function in a variable
- Execute the returned function
- Produce the expected output

Do **not** call `greet()` from inside `create_greeter()`.

The goal is to return the function itself.

---

## Starter Code

```python
def create_greeter():
    def greet():
        pass

    return


my_greeter = create_greeter()

my_greeter()
```

---

## Expected Usage

```python
def create_greeter():
    def greet():
        print("Hello!")

    return greet


my_greeter = create_greeter()

my_greeter()
```

---

## Expected Output

```text
Hello!
```

---

## Hints

### Hint 1

Functions can be created inside other functions.

Example:

```python
def outer():
    def inner():
        pass
```

---

### Hint 2

Return the function itself.

Correct:

```python
return greet
```

Incorrect:

```python
return greet()
```

---

### Hint 3

Remember:

```python
greet
```

refers to the function.

While:

```python
greet()
```

executes the function.

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Change the greeting:

```python
Welcome!
```

Does it still work?

---

### Try 2

Call the returned function multiple times:

```python
my_greeter()
my_greeter()
my_greeter()
```

---

### Try 3

Create another factory:

```python
create_farewell()
```

that returns a function printing:

```text
Goodbye!
```

---

### Try 4

Print the returned object before executing it:

```python
print(my_greeter)
```

What do you see?

---

## Reflection

Answer the following questions.

1. What does `create_greeter()` return?
2. Why does `return greet` work?
3. What happens if you write `return greet()` instead?
4. Why might returning a function be useful?

---

## Stretch Goal

Create a function:

```python
create_message_printer()
```

that returns a nested function which prints a message.

Example:

```python
printer = create_message_printer()

printer()
```

Output:

```text
Learning decorators!
```

Can you create multiple functions that each return different printing functions?

---

## Real-World Connection

Decorators rely on returning functions.

A decorator often looks something like:

```python
def decorator(func):
    def wrapper():
        func()

    return wrapper
```

Notice the final line:

```python
return wrapper
```

This works because Python allows functions to return other functions.

This exercise introduces that important concept before you build your first wrapper function.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a nested function
- [ ] You can return a function from another function
- [ ] You understand the difference between `greet` and `greet()`
- [ ] You can store a returned function in a variable
- [ ] You are ready to build wrapper functions

---

## Solution

See:

```text
solutions/03-return-a-function.py
```