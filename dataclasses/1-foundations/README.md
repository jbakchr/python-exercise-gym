## Foundations

### Overview

The purpose of the Foundations stage is to understand the core ideas behind dataclasses.

Before dataclasses were introduced, Python developers often wrote a large amount of repetitive code simply to create objects that stored data.

Dataclasses provide a cleaner way to model structured data while automatically generating common methods such as:

```text
__init__
__repr__
__eq__
```

This stage focuses on understanding how dataclasses help transform simple collections of related values into organized, reusable application models.

The goal is to build a strong foundation before exploring more advanced features such as immutability, ordering, factories, and real-world data modelling.

### Learning Goals

By the end of this stage you should be able to:

- Understand what a dataclass is
- Create simple dataclasses
- Define fields using type annotations
- Instantiate dataclass objects
- Access and modify object attributes
- Understand automatically generated methods
- Use default values
- Work with optional fields
- Model simple real-world data using dataclasses
- Explain why dataclasses are useful

More importantly, dataclasses should start feeling like a natural tool for modelling structured data.

### How This Stage Is Structured

The exercises are intentionally progressive.

Each exercise introduces one new idea and builds upon previous exercises.

The goal is not to memorize `@dataclass`.

The goal is to understand how dataclasses help organize and model data.

Progression:

```text
01 Creating Your First Dataclass
↓
02 Adding Multiple Fields
↓
03 Using Type Annotations
↓
04 Creating Dataclass Objects
↓
05 Accessing Attributes
↓
06 Understanding Generated __init__
↓
07 Understanding Generated __repr__
↓
08 Comparing Dataclass Objects
↓
09 Using Default Values
↓
10 Building a Simple Data Model
```

Think of the exercises as a skill ladder rather than a checklist.

### Recommended Approach

For each exercise:

- Read the challenge carefully.
- Attempt a solution before viewing hints.
- Use hints only when necessary.
- Experiment with the "Things to Try" section.
- Compare your work with the solution.
- Complete the reflection questions.
- Move on only when the concept feels comfortable.

The goal is understanding, not speed.

### Exercises

#### 01 Creating Your First Dataclass

Learn how to create a basic dataclass using the `@dataclass` decorator.

#### 02 Adding Multiple Fields

Create dataclasses containing several related pieces of information.

#### 03 Using Type Annotations

Learn how dataclasses and type hints work together.

#### 04 Creating Dataclass Objects

Create instances of dataclasses and provide values for their fields.

#### 05 Accessing Attributes

Read and modify values stored inside dataclass objects.

#### 06 Understanding Generated __init__

Explore how dataclasses automatically create constructors.

#### 07 Understanding Generated __repr__

Learn how dataclasses automatically create useful string representations.

#### 08 Comparing Dataclass Objects

Discover how dataclasses compare objects based on their fields.

#### 09 Using Default Values

Create fields that automatically receive default values.

#### 10 Building a Simple Data Model

Combine everything learned to model a realistic piece of application data.

### Success Criteria

You are ready to continue to the Exploration stage when:

- All exercises are complete
- You understand what problems dataclasses solve
- You can create dataclasses without assistance
- You understand generated `__init__` and `__repr__` methods
- You can work with dataclass attributes confidently
- You can use default values appropriately
- You can model simple real-world entities using dataclasses
- Dataclasses feel more natural than manually writing repetitive data classes

### What Comes Next?

Next:

```text
2-exploration
```

In the Exploration stage you will investigate more advanced dataclass features including:

- Default factories
- Frozen dataclasses
- Ordering
- Post-initialization processing
- Nested dataclasses
- Field customization

The focus shifts from:

```text
How dataclasses work
```

to:

```text
What dataclasses can do
```

### Remember

Reading creates familiarity.

Practice creates skill.

Repetition creates mastery.

The goal of this stage is not to memorize dataclass syntax.

The goal is to build an intuition for modelling structured data.

Once dataclasses feel natural, they become one of the most powerful tools in modern Python application design.