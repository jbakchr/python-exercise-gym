# Decorators – Exploration

## Overview

You now know the building blocks of decorators.

You have:

- Passed functions as arguments
- Returned functions from functions
- Wrapped functions
- Used the `@` syntax
- Built simple decorators

The next step is not learning new syntax.

The next step is understanding how decorators behave in real situations.

This stage focuses on exploration.

You will experiment with decorators, observe their behavior, and discover common patterns used in everyday Python development.

The goal is to move from:

```text
"I know how decorators work."
```

to:

```text
"I understand how decorators behave."
```

---

## Learning Goal

By the end of this stage you should be comfortable with:

- Decorating functions that accept arguments
- Decorating functions with keyword arguments
- Handling return values correctly
- Writing flexible wrappers
- Understanding function metadata
- Preserving metadata with `functools.wraps`
- Combining multiple decorators
- Recognizing common decorator patterns

---

## What Makes Exploration Different?

Foundations focused on building decorators.

Exploration focuses on investigating them.

You will intentionally ask questions like:

```text
What happens if the function takes arguments?
```

```text
What happens if the function returns a value?
```

```text
What information gets lost when a function is decorated?
```

```text
What happens when decorators are stacked?
```

```text
How can one decorator work with many different functions?
```

The goal is to develop intuition through experimentation.

---

## Stage Progression

The exercises in this stage build on each other.

Pattern:

```text
01 → Functions with arguments
02 → Multiple arguments
03 → Keyword arguments
04 → Flexible wrappers
05 → Return values
06 → Reusable decorators
07 → Metadata inspection
08 → Preserving metadata
09 → Stacked decorators
10 → Putting it all together
```

Each exercise introduces one new idea while reinforcing previous concepts.

---

## Recommended Approach

For every exercise:

1. Read the requirements carefully.
2. Predict what the code should do.
3. Implement a solution.
4. Run experiments.
5. Try the stretch goals.
6. Compare with the provided solution.
7. Complete the reflection questions.

Do not rush through the exercises.

The value comes from observing behavior and testing ideas.

---

## Common Questions You Should Be Asking

Throughout this stage, regularly stop and ask:

```text
What is the wrapper actually receiving?
```

```text
What does the wrapper return?
```

```text
What information belongs to the original function?
```

```text
What information belongs to the wrapper?
```

```text
What changes when another decorator is added?
```

Curiosity is more important than speed.

---

## Success Criteria

By the end of the Exploration stage you should be able to:

- Write decorators that work with arbitrary arguments
- Return values correctly from decorated functions
- Preserve function metadata
- Explain what `functools.wraps` does
- Predict the order of execution in stacked decorators
- Adapt a decorator to different kinds of functions

Most importantly, decorators should start feeling predictable rather than magical.

---

## Remember

Decorators are just functions.

Everything in this stage builds on the same idea:

```text
Function
↓
Wrapped by another function
↓
Called through the wrapper
```

The more situations you observe, the stronger your intuition becomes.

```text
Read
↓
Experiment
↓
Observe
↓
Understand
↓
Master
```