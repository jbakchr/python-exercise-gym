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
⬜ Exploration Not Started
⬜ Manipulation Not Started
⬜ Problem Solving Not Started
⬜ Mini Project Not Started
🚧 Topic In Progress
```

Progress:

```text
10 / 41 Learning Units Complete
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

## 🏆 Reference Topic

Decorators currently serve as the reference implementation for future topics.

The decorators topic demonstrates:

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

Future topics should follow this structure and level of quality.

Typing Foundations now serves as the reference implementation for introducing typing concepts through deliberate practice.

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
2-exploration
```

Reason:

```text
The Foundations stage is complete.

The next step is to explore
more advanced typing constructs
commonly used in professional
Python projects while continuing
the skill-ladder approach.
```

---

## 📋 Planned Typing Exploration Topics

Exercises:

```text
11-20
```

Planned Concepts:

```text
TypedDict
Literal
Callable
Any
NewType
Type Inference
Type Narrowing
NamedTuple
Self
Advanced Annotation Patterns
```

Goal:

```text
Move beyond basic annotations
and begin modeling data and
behavior more effectively.
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
2-exploration
↓
Exercise 11
```

Recommended starting exercise:

```text
11. TypedDict
```

Reason:

```text
TypedDict builds naturally on:

- Dictionary Types
- Nested Structures
- Type Aliases

introduced during Foundations.
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