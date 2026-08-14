# PROJECT_CONTEXT.md

## python-exercise-gym – Project Context

### 🧠 What This Project Is

python-exercise-gym is a repository for learning Python through deliberate practice.

The goal is not to teach Python through tutorials.

The goal is to build mastery through repetition and progressive exercises.

Learners should be able to choose a topic, start with Exercise 01, and progress through a carefully designed skill ladder.

Example:

```text
decorators/
typing/
pathlib/
logging/
sqlite/
```

The focus is:

```text
Practice
↓
Repetition
↓
Application
↓
Mastery
```

---

## 🎯 Core Philosophy

The project is built around one idea:

```text
Reading creates familiarity.
Practice creates skill.
Repetition creates mastery.
```

This repository exists to help learners move from:

```text
"I understand the concept."
```

to:

```text
"I can use the concept naturally."
```

---

## 🧭 Repository Philosophy

This repository complements two related projects.

### easier-python-docs

Purpose:

```text
Understand concepts.
```

### python-mastery-path

Purpose:

```text
Know what to learn next.
```

### python-exercise-gym

Purpose:

```text
Practice until mastery.
```

Each project serves a different learning need.

---

## 🏗 Repository Structure

Every topic follows the same structure:

```text
topic/
│
├── 1-foundations/
├── 2-exploration/
├── 3-manipulation/
├── 4-problem-solving/
├── 5-mini-project/
└── README.md
```

---

## 📖 Learning Stages

### Foundations

Goal:

```text
Learn
```

Focus:

- Core concepts
- Basic syntax
- Building blocks

Question:

```text
What is this?
```

---

### Exploration

Goal:

```text
Investigate
```

Focus:

- Variations
- Behaviors
- Common patterns

Question:

```text
What else can it do?
```

---

### Manipulation

Goal:

```text
Build
```

Focus:

- Small utilities
- Practical usage
- Reusable tools

Question:

```text
How can I use it?
```

---

### Problem Solving

Goal:

```text
Apply
```

Focus:

- Realistic scenarios
- Design decisions
- Edge cases

Question:

```text
How do I solve problems with it?
```

---

### Mini Project

Goal:

```text
Create
```

Focus:

- Combining concepts
- End-to-end usage
- Proof of understanding

Question:

```text
Can I build something with it?
```

---

## 📝 Repository Templates

### Topic Templates

```text
templates/topic-readme-template.md
```

### Stage Templates

```text
templates/stage-readme-template.md
```

Used for:

```text
1-foundations/README.md
2-exploration/README.md
3-manipulation/README.md
4-problem-solving/README.md
5-mini-project/README.md
```

### Exercise Templates

```text
templates/exercise-foundations-template.md
templates/exercise-exploration-template.md
templates/exercise-manipulation-template.md
templates/exercise-problem-solving-template.md
```

### Mini Project Template

```text
templates/mini-project-template.md
```

### Solution Template

```text
templates/solution-template.py
```

Rule:

```text
Exercise File
=
Learning Experience

Solution File
=
Minimal Correct Implementation
```

Solutions should:

- Solve only the exercise requirements
- Exclude experiments
- Exclude stretch goals
- Prefer simple solutions
- Prioritize readability over cleverness

---

## 🧩 Exercise Philosophy

Every exercise should build upon previous exercises.

Pattern:

```text
01
↓
02 requires 01
↓
03 requires 01-02
↓
04 requires 01-03
↓
...
```

Knowledge should accumulate.

Nothing should feel disconnected.

Exercises should feel like:

```text
A Skill Ladder
```

not:

```text
A Checklist
```

---

## ✅ Current Progress

### Decorators

Status:

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Manipulation Complete
✅ Problem Solving Complete
✅ Mini Project Complete
✅ Topic Complete
```

Progress:

```text
41 / 41 Learning Units Complete
```

---

### Typing

Status:

```text
✅ Foundations Complete
✅ Exploration Complete
⬜ Manipulation Not Started
⬜ Problem Solving Not Started
⬜ Mini Project Not Started
🚧 Topic In Progress
```

Progress:

```text
20 / 41 Learning Units Complete
```

---

## ✅ Typing Foundations Completed

Exercises:

```text
01-10
```

Topics Covered:

```text
01. Basic Parameter Types
02. Return Types
03. Multiple Parameters
04. Optional Values
05. Union Types
06. Lists and Collections
07. Dictionaries and Nested Structures
08. Type Aliases
09. Annotating Real Functions
10. Build a Typed Utility
```

Skills Practiced:

```text
Parameter Annotations
Return Annotations
Optional Values
Union Types
Collection Types
Dictionary Types
Nested Structures
Type Aliases
Typed Function Signatures
Typed Utility Design
```

Core Concepts Introduced:

```text
str
int
float
bool

Optional

Union

list
set
tuple

dict

Type Aliases
```

Outcome:

```text
Built a practical foundation
for understanding and using
Python type annotations in
real-world code.
```

---

## ✅ Typing Exploration Completed

Exercises:

```text
11-20
```

Topics Covered:

```text
11. TypedDict
12. Literal
13. Callable
14. Any
15. NewType
16. NamedTuple
17. Type Inference
18. Type Narrowing
19. Self
20. Advanced Annotation Patterns
```

Skills Practiced:

```text
Structured Data Modelling
Restricted Values
Callable Signatures
Flexible Typing
Domain-Specific Types
Immutable Data Models
Type Inference
Type Narrowing
Class-Aware Annotations
Annotation Composition
```

Core Concepts Introduced:

```text
TypedDict
Literal
Callable
Any
NewType
NamedTuple

Type Inference
Type Narrowing

Self

Advanced Annotation Patterns
```

Outcome:

```text
Moved beyond basic type
annotations and learned how
typing can be used to model
data, behaviour, constraints,
and application design.
```

---

## 🏆 Reference Topics

### Decorators

Decorators remains the complete reference implementation.

The topic demonstrates:

```text
Topic README

Stage READMEs

40 Progressive Exercises

1 Mini Project

Exercise Files

Solution Files

Reflection Questions

Stretch Goals

Problem Solving Scenarios

Capstone Project
```

Future topics should continue following this standard.

---

### Typing

Typing now serves as the reference implementation for:

```text
Foundations

Exploration
```

The topic demonstrates how a learner can progress from:

```text
Basic Type Annotations
```

to:

```text
Real-World Type Modelling
```

through deliberate practice.

Typing Exploration is now considered complete.

---

## 🎯 Current Focus

### Active Topic

Status:

```text
ACTIVE
```

Topic:

```text
typing
```

Current Stage:

```text
3-manipulation
```

Reason:

```text
The Foundations stage introduced
the core typing building blocks.

The Exploration stage introduced
the major typing constructs used
in professional Python projects.

The next step is applying those
concepts to build practical and
reusable type-safe utilities.
```

---

## 📋 Planned Typing Manipulation Topics

Exercises:

```text
21-30
```

Planned Concepts:

```text
Typed Configuration Data

Typed Environment Settings

Typed API Responses

Generic Containers

Validation Helpers

Reusable Type Utilities

Typed Data Processing

Typed Service Interfaces

Data Transformation Pipelines

Typing Utility Toolbox
```

Goal:

```text
Move from understanding typing
concepts to building practical
reusable tools with them.
```

---

## 🎯 Long-Term Goal

Every topic should eventually contain:

```text
10 Foundations Exercises
10 Exploration Exercises
10 Manipulation Exercises
10 Problem Solving Exercises
1 Mini Project
```

Total:

```text
41 Learning Units Per Topic
```

---

## 🚫 Non-Goals

This repository is not:

- LeetCode
- Advent of Code
- Interview preparation
- Documentation
- A Python encyclopedia

The focus remains:

```text
Deep Understanding
through
Deliberate Practice
```

---

## 💡 Important Design Rules

Prefer:

- One new idea at a time
- Progressive difficulty
- Small exercises
- Practical examples
- Reflection questions
- Stretch goals

Avoid:

- Massive difficulty jumps
- Teaching multiple concepts simultaneously
- Premature abstraction
- Overengineering
- Huge projects too early

---

## 🔮 Future Topics

Recommended order:

```text
typing
pathlib
exceptions
logging
dataclasses
shutil

generators
iterators
context-managers

testing
sqlite
packaging

concurrency
async
```

Reason:

```text
Typing acts as a force multiplier.

The concepts learned in the
typing topic can be reused and
reinforced throughout almost
every future topic in the
curriculum.
```

---

## 🚀 What To Work On Next

Current focus:

```text
typing
↓
3-manipulation
↓
Exercise 21
```

Recommended starting exercise:

```text
21. Typed Configuration Data
```

Reason:

```text
Typed Configuration Data
naturally combines:

- TypedDict
- Literal
- Optional
- Type Aliases
- Advanced Annotation Patterns

introduced throughout
Foundations and Exploration.
```

When returning to this project, start there.

---

## 🔑 Most Important Rule

Always optimize for learning.

```text
Simple
↓
Progressive
↓
Practical
↓
Reusable
```

The goal is not exercise completion.

The goal is intuition.

A learner should eventually reach the point where the concept feels natural and no longer requires looking things up.

Every exercise, solution, stage, and project should support that outcome.