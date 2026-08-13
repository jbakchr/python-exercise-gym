## Typing – Exploration

### Overview
  
You now know the foundations of Python type annotations.

You have:
- Annotated parameters
- Annotated return values
- Used Optional and Union
- Annotated collections
- Worked with nested structures
- Created type aliases
- Annotated realistic functions
- Built a typed utility

The next step is not learning more basic annotations.

The next step is understanding how Python's typing system is used to model real data, describe behavior, and improve code quality in larger applications.

This stage focuses on exploration.

You will investigate more advanced typing tools, observe how they affect code design, and discover patterns commonly used in professional Python projects.

The goal is to move from:

```text
"I know how to add type annotations."
```

to:

```text
"I know how to model data and behavior with types."
```

### Learning Goal
  
By the end of this stage you should be comfortable with:

- Defining structured dictionary types with TypedDict
- Restricting values with Literal
- Describing callable objects with Callable
- Understanding when Any is appropriate
- Creating domain-specific types with NewType
- Working with NamedTuple
- Understanding type inference
- Using type narrowing techniques
- Annotating methods with Self
- Reading and understanding advanced type annotations

### What Makes Exploration Different?
  
Foundations focused on learning the building blocks of typing.

Exploration focuses on investigating how typing behaves in real applications.

You will intentionally ask questions like:

```text
How can I describe the shape of a dictionary?

How can I restrict values to a specific set?

How do I annotate functions that receive functions?

When should I avoid Any?

How can I create safer domain-specific types?

How do type checkers become more precise?

How do professional Python projects use these tools?
```

The goal is to develop intuition through experimentation.

### Stage Progression
  
The exercises in this stage build on each other.

Pattern:

```text
11 → TypedDict
12 → Literal
13 → Callable
14 → Any
15 → NewType
16 → NamedTuple
17 → Type Inference
18 → Type Narrowing
19 → Self
20 → Advanced Annotation Patterns
```

Each exercise introduces one new idea while reinforcing previous concepts.

### Recommended Approach
  
For every exercise:

- Read the requirements carefully.
- Predict how the type annotations should behave.
- Implement a solution.
- Run experiments.
- Try the stretch goals.
- Compare with the provided solution.
- Complete the reflection questions.

Do not rush through the exercises.

The value comes from observing how different typing tools improve clarity, safety, and maintainability.

### Common Questions You Should Be Asking
  
Throughout this stage, regularly stop and ask:

```text
What information am I trying to describe?

Can this type be more precise?

Would another developer immediately understand this annotation?

Could a type checker catch mistakes here?

Is this type helping or making the code harder to read?

What assumptions am I making about my data?
```

Curiosity is more important than speed.

### Success Criteria
  
By the end of the Exploration stage you should be able to:

- Model structured data with TypedDict
- Restrict values with Literal
- Annotate functions using Callable
- Explain the risks and benefits of Any
- Create domain-specific types with NewType
- Use NamedTuple effectively
- Explain how type inference works
- Apply type narrowing techniques
- Use Self in class methods
- Read and understand more advanced type annotations

Most importantly, type annotations should begin to feel like a design tool rather than merely additional syntax.

### Remember
  
Typing is about communication.

Type annotations help communicate:

```text
What data looks like

What functions expect

What functions return

What assumptions the code makes
```

Everything in this stage builds toward writing code that is easier to understand, safer to modify, and more predictable to use.

```text
Read
↓
Experiment
↓
Model
↓
Understand
↓
Master
```
