# Foundations

## Overview

The purpose of the Foundations stage is to understand the core ideas that make decorators possible.

Decorators are often introduced as a special Python feature.

They are not.

Decorators are built from a small set of ideas:

```text
Functions are objects
↓
Functions can be passed around
↓
Functions can be returned
↓
Functions can wrap other functions
↓
Decorator syntax becomes obvious
```

This stage focuses on building those ideas one step at a time.

---

## Learning Goals

By the end of this stage you should be able to:

- Understand functions as first-class objects
- Pass functions to other functions
- Return functions from other functions
- Create wrapper functions
- Build simple decorators
- Use Python's `@decorator` syntax
- Explain how decorators work internally

More importantly, decorators should no longer feel like magic.

---

## How This Stage Is Structured

The exercises are intentionally progressive.

Each exercise introduces one new idea and builds upon previous exercises.

The goal is not to memorize decorator syntax.

The goal is to understand the mechanics behind decorators.

Progression:

```text
01 Functions Are Objects
↓
02 Pass Function as Argument
↓
03 Return a Function
↓
04 Create Your First Wrapper
↓
05 Wrap a Function
↓
06 Before Execution
↓
07 Before and After Execution
↓
08 Understanding @ Syntax
↓
09 Multiple Decorated Functions
↓
10 Build a Simple Announcer
```

Think of the exercises as a skill ladder rather than a checklist.

---

## Recommended Approach

For each exercise:

1. Read the challenge carefully.
2. Attempt a solution before viewing hints.
3. Use hints only when necessary.
4. Experiment with the "Things to Try" section.
5. Compare your work with the solution.
6. Complete the reflection questions.
7. Move on only when the concept feels comfortable.

The goal is understanding, not speed.

---

## Exercises

### 01 Functions Are Objects

Learn that functions can be stored in variables just like other values.

### 02 Pass Function as Argument

Learn that functions can be passed to other functions.

### 03 Return a Function

Learn that functions can be returned from other functions.

### 04 Create Your First Wrapper

Create a function that executes another function.

### 05 Wrap a Function

Combine previous concepts to dynamically wrap a function.

### 06 Before Execution

Use a wrapper to execute code before another function runs.

### 07 Before and After Execution

Use a wrapper to execute code around another function.

### 08 Understanding @ Syntax

Learn how Python's decorator syntax relates to manual wrapping.

### 09 Multiple Decorated Functions

Apply the same decorator to multiple functions.

### 10 Build a Simple Announcer

Combine everything learned to build a reusable decorator.

---

## Success Criteria

You are ready to continue to the Exploration stage when:

- [ ] All exercises are complete
- [ ] You understand how decorators work internally
- [ ] You can explain wrapper functions
- [ ] You can manually create a decorator
- [ ] You understand what `@decorator` does
- [ ] You can apply the same decorator to multiple functions
- [ ] Decorators no longer feel like magic

---

## What Comes Next?

Next:

```text
2-exploration
```

In the Exploration stage you will investigate how decorators behave with:

- Function arguments
- Keyword arguments
- Return values
- Function metadata
- More realistic use cases

The focus shifts from:

```text
How decorators work
```

to:

```text
How decorators behave
```

---

## Remember

```text
Reading creates familiarity.
Practice creates skill.
Repetition creates mastery.
```

The goal of this stage is not to memorize decorator syntax.

The goal is to build an intuition for why decorators work.

Once the underlying ideas feel natural, decorators become much easier to use and understand.