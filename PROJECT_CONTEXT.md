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
pathlib/
typing/
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
⬜ Problem Solving
⬜ Mini Project
```

Progress:

```text
30 / 50 Exercises Complete
```

---

### Foundations Completed

Exercises:

```text
01-10
```

Topics:

```text
Functions Are Objects
Pass Function as Argument
Return a Function
Create Your First Wrapper
Wrap a Function
Before Execution
Before and After Execution
Understanding @ Syntax
Multiple Decorated Functions
Build a Simple Announcer
```

Completed:

- Foundations README
- Exercise files
- Solution files

---

### Exploration Completed

Exercises:

```text
11-20
```

Topics:

```text
Functions With Arguments
Multiple Arguments
Keyword Arguments
Flexible Wrappers
Return Values
Reusable Decorators
Function Metadata
Preserving Metadata
Stacking Decorators
Build a Call Logger
```

Completed:

- Exploration README
- Exercise files
- Solution files

---

### Manipulation Completed

Exercises:

```text
21-30
```

Utilities Built:

```text
21. Timing Decorator
22. Repeat Decorator
23. Retry Decorator
24. Debug Decorator
25. Access Counter
26. Cache Decorator
27. Permission Decorator
28. Validation Decorator
29. Logging Decorator
30. Decorator Toolbox
```

Concepts Practiced:

```text
Decorator Factories
Flexible Wrappers
State Management
Caching
Validation
Access Control
Logging
Timing
Composition
Reusable Utilities
```

Completed:

- Manipulation README
- Exercise files
- Solution files

---

## 🎯 Current Focus

### Decorators

#### Problem Solving

Status:

```text
NEXT
```

Goal:

```text
Move from building decorators
to solving realistic problems
with decorators.
```

Target:

```text
Exercises 31-40
```

Focus:

```text
Scenario First

Problem First

Decorator Choice Second
```

The learner should increasingly answer:

```text
What problem am I solving?
```

before asking:

```text
Which decorator should I build?
```

---

## 📋 Planned Problem Solving Exercises

Proposed exercises:

```text
31. Slow API Calls
32. Rate Limiting
33. Expensive Calculations
34. Audit Trail System
35. Production Debugging
36. Function Monitoring
37. Data Validation Pipeline
38. Secure Operations
39. Background Task Tracking
40. Decorator Design Challenge
```

Goal:

```text
Use existing decorator knowledge
to solve realistic problems.
```

---

## 🚀 Planned Mini Project

Status:

```text
Future
```

Possible project ideas:

```text
Task Runner

Decorator Utility Library

Monitoring Toolkit

Audit System

Tiny Web Framework
```

Goal:

```text
Combine everything learned
throughout the decorators topic.
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
pathlib
exceptions
logging
dataclasses
typing
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
Strengthen everyday Python skills
before moving into more advanced
execution models and architectures.
```

---

## 🚀 What To Work On Next

Current focus:

```text
Decorators
↓
4-problem-solving
↓
Exercises 31-40
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