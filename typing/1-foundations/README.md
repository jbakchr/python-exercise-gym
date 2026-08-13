## Foundations

### Overview

The purpose of the Foundations stage is to understand the core ideas behind Python's type annotation system.

Typing is often introduced as something you add to satisfy a type checker.

It is not.

At its core, typing is about communicating intent.

Typing helps answer questions like:

```text
What kind of value should this function receive?

What kind of value should it return?

What data structure is expected here?

What assumptions can other developers safely make?
```

This stage focuses on the building blocks of type annotations.

You will learn how to describe values, functions, collections, and common data structures using Python's typing system.

The goal is not to memorize syntax.

The goal is to learn how to express the shape of your code clearly and consistently.

### Learning Goals

By the end of this stage you should be able to:

- Understand why type hints exist
- Add type hints to function parameters
- Add type hints to return values
- Annotate variables
- Annotate common collection types
- Use Optional values appropriately
- Use Union types to represent multiple possibilities
- Create simple type aliases
- Read and understand common type annotations
- Explain the benefits and limitations of type hints

More importantly, type annotations should feel useful rather than intimidating.

### How This Stage Is Structured

The exercises are intentionally progressive.

Each exercise introduces one new idea and builds upon previous exercises.

The goal is not to learn every feature in the `typing` module.

The goal is to build a solid foundation that future exercises can build upon.

Progression:

```text
01 Basic Parameter Types
↓
02 Return Types
↓
03 Multiple Parameters
↓
04 Optional Values
↓
05 Union Types
↓
06 Lists and Collections
↓
07 Dictionaries and Nested Structures
↓
08 Type Aliases
↓
09 Annotating Real Functions
↓
10 Build a Typed Utility
```

Think of the exercises as a skill ladder rather than a checklist.

Each exercise should make the next exercise feel easier.

### Recommended Approach

For each exercise:

- Read the challenge carefully.
- Attempt a solution before viewing hints.
- Use hints only when necessary.
- Experiment with your own variations.
- Refactor and improve your solution.
- Compare your work with the solution.
- Complete the reflection questions.
- Move on only when the concept feels comfortable.

The goal is understanding, not speed.

### Exercises

#### 01 Basic Parameter Types

Add simple type hints to function parameters such as strings, integers, floats, and booleans.

#### 02 Return Types

Add return type annotations and practice reading typed function signatures.

#### 03 Multiple Parameters

Annotate functions that accept several different parameter types.

#### 04 Optional Values

Learn how to represent values that may be missing.

#### 05 Union Types

Allow functions to work with more than one valid type.

#### 06 Lists and Collections

Annotate common collection types such as lists, tuples, and sets.

#### 07 Dictionaries and Nested Structures

Describe more complex data structures using type annotations.

#### 08 Type Aliases

Create reusable names for complex type definitions.

#### 09 Annotating Real Functions

Apply everything learned so far to realistic utility functions.

#### 10 Build a Typed Utility

Combine all previous concepts to build a small, properly typed utility.

### Success Criteria

You are ready to continue to the Exploration stage when:

- All exercises are complete
- You understand why type hints exist
- You can annotate parameters and return values confidently
- You can annotate common collection types
- You understand the difference between Optional and Union
- You can create and use type aliases
- You can read and understand typed function signatures
- Type annotations feel natural rather than unfamiliar

### What Comes Next?

Next:

```text
2-exploration
```

In the Exploration stage you will investigate more advanced typing features, including:

- TypedDict
- NewType
- Literal
- Callable
- Any
- Type inference
- Type narrowing

The focus shifts from:

```text
How do I write type hints?
```

to:

```text
How do I model data and behaviour effectively?
```

### Remember

Reading creates familiarity.

Practice creates skill.

Repetition creates mastery.

The goal of this stage is not to memorize typing syntax.

The goal is to develop the habit of expressing intent clearly.

Once basic type annotations become second nature, Python code becomes easier to understand, easier to maintain, and easier to evolve.