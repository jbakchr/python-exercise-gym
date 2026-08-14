# Exercise 27 - Typed Data Processor

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
➡️ Current Manipulation Exercise
⬜ Exercise 28 - Typed Service Interfaces
```

---

## Goal

Use:

```text
TypeVar
Callable
Generic Utility Design
Typed Functions
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable typed data processor that
can transform values while preserving
type safety.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Function type annotations
- Type aliases
- Callable
- Generic classes
- Generic functions
- TypeVar
- Reusable utility design

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are processing incoming data.

You may need to:

```text
Convert usernames to uppercase

Format strings

Process numbers

Transform configuration values

Prepare API data
```

In many applications, the same processing pattern occurs repeatedly:

```text
Take a value
↓
Apply a transformation
↓
Return the result
```

Rather than creating a separate function for every situation, you want to build a reusable utility that can process values using different transformation functions.

The goal is to create a type-safe processing utility that can be reused throughout an application.

---

## Challenge

Build a solution that:

1. Defines a reusable processor type.
2. Accepts a value and a processing function.
3. Applies the processing function.
4. Returns the transformed value.
5. Preserves type information.

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

- The processor should:

```text
Accept a value of type T
Return a value of type T
```

- Create a function:

```python
def process(value: T, processor: Processor[T]) -> T:
```

that applies the processor function and returns the result.

- Create a processing function named:

```python
to_uppercase
```

that converts a string to uppercase.

- Demonstrate the utility using the value:

```python
"alice"
```

Your solution should not:

- Use `Any`
- Duplicate processing logic
- Hardcode the final result

---

## Starter Code

```python
from typing import Callable, TypeVar


# Create a TypeVar


# Create a Processor type alias


def to_uppercase(value):
    pass


def process(value, processor):
    pass


print(process("alice", to_uppercase))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Accept a processing function.
Transform a value.
Return the transformed value.
Reuse the same utility with different processors.
```

Expected output:

```text
ALICE
```

You should also be able to explain:

- Why Callable is useful
- Why TypeVar is useful
- How processing functions promote reuse
- How type information is preserved

---

## Hints

### Hint 1

Think about the processor signature:

```python
Callable[[T], T]
```

---

### Hint 2

The processing utility should not know *how* the value is transformed.

It should only execute the processor.

---

### Hint 3

Your `process()` function will likely be very short.

Focus on reusability rather than complexity.

---

## Possible Improvements

Once the basic solution works, consider:

- Creating additional processors
- Processing integers
- Processing configuration values
- Processing API response data
- Building a small transformation library

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does a reusable processor solve?
2. How is this exercise similar to the validation helper exercise?
3. Why is TypeVar useful here?
4. Where might this pattern appear in a real application?

---

## Stretch Goal

Extend the utility with one additional feature.

Create a second processor:

```python
def add_exclamation(value: str) -> str:
```

Then use it with the same processing utility.

---

## Real-World Connection

This pattern appears in:

- Data transformation pipelines
- ETL systems
- API response processing
- Configuration processing
- Utility libraries

Developers frequently separate transformation logic from orchestration logic.

Typed processors make these transformations easier to reuse, test, and maintain while preserving strong type information.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] A `TypeVar` is implemented
- [ ] A `Processor` type alias is implemented
- [ ] `Callable` is used correctly
- [ ] `process()` works correctly
- [ ] `to_uppercase()` works correctly
- [ ] Type information is preserved
- [ ] You understand how generic processing utilities work

---

## Solution

See:

```text
solutions/27-typed-data-processor.py
```