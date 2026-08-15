## Dataclasses – Exploration

### Overview

You now understand the core building blocks of dataclasses.

You have:
- Created dataclasses
- Defined fields
- Used type annotations
- Created objects
- Accessed attributes
- Used generated methods
- Compared instances
- Worked with default values
- Built simple data models

The next step is not learning how to create dataclasses.

The next step is understanding how dataclasses behave in more realistic situations.

This stage focuses on exploration.

You will investigate advanced dataclass features, experiment with different configurations, and observe how dataclasses can be customized to fit real-world needs.

The goal is to move from:

```text
"I know how to create a dataclass."
```

to:

```text
"I understand how dataclasses behave."
```

### Learning Goals

By the end of this stage you should be comfortable with:

- Using default_factory for mutable defaults
- Creating immutable dataclasses
- Understanding field ordering rules
- Customizing fields with field()
- Creating ordered dataclasses
- Using post-initialization processing
- Working with nested dataclasses
- Converting dataclasses to dictionaries
- Understanding dataclass-generated behavior
- Recognizing common dataclass design patterns

### What Makes Exploration Different?

Foundations focused on creating dataclasses.

Exploration focuses on investigating them.

You will intentionally ask questions such as:

```text
What happens when a field contains a list?
What is the difference between default and default_factory?
How can a dataclass be made immutable?
What happens when dataclasses contain other dataclasses?
How can fields be customized?
What code runs after initialization?
What methods can dataclasses generate automatically?
```

The goal is to develop intuition through experimentation.

### Stage Progression

The exercises in this stage build on each other.

Pattern:

```text
11 → Default Values Revisited
12 → Using default_factory
13 → Working with Mutable Fields
14 → Immutable Dataclasses
15 → Ordered Dataclasses
16 → Customizing Fields with field()
17 → Post-Initialization Processing
18 → Nested Dataclasses
19 → Converting Dataclasses to Dictionaries
20 → Exploring Dataclass Utilities
```

Each exercise introduces one new idea while reinforcing previous concepts.

### Recommended Approach

For every exercise:

- Read the requirements carefully.
- Predict how the dataclass should behave.
- Implement a solution.
- Run experiments.
- Try the stretch goals.
- Compare with the provided solution.
- Complete the reflection questions.

Do not rush through the exercises.

The value comes from observing behavior and testing ideas.

### Common Questions You Should Be Asking

Throughout this stage, regularly stop and ask:

```text
Why does this field behave differently?
What code is generated automatically?
Could this object be made immutable?
Should this field use a default value or a factory?
What happens when objects contain other objects?
What belongs inside __post_init__?
How would this design work in a larger application?
```

Curiosity is more important than speed.

### Exercises

#### 11

Default Values Revisited

Explore how default values are assigned and understand potential pitfalls when working with mutable data.

#### 12

Using default_factory

Learn how default_factory generates new default objects for every instance.

#### 13

Working with Mutable Fields

Investigate how lists, dictionaries, and sets behave inside dataclasses.

#### 14

Immutable Dataclasses

Create frozen dataclasses and explore the benefits of immutable data models.

#### 15

Ordered Dataclasses

Generate comparison methods automatically and investigate object ordering.

#### 16

Customizing Fields with field()

Learn how field() changes dataclass behavior and configuration.

#### 17

Post-Initialization Processing

Use __post_init__ to perform calculations and validation after object creation.

#### 18

Nested Dataclasses

Model more complex structures by combining multiple dataclasses.

#### 19

Converting Dataclasses to Dictionaries

Use dataclass utilities to transform objects into serializable structures.

#### 20

Exploring Dataclass Utilities

Investigate helper functions and generated functionality provided by the dataclasses module.

### Success Criteria

By the end of the Exploration stage you should be able to:

- Explain when to use default_factory
- Avoid common mutable-default pitfalls
- Create immutable dataclasses
- Customize fields using field()
- Use __post_init__ effectively
- Create nested data models
- Convert dataclasses into dictionaries and other representations
- Explain how generated methods behave

Most importantly, dataclasses should start feeling predictable rather than magical.

### What Comes Next?

After completing this stage, move on to:

```text
Dataclasses – Manipulation
```

In the next stage you will move beyond exploration and begin building practical utilities and reusable components using dataclasses.

The focus shifts from:

```text
Understanding dataclasses
```

to:

```text
Using dataclasses to build useful things
```

### Remember

Dataclasses are tools for modelling structured data.

Everything in this stage builds on the same idea:

```text
Data
↓
Structure
↓
Behavior
↓
Application
```

The more variations you explore, the stronger your intuition becomes.

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