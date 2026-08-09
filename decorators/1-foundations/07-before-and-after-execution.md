# Exercise 07 - Before and After Execution

## Progression

```text
✅ 01 Functions Are Objects
✅ 02 Pass Function as Argument
✅ 03 Return a Function
✅ 04 Create Your First Wrapper
✅ 05 Wrap a Function
✅ 06 Before Execution
➡️ 07 Before and After Execution
⬜ 08 Understanding @ Syntax
⬜ 09 Multiple Decorated Functions
```

---

## Goal

Learn how a wrapper function can execute code both before and after the wrapped function runs.

In the previous exercise, you learned how a wrapper can perform work before a function executes.

In this exercise, you will extend the pattern by adding behavior both before and after execution.

This is one of the most common decorator patterns in real-world Python code.

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01 - Functions Are Objects
- Exercise 02 - Pass Function as Argument
- Exercise 03 - Return a Function
- Exercise 04 - Create Your First Wrapper
- Exercise 05 - Wrap a Function
- Exercise 06 - Before Execution

---

## New Concept

A wrapper can execute code around another function.

Example:

```python
def wrapper():
    print("Before")
    func()
    print("After")
```

Output:

```text
Before
Hello!
After
```

The wrapper surrounds the function execution.

---

## Challenge

Create a function named:

```python
say_hello()
```

that prints:

```text
Hello!
```

Create a function named:

```python
wrap()
```

that:

1. Receives another function
2. Creates a wrapper
3. Prints:

```text
Before
```

4. Executes the wrapped function
5. Prints:

```text
After
```

6. Returns the wrapper

Then:

1. Wrap `say_hello`
2. Store the returned wrapper
3. Execute the wrapper

---

## Requirements

Your solution must:

- Create a function named `say_hello`
- Create a function named `wrap`
- Receive a function as an argument
- Create a nested wrapper function
- Print `"Before"`
- Execute the wrapped function
- Print `"After"`
- Return the wrapper
- Produce the expected output

---

## Starter Code

```python
def say_hello():
    pass


def wrap(func):
    def wrapper():
        pass

    return wrapper


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
        print("Before")
        func()
        print("After")

    return wrapper


wrapped_hello = wrap(say_hello)

wrapped_hello()
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

The wrapped function should still be executed:

```python
func()
```

---

### Hint 2

Anything before:

```python
func()
```

runs before the wrapped function.

Anything after:

```python
func()
```

runs after the wrapped function.

---

### Hint 3

The order matters.

This:

```python
print("Before")
func()
print("After")
```

produces a different result than:

```python
func()
print("Before")
print("After")
```

---

### Hint 4

Remember to return:

```python
wrapper
```

not:

```python
wrapper()
```

---

## Things to Try

After completing the exercise, experiment with these variations.

### Try 1

Replace the messages with:

```text
Starting...
Finished.
```

---

### Try 2

Wrap a second function:

```python
say_goodbye()
```

and verify that the messages appear around it as well.

---

### Try 3

Add additional messages:

```python
print("Preparing...")
print("Before")
func()
print("After")
print("Cleaning up...")
```

---

### Try 4

Create a wrapper that counts how many functions have been executed.

(You don't need to store the count yet, just print a message.)

---

## Reflection

Answer the following questions.

1. Why does the wrapper execute code before and after the function?
2. How does the wrapper change behavior without modifying the original function?
3. Why is this pattern useful?
4. What kinds of tasks might be performed before execution?
5. What kinds of tasks might be performed after execution?

---

## Stretch Goal

Modify the wrapper so it prints the function name in both messages.

Expected output:

```text
Starting say_hello...
Hello!
Finished say_hello.
```

Hint:

```python
func.__name__
```

may be useful.

---

## Real-World Connection

Many production decorators use this exact pattern.

Examples include:

- Logging when a function starts and ends
- Measuring execution time
- Opening and closing resources
- Creating audit trails
- Tracking success or failure of operations

The general pattern is:

```python
def wrapper():
    do_something_before()

    func()

    do_something_after()
```

This is the core behavior behind many useful decorators.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You can create a wrapper that executes code before a function
- [ ] You can create a wrapper that executes code after a function
- [ ] You understand execution order
- [ ] You can explain why the wrapped function is unchanged
- [ ] You understand how wrappers can add behavior around existing functions
- [ ] You are ready to learn how Python's `@` syntax works

---

## Solution

See:

```text
solutions/07-before-and-after-execution.py
```