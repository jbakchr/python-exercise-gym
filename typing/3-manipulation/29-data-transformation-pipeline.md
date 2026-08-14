# Exercise 29 - Data Transformation Pipeline

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
✅ Exercise 23 - Typed API Responses
✅ Exercise 24 - Generic Container
✅ Exercise 25 - Typed Validation Helpers
✅ Exercise 26 - Type Utility Functions
✅ Exercise 27 - Typed Data Processor
✅ Exercise 28 - Service Interface Design
➡️ Current Manipulation Exercise
⬜ Exercise 30 - Typing Utility Toolbox
```

---

## Goal

Use:

```text
TypeVar
Callable
Type Aliases
Typed Function Composition
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A type-safe data transformation pipeline
that applies multiple processing steps
to a value.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Function type annotations
- Type aliases
- Callable
- TypeVar
- Generic utility functions
- Typed data processors
- Reusable utility design

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are processing data before storing it.

For example:

```text
Usernames may need trimming.

Names may need capitalization.

Data may need normalization.

Configuration values may need cleanup.
```

Very often data passes through multiple transformation steps:

```text
Input
↓
Transform
↓
Transform
↓
Transform
↓
Output
```

Instead of manually performing each step, you want to build a reusable pipeline utility.

The goal is to create a type-safe processing pipeline that can apply multiple transformations in sequence.

---

## Challenge

Build a solution that:

1. Defines a reusable processor type.
2. Accepts multiple processing functions.
3. Applies them in order.
4. Returns the final transformed value.
5. Preserves type information throughout the process.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type variable named:

```python
T
```

- Create a type alias named:

```python
Processor
```

using:

```python
Callable
```

- A processor should:

```text
Accept a value of type T
Return a value of type T
```

- Create a function:

```python
def run_pipeline(
    value: T,
    processors: list[Processor[T]],
) -> T:
```

- The function should:
  - Process the value using each processor in order
  - Return the final result

- Create two processor functions:

```python
strip_whitespace
```

and

```python
to_uppercase
```

- Demonstrate the pipeline using:

```python
"  alice  "
```

Your solution should not:

- Use `Any`
- Duplicate transformation logic
- Hardcode the final result

---

## Starter Code

```python
from typing import Callable, TypeVar


# Create a TypeVar


# Create a Processor type alias


def strip_whitespace(value):
    pass


def to_uppercase(value):
    pass


def run_pipeline(value, processors):
    pass


result = run_pipeline(
    "  alice  ",
    [
        strip_whitespace,
        to_uppercase,
    ],
)

print(result)
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Accept multiple processors.
Apply them in order.
Return the final transformed value.
Reuse the same pipeline with other processors.
```

Expected output:

```text
ALICE
```

You should also be able to explain:

- Why pipelines are useful
- Why Callable is useful
- Why TypeVar is useful
- How processing stages remain reusable

---

## Hints

### Hint 1

A processor type may look similar to:

```python
Callable[[T], T]
```

---

### Hint 2

Loop through each processor and update the value after each step.

---

### Hint 3

Each processor should only have a single responsibility.

The pipeline combines them together.

---

## Possible Improvements

Once the basic solution works, consider:

- Adding additional processors
- Text normalization
- Configuration processing
- API response cleanup
- Building a reusable utility module

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does a transformation pipeline solve?
2. How does this exercise build upon Exercise 27?
3. Why is it useful to separate processing steps?
4. Where might you use pipelines in a real application?

---

## Stretch Goal

Extend the utility with one additional feature.

Create a processor:

```python
def add_exclamation(value: str) -> str:
```

and add it to the pipeline.

Expected output:

```text
ALICE!
```

---

## Real-World Connection

This pattern appears in:

- Data processing systems
- ETL pipelines
- API response normalization
- Configuration processing
- Machine learning preprocessing

Developers frequently build workflows where data passes through a sequence of reusable transformation steps.

Typed pipelines make these workflows easier to understand, test, and extend while preserving strong type information.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `TypeVar` is implemented
- [ ] A `Processor` type alias is implemented
- [ ] Multiple processors can be applied
- [ ] `run_pipeline()` works correctly
- [ ] The final output is correct
- [ ] Type information is preserved
- [ ] You understand the value of transformation pipelines

---

## Solution

See:

```text
solutions/29-data-transformation-pipeline.py
```