# Exercise <NUMBER> - <TITLE>

## Progression

```text
✅ Previous Exercise
➡️ Current Exercise
⬜ Next Exercise
```

Example:

```text
✅ 01 Wrap a Function
✅ 02 Print Before Execution
➡️ 03 Print Before and After Execution
⬜ 04 Handle Positional Arguments
```

---

## Goal

Describe the primary learning objective of this exercise.

Example:

```text
Learn how a decorator can execute code both before and after a wrapped function runs.
```

---

## Prerequisites

Before attempting this exercise, you should understand:

- Exercise 01
- Exercise 02

---

## New Concept

Introduce the one new idea this exercise focuses on.

Example:

```text
Executing code after the wrapped function completes.
```

---

## Challenge

Describe what the learner must build.

Example:

Create a decorator named:

```python
announce
```

that prints a message before and after the decorated function executes.

---

## Requirements

Your solution must:

- Requirement 1
- Requirement 2
- Requirement 3

Example:

- Print `"Before"`
- Run the decorated function
- Print `"After"`

---

## Starter Code

Provide a minimal starting point.

```python
def announce(func):
    pass
```

---

## Expected Usage

Show how the finished solution should be used.

```python
@announce
def greet():
    print("Hello")


greet()
```

---

## Expected Output

```text
Before
Hello
After
```

---

## Hints

### Hint 1

Small hint.

---

### Hint 2

Medium hint.

---

### Hint 3

Large hint.

---

## Things to Try

Experiment beyond the basic requirements.

Examples:

- What happens if the function accepts arguments?
- What happens if the function returns a value?
- What happens if the function raises an exception?

---

## Reflection

Answer these questions after completing the exercise.

1. What new concept did you learn?
2. How does this exercise build on previous exercises?
3. When might you use this in a real project?
4. What was most difficult to understand?

---

## Stretch Goal

Optional challenge for deeper understanding.

Example:

```text
Modify the decorator so that it accepts a custom message.
```

---

## Real-World Connection

Where might this concept appear in real software?

Example:

```text
Decorators are commonly used for:

- Logging
- Timing
- Authentication
- Caching
- Validation
```

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The solution works
- [ ] You understand why it works
- [ ] You can explain the solution to another developer
- [ ] You can modify the solution without help

---

## Solution

See:

```text
solutions/<FILE_NAME>.py
```