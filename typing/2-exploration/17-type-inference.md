# Exercise 17 - Type Inference

## Progression

```text
✅ Exercise 11 - TypedDict
✅ Exercise 12 - Literal
✅ Exercise 13 - Callable
✅ Exercise 14 - Any
✅ Exercise 15 - NewType
✅ Exercise 16 - NamedTuple
➡️ Current Exploration Exercise
⬜ Exercise 18 - Type Narrowing
⬜ Future Exploration Exercises
```

---

## Goal

Explore how:

```text
Type Inference
```

behaves in different situations.

By the end of this exercise you should understand:

- What type inference is
- When Python developers can rely on inference
- When explicit annotations improve readability

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Collection annotations
- TypedDict
- NamedTuple

If not, review:

```text
Exercise 01 - Basic Parameter Types
Exercise 06 - Lists and Collections
Exercise 11 - TypedDict
Exercise 16 - NamedTuple
```

---

## Focus Area

This exercise explores:

```text
How types can often be inferred
without being explicitly written.
```

Example:

```python
name = "Alice"
```

Most type checkers can infer:

```python
name: str
```

without an explicit annotation.

This is not a new typing feature.

Instead, it is an investigation into how type checkers use information that already exists in your code.

---

## Challenge

Investigate the following behavior.

Your task is to:

1. Create several variables without type annotations
2. Assign different kinds of values
3. Determine what types a type checker would infer
4. Add explicit annotations and compare the results

As you work, pay attention to:

- When annotations feel unnecessary
- When annotations improve clarity
- How inference behaves with different values

---

## Starter Code

```python
name = "Alice"
age = 30
is_active = True

users = ["Alice", "Bob", "Charlie"]
```

---

## Questions To Investigate

As you complete the exercise, try to answer:

### Question 1

```text
How does a type checker determine
the type of a variable?
```

---

### Question 2

```text
When is an explicit annotation
unnecessary?
```

---

### Question 3

```text
When does an explicit annotation
make code easier to understand?
```

---

## Verify Your Understanding

You should be able to explain:

- What type inference is
- Why type inference exists
- When explicit annotations are still valuable

You should also observe:

```text
Not every variable requires an
explicit annotation.

In many situations the type
can be inferred automatically.
```

Avoid checking the solution until you can explain why the behavior occurs.

---

## Hints

### Hint 1

Consider:

```python
name = "Alice"
```

What type would a type checker infer?

---

### Hint 2

Consider:

```python
count = 10
```

What type would be inferred?

---

### Hint 3

Compare:

```python
name = "Alice"
```

with:

```python
name: str = "Alice"
```

What additional information is being provided?

---

## Experiment Further

Now modify your solution and observe what changes.

### Experiment 1

Try:

```python
score = 99.5
```

What type would be inferred?

---

### Experiment 2

Try:

```python
items = ["apple", "banana"]
```

What information can be inferred about the list?

---

### Experiment 3

Try:

```python
data = []
```

What type information is available now?

Why might an annotation be useful here?

---

## Observations

Write down your findings.

Consider:

- What surprised you?
- What behaved as expected?
- When does inference work well?
- When does inference become less clear?

---

## Reflection

Answer the following questions.

1. What did this exercise reveal about type inference?
2. When can you rely on inference?
3. When are explicit annotations beneficial?
4. What patterns do you notice?

---

## Stretch Goal

Create two versions of the same code:

### Version 1

Use explicit annotations everywhere.

### Version 2

Rely on inference wherever possible.

Compare readability and decide which style you prefer.

The goal is not to build something larger.

The goal is to deepen your understanding.

---

## Real-World Connection

This behavior appears in situations such as:

- Everyday Python development
- Application code
- Libraries and frameworks
- Data processing scripts
- Test suites

Understanding type inference matters because most typed Python code uses a combination of:

```text
Explicit annotations
+
Type inference
```

Professional developers rarely annotate every variable.

Instead, they use annotations where they improve clarity and rely on inference where the type is already obvious.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] You completed the investigation
- [ ] You observed the expected behavior
- [ ] You can explain what type inference is
- [ ] You understand when annotations are optional
- [ ] You explored at least one variation
- [ ] You feel comfortable experimenting further

---

## Solution

See:

```text
solutions/17-type-inference.py
```