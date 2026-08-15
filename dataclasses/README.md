# Dataclasses

Learn dataclasses through deliberate practice.

The goal of this topic is not simply to understand what dataclasses are, but to become comfortable designing structured, maintainable, and reusable data models in real-world Python projects.

By the end of this exercise path, you should be able to:

- Understand how dataclasses work
- Create dataclasses confidently
- Use type annotations with dataclasses
- Handle default values and factories
- Create immutable data models
- Compare and sort dataclass objects
- Model real-world application data
- Recognize common dataclass patterns used in professional Python code

## What Are Dataclasses?

Dataclasses are a feature introduced in Python to simplify the creation of classes whose primary purpose is storing data.

Without dataclasses, developers often write repetitive boilerplate code such as:

- `__init__`
- `__repr__`
- `__eq__`

Dataclasses generate much of this code automatically, making data models easier to write, read, and maintain.

They are commonly used for:

- Configuration objects
- Application settings
- API request and response models
- Domain entities
- Structured application data
- Data transfer objects

### Simple Example

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


person = Person("Alice", 30)

print(person)
```

### Example Output

```text
Person(name='Alice', age=30)
```

The `@dataclass` decorator automatically creates useful methods such as `__init__`, `__repr__`, and `__eq__`, allowing you to focus on modelling data rather than writing boilerplate code.

## Exercise Philosophy

The exercises in this topic are designed to build on each other.

Instead of learning many dataclass concepts at once, every exercise introduces one new idea while reinforcing previous knowledge.

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

## Structure

```text
dataclasses/
│
├── 1-foundations/
├── 2-exploration/
├── 3-manipulation/
├── 4-problem-solving/
├── 5-mini-project/
└── README.md
```

Each stage introduces new concepts and increasingly realistic modelling challenges.

## 1. Foundations

Goal:

Understand the fundamental building blocks of dataclasses.

Topics include:

- Creating dataclasses
- Fields and type annotations
- Constructor generation
- String representations
- Equality comparison
- Default values
- Optional fields
- Basic object modelling

Example exercises:

```text
01 Creating Your First Dataclass
02 Adding Multiple Fields
03 Using Type Annotations
04 Understanding Generated __init__
05 Understanding Generated __repr__
```

## 2. Exploration

Goal:

Explore additional dataclass features and behaviors.

Topics include:

- Default values
- Default factories
- Frozen dataclasses
- Field customization
- Ordering and comparison
- Post-initialization processing
- Nested dataclasses

Example exercises:

```text
11 Default Values
12 Default Factories
13 Frozen Dataclasses
14 Ordering Objects
15 Using __post_init__
```

## 3. Manipulation

Goal:

Use dataclasses to build useful application components.

Topics include:

- Configuration objects
- User models
- Product models
- Data transformation
- Serialization patterns
- Application settings
- Domain modelling

Example exercises:

```text
21 Application Configuration
22 User Profile Model
23 Product Catalog Entry
24 API Response Model
25 Dataclass Utility Toolbox
```

## 4. Problem Solving

Goal:

Apply dataclasses to realistic software design problems.

Topics include:

- Refactoring dictionaries into dataclasses
- Replacing fragile data structures
- Improving code readability
- Enforcing immutability
- Building maintainable application models
- Designing object relationships

Example exercises:

```text
31 Refactoring Dictionary-Based Data
32 Building a Configuration System
33 Immutable Domain Models
34 Modelling Application State
35 Dataclass Design Challenge
```

## 5. Mini Project

Goal:

Combine everything learned throughout the topic.

### Example Project

Application Configuration Framework

Possible features:

```text
Configuration Models
Validation Rules
Nested Configuration Objects
Immutable Settings
Serialization Support
Environment Configuration
```

The project should require knowledge from all previous sections.

## Recommended Workflow

For each exercise:

- Read the challenge.
- Attempt a solution without looking at hints.
- Experiment with variations.
- Refactor your solution.
- Compare with the provided solution.
- Move on only when the concept feels comfortable.

## Mastery Checklist

Before leaving this topic, you should be able to confidently explain:

- What a dataclass is
- Why dataclasses exist
- When to use a dataclass
- How type annotations and dataclasses work together
- How default values and factories differ
- How frozen dataclasses work
- How ordering and comparison are generated
- How `__post_init__` works
- How to model real-world data using dataclasses
- When a regular class is a better choice than a dataclass

If you can complete the mini project without referring to previous exercises, you've likely achieved a solid working understanding of dataclasses.

## Remember

The goal is not to memorize `@dataclass`.

The goal is to reach the point where, when you need to model structured application data, your instinct is:

```text
"This should probably be a dataclass."
```