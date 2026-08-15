# PROJECT_CONTEXT.md

## python-exercise-gym – Project Context

### 🧠 What This Project Is

python-exercise-gym is a repository for learning Python through deliberate practice.

The goal is not to teach Python through tutorials.

The goal is to build mastery through repetition, application, and progressively designed exercises.

Learners should be able to:

```text
Choose a topic
↓
Start at Exercise 01
↓
Progress through a skill ladder
↓
Develop intuition
↓
Reach mastery
```

Example topics:

```text
typing
decorators
dataclasses
pathlib
logging
exceptions
sqlite
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

The project is built around one principle:

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
Understand concepts
```

### python-mastery-path

Purpose:

```text
Know what to learn next
```

### python-exercise-gym

Purpose:

```text
Practice until mastery
```

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

Question:

```text
What is this?
```

Focus:

- Core concepts
- Syntax
- Building blocks

---

### Exploration

Goal:

```text
Investigate
```

Question:

```text
What else can it do?
```

Focus:

- Variations
- Behaviors
- Common patterns

---

### Manipulation

Goal:

```text
Build
```

Question:

```text
How can I use it?
```

Focus:

- Utilities
- Reusable tools
- Practical usage

---

### Problem Solving

Goal:

```text
Apply
```

Question:

```text
How do I solve problems with it?
```

Focus:

- Realistic scenarios
- Design decisions
- Refactoring
- Trade-offs

---

### Mini Project

Goal:

```text
Create
```

Question:

```text
Can I build something useful?
```

Focus:

- Integration
- End-to-end usage
- Proof of understanding

---

## 📝 Repository Templates

### Topic README

```text
templates/topic-readme-template.md
```

### Stage READMEs

```text
templates/stage-readme-template.md
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
templates/exercise-solution-template.py
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

- Solve only exercise requirements
- Exclude stretch goals
- Exclude experiments
- Prioritize clarity
- Prefer readability over cleverness

---

## 🧩 Exercise Philosophy

Every exercise builds upon previous exercises.

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

Exercises should feel like:

```text
A Skill Ladder
```

not:

```text
A Checklist
```

Knowledge must accumulate.

Nothing should feel disconnected.

---

## ✅ Current Progress

### Decorators ✅

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

Decorators is the first complete reference implementation.

---

### Typing ✅

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

Typing is the second complete reference implementation.

---

### Dataclasses 🚧

Status:

```text
✅ Foundations Complete
⬜ Exploration
⬜ Manipulation
⬜ Problem Solving
⬜ Mini Project
```

Progress:

```text
10 / 41 Learning Units Complete
```

---

## ✅ Dataclasses Foundations Complete

Exercises:

```text
01. Creating Your First Dataclass
02. Adding Multiple Fields
03. Using Type Annotations
04. Creating Dataclass Objects
05. Accessing Attributes
06. Understanding Generated __init__
07. Understanding Generated __repr__
08. Comparing Dataclass Objects
09. Using Default Values
10. Building a Simple Data Model
```

Skills Practiced:

```text
Dataclass Creation
Multiple Fields
Type Annotations
Object Creation
Attribute Access
Generated __init__
Generated __repr__
Generated Equality
Default Values
Basic Data Modelling
```

Outcome:

```text
Learned how dataclasses reduce
boilerplate code and help model
structured application data.

Built familiarity with the core
features automatically generated
by the @dataclass decorator.
```

---

# 🎯 Current Focus

## ACTIVE

Topic:

```text
dataclasses
```

Current Stage:

```text
2-exploration
```

Next Exercise:

```text
11. Default Values Revisited
```

Reason:

```text
The Foundations stage is complete.

The next step is to explore more
advanced dataclass features such as
default factories, immutability,
ordering, nested dataclasses,
field customization, and
post-initialization processing.
```

---

# 📋 Current Topic

## Dataclasses

Status:

```text
✅ Foundations
⬜ Exploration
⬜ Manipulation
⬜ Problem Solving
⬜ Mini Project
```

Progress:

```text
10 / 41 Learning Units Complete
```

Planned Remaining Structure:

```text
10 Exploration Exercises
10 Manipulation Exercises
10 Problem Solving Exercises
1 Mini Project
```

Dataclasses is becoming the reference topic for:

```text
Structured Data Modelling
Object Design
Defaults
Factories
Immutability
Comparison
Ordering
Nested Models
Application Models
```

---

# 🔮 Future Topics

Recommended order:

```text
dataclasses

pathlib
exceptions
logging
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
Dataclasses extends many of the
concepts introduced in Typing and
provides a bridge toward modelling
real application data.

Many future topics become easier
and more realistic when learners
can create proper application models.
```

---

## 💡 Important Rule

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

Every exercise, solution, stage, and project should reinforce that objective.

---

## 🚀 What To Work On Next

Current recommendation:

```text
dataclasses
↓
2-exploration
↓
Exercise 11
```

Start with:

```text
11. Default Values Revisited
```

When continuing this project in a future chat:

- Assume Decorators is complete.
- Assume Typing is complete.
- Assume Dataclasses Foundations is complete.
- Assume Dataclasses Topic README exists.
- Assume Dataclasses Foundations README exists.
- Assume Exercises 01-10 and solutions exist.
- Use Decorators and Typing as reference implementations.
- Continue developing Dataclasses Exploration.
- Maintain existing exercise templates and solution templates.
- Keep exercises progressive and practical.
- Continue following the deliberate-practice philosophy of the repository.

```text
Learn
↓
Explore
↓
Build
↓
Apply
↓
Create
```

Every topic should reinforce that progression.