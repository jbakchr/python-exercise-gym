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

Combine everything you have learned so far.

In the previous exercises, you learned that:

- Functions are objects
- Functions can be passed as arguments
- Functions can be returned
- Wrapper functions can execute other functions

Now you will combine all of those concepts to dynamically wrap a function.

This is the first exercise that begins to resemble a real decorator.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper

---

## New Concept

A function can:

1. Receive another function
2. Create a wrapper around it
3. Return the wrapper

Example:

```python
def wrap(func):
    def wrapper():
        func()

    return wrapper
```

This pattern is the foundation of decorators.

---

## Challenge

Create a function named:

```python
wrap()
```

that receives another function.

Inside it:

1. Create a nested function named `wrapper`
2. Have `wrapper()` execute the received function
3. Return the `wrapper` function

Then:

1. Create a function named `say_hello`
2. Pass it into `wrap()`
3. Store the returned wrapper in a variable
4. Execute the returned wrapper

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrap`
- Receive a function as an argument
- Create a nested wrapper function
- Execute the supplied function inside the wrapper
- Return the wrapper
- Execute the returned wrapper
- Produce the expected output

---

## Starter Code

```python
def say_hello():
    pass


def wrap(func):
    def wrapper():
        pass

    return


wrapped_hello = wrap(say_hello)

wrapped_hello()
```

---

## Expected Usage

```python
def say_hello():
    print("Hello!")


def wrap(func):
    def wrapper():
        func()

    return wrapper


wrapped_hello = wrap(say_hello)

wrapped_hello()
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
func
```

contains the function passed into `wrap()`.

---

### Hint 2

The wrapper should execute:

```python
func()
```

---

### Hint 3

Return the wrapper itself.

Correct:

```python
return wrapper
```

Incorrect:

```python
return wrapper()
```

---

### Hint 4

The flow should look like:

```text
say_hello
↓
wrap(say_hello)
↓
returns wrapper
↓
call wrapper
↓
wrapper calls say_hello
```

---

## Things to Try

After completing the exercise, experiment with these variations.

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

and execute both.

---

### Try 3

Print messages inside the wrapper.

Example:

```python
def wrapper():
    print("Wrapper started")
    func()
```

---

### Try 4

Create a wrapper that calls the function twice.

Example:

```python
func()
func()
```

---

## Reflection

Answer the following questions.

1. Why does `wrap()` receive a function?
2. Why does `wrap()` return a function?
3. What role does `wrapper()` play?
4. How does this exercise combine earlier concepts?
5. Why is returning `wrapper` important?

---

## Stretch Goal

Modify the wrapper so it prints:

```text
Calling function...
```

before executing the function.

Example output:

```text
Calling function...
Hello!
```

You have now begun adding behavior around another function.

---

## Real-World Connection

This pattern is extremely common in Python.

Many tools and frameworks use functions that:

- Receive another function
- Wrap it
- Return a new function

Examples include:

- Logging systems
- Authentication checks
- Retry mechanisms
- Performance monitoring
- Caching

Understanding this wrapping pattern makes decorators much easier to understand.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can pass a function into another function
- [ ] You can create a nested wrapper function
- [ ] You can return a wrapper function
- [ ] You understand how wrapping works
- [ ] You can explain the flow of execution
- [ ] You are ready to add behavior before function execution

---

## Solution

See:

```text
solutions/05-wrap-a-function.py
```