# Exercise 18 - Type Narrowing

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
✅ Exercise 14 - Any
✅ Exercise 15 - NewType
✅ Exercise 16 - NamedTuple
✅ Exercise 17 - Type Inference
➡️ Current Exploration Exercise
⬜ Exercise 19 - Self
⬜ Exercise 20 - Advanced Annotation Patterns
```

---

## Goal

Explore how:

```text
Type Narrowing
```

behaves in different situations.

By the end of this exercise you should understand:

- What type narrowing is
- How Python can refine possible types using conditions
- How type checkers reason about code flow

---

## Previously Learned

Before starting this exercise you should already understand:

- Union types
- Optional values
- Type inference

If not, review:

```text
Exercise 04 - Optional Values
Exercise 05 - Union Types
Exercise 17 - Type Inference
```

---

## Focus Area

This exercise explores:

```text
Reducing a broad type into a
more specific type.
```

Example:

```python
str | int
```

can become:

```python
str
```

after checking:

```python
isinstance(value, str)
```

This is not a new annotation.

Instead, this exercise investigates how type checkers use program logic to become more confident about the type of a value.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create a function that accepts either a string or an integer
2. Use an if statement with isinstance()
3. Handle the string and integer cases separately
4. Display different information depending on the type

As you work, pay attention to:

- What the possible types are at the start
- What the possible types are after a check
- How the type checker's understanding changes

---

## Starter Code

```python
def process(value):
    pass


process("hello")
process(42)
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
Why can a type checker treat
"value" differently inside each
branch of the conditional?
```

---

### Question 2

```text
What information does isinstance()
provide?
```

---

### Question 3

```text
How does type narrowing make code
safer and easier to understand?
```

---

## Verify Your Understanding

You should be able to explain:

- What type narrowing is
- Why type narrowing exists
- How conditionals affect type information

You should also observe:

```text
A value can start with multiple
possible types.

After a type check, the possible
types become more specific.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Use a union annotation:

```python
str | int
```

---

### Hint 2

Try:

```python
isinstance(value, str)
```

inside an if statement.

---

### Hint 3

Provide different behavior for:

```python
str
```

and:

```python
int
```

values.

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
def process(value: str | int | float):
    ...
```

How many possible types exist now?

---

### Experiment 2

Try:

```python
if isinstance(value, int):
    ...
```

before checking for strings.

Does the logic still work?

---

### Experiment 3

Try:

```python
value: str | None
```

and check:

```python
if value is not None:
    ...
```

How does this narrow the type?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- How does program flow affect type information?
- What assumptions become safer after narrowing?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about type narrowing?
2. How does narrowing relate to Union types?
3. What patterns do you notice?
4. When might this be useful in real code?

---

## Stretch Goal

Create a function that accepts:

```python
str | list[str]
```

Use type checks to handle each case differently.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- User input processing
- API response handling
- Configuration parsing
- Optional values
- Data validation systems

Understanding type narrowing matters because real applications frequently work with values that could have multiple possible types.

Type narrowing helps both developers and type checkers reason about those values safely and accurately.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what type narrowing is
- [ ] You understand how type checks refine possible types
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/18-type-narrowing.py
```