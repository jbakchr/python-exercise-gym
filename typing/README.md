## Typing

Learn typing through deliberate practice.

The goal of this topic is not simply to understand type hints, but to become comfortable using Python's typing system to write clearer, safer, and more maintainable code.

By the end of this exercise path, you should be able to:

- Understand the purpose of type annotations
- Add meaningful type hints to functions and variables
- Work with common typing constructs
- Create reusable type definitions
- Build generic and type-safe code
- Recognize common typing patterns
- Solve practical problems using typing
- Improve code readability and developer experience

### What Is Typing?

Typing refers to Python's type annotation system, which allows developers to describe the kinds of values a function, variable, or object is expected to use.

Type hints do not change how Python executes code, but they provide information that can help:

- Humans understand code more quickly
- Editors provide better autocomplete
- Static type checkers catch mistakes earlier
- Teams maintain larger codebases more confidently

Simple example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Example output:

```text
Hello, Alice
```

In this example:

```python
name: str
```

indicates that `name` should be a string.

```python
-> str
```

indicates that the function returns a string.

Typing is commonly used in:

- APIs
- Libraries
- Large applications
- Data processing
- Automation tools
- Professional Python codebases

As projects grow, type hints help developers understand expectations and catch mistakes before code reaches production.

### Exercise Philosophy

The exercises in this topic are designed to build on each other.

Instead of learning many typing concepts at once, every exercise introduces one new idea while reinforcing previous knowledge.

```text
Exercise 01
↓
Exercise 02 requires Exercise 01
↓
Exercise 03 requires Exercise 01 + 02
↓
Exercise 04 requires Exercise 01 + 02 + 03
...
```

Knowledge accumulates.

Nothing is thrown away.

### Structure

```text
typing/
│
├── 1-foundations/
├── 2-exploration/
├── 3-manipulation/
├── 4-problem-solving/
├── 5-mini-project/
└── README.md
```

Each stage introduces new concepts and increasingly challenging exercises.

### 1. Foundations

Goal:

```text
Understand basic type annotations.
```

Topics include:

- Parameter annotations
- Return type annotations
- Variable annotations
- Optional values
- Union types
- Collection types
- Type aliases

Example exercises:

```text
01 Basic Parameter Types
02 Return Types
03 Multiple Parameters
```

### 2. Exploration

Goal:

```text
Explore commonly used typing features.
```

Topics include:

- TypedDict
- NewType
- Literal
- Callable
- Any
- Type narrowing
- Type inference

Example exercises:

```text
11 Typed User Records
12 Literal Values
13 Callable Functions
```

### 3. Manipulation

Goal:

```text
Use typing to improve practical code.
```

Topics include:

- Typed configuration data
- Typed APIs
- Reusable type aliases
- Validation helpers
- Generic utilities

Example exercises:

```text
21 Typed Configuration Loader
22 Typed Data Transformer
23 Generic Stack
```

### 4. Problem Solving

Goal:

```text
Apply typing to realistic software development problems.
```

Topics include:

- Refactoring legacy code
- Eliminating ambiguous types
- Designing safer interfaces
- Using protocols
- Building generic solutions

Example exercises:

```text
31 Refactor Untyped Code
32 Replace Any
33 Type-Safe Plugin System
```

### 5. Mini Project

Goal:

```text
Combine everything learned throughout the topic.
```

Example project:

```text
Type-Safe Configuration Framework
```

Possible features:

- Typed application settings
- Typed configuration schema
- Validation helpers
- Generic configuration loader
- Reusable type aliases

The project should require knowledge from all previous sections.

### Recommended Workflow

For each exercise:

- Read the challenge.
- Attempt a solution without looking at hints.
- Experiment with variations.
- Refactor your solution.
- Compare with the provided solution.
- Move on only when the concept feels comfortable.

### Mastery Checklist

Before leaving this topic, you should be able to confidently explain:

- What type hints are
- Why typing exists
- When type hints provide value
- How to annotate functions
- How to annotate collections
- How Optional and Union differ
- When to use TypedDict
- What generics solve
- How Protocols support flexible design
- Common typing mistakes
- How typing improves maintainability

If you can complete the mini project without referring to previous exercises, you've likely achieved a solid working understanding of typing.

### Remember

The goal is not to memorize typing syntax.

The goal is to develop the habit of expressing intent clearly in code.

When writing a new function, your instinct should eventually be:

```text
What types should this function accept and return?
```

Typing is not about satisfying a type checker.

Typing is about making code easier to understand, safer to change, and easier to maintain.