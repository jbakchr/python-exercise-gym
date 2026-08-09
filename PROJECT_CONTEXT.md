# PROJECT_CONTEXT.md

## python-exercise-gym – Project Context

### 🧠 What This Project Is

python-exercise-gym is a GitHub repository dedicated to learning Python through deliberate practice.

The goal is NOT to be:

- Another Python tutorial
- Another documentation site
- Another roadmap
- A collection of random coding challenges

The goal is:

👉 Provide structured, progressive exercises that help learners deeply understand specific Python topics.

The repository is designed so a learner can choose a topic and immediately begin working through exercises that become progressively more challenging.

For example:

```text
decorators/
pathlib/
shutil/
generators/
```

A learner should be able to think:

```text
Today I want to practice decorators.
```

and immediately know where to start.

---

## 🎯 Core Philosophy

The project is built around one idea:

```text
Reading creates familiarity.
Practice creates skill.
Repetition creates mastery.
```

Learning does not happen by reading documentation alone.

Learning happens through:

```text
Concept
↓
Exercise
↓
Exercise
↓
Exercise
↓
Application
↓
Mastery
```

Each topic should encourage deep practice rather than broad exposure.

---

## 🧭 Repository Philosophy

The repository complements two existing projects:

### easier-python-docs

Purpose:

```text
Understand concepts.
```

---

### python-mastery-path

Purpose:

```text
Know what to learn next.
```

---

### python-exercise-gym

Purpose:

```text
Practice until mastery.
```

Each repository has a distinct role.

---

## 🏗 Repository Structure

Topics are organized by Python concept.

Examples:

```text
python-exercise-gym/
│
├── pathlib/
├── shutil/
├── exceptions/
├── logging/
├── dataclasses/
├── typing/
├── decorators/
├── generators/
├── iterators/
├── context-managers/
├── testing/
├── sqlite/
├── packaging/
├── concurrency/
└── async/
```

The primary design principle is:

```text
One topic
↓
Progressive exercises
↓
Mastery
```

---

## 📚 Topic Structure

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

This structure should be reused for all topics.

---

## 📖 Learning Stages

### 1. Foundations

Goal:

```text
Understand the building blocks.
```

Examples:

- Syntax
- Core concepts
- Basic usage

---

### 2. Exploration

Goal:

```text
Explore variations and behaviors.
```

Examples:

- Different inputs
- Different patterns
- Common use cases

---

### 3. Manipulation

Goal:

```text
Use the concept to solve practical problems.
```

Examples:

- Utilities
- Helpers
- Small tools

---

### 4. Problem Solving

Goal:

```text
Apply the concept to realistic scenarios.
```

Examples:

- Edge cases
- Production-style problems
- More complex exercises

---

### 5. Mini Project

Goal:

```text
Combine everything learned.
```

The mini project acts as proof of understanding.

---

## 📝 Documentation Templates

The repository currently uses reusable templates.

### Topic Template

```text
templates/topic-readme-template.md
```

Used for:

```text
decorators/README.md
pathlib/README.md
generators/README.md
...
```

---

### Stage Template

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

---

### Exercise Template

```text
templates/exercise-template.md
```

Used for all exercises.

---

### Mini Project Template

```text
templates/mini-project-template.md
```

Used for final projects within each topic.

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

The learner should feel like they are climbing a skill ladder.

---

## 🎮 Desired Learning Experience

Exercises should feel more like:

```text
A skill tree
```

than:

```text
A checklist
```

Every exercise should answer:

```text
What new thing am I learning?

Why does it matter?

How does it build on previous exercises?
```

---

## ✅ Current Topic Progress

### Decorators

Status:

```text
1-foundations complete
```

Completed exercises:

```text
01 Functions Are Objects
02 Pass Function as Argument
03 Return a Function
04 Create Your First Wrapper
05 Wrap a Function
06 Before Execution
07 Before and After Execution
08 Understanding @ Syntax
09 Multiple Decorated Functions
10 Build a Simple Announcer
```

Each exercise includes:

- Exercise markdown
- Python solution file

Structure:

```text
1-foundations/
├── solutions/
├── 01-*.md
├── 02-*.md
...
└── 10-*.md
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
41 learning units per topic
```

This provides enough repetition for genuine mastery.

---

## 🚫 Non-Goals

This repository is NOT:

- LeetCode
- Advent of Code
- Competitive programming
- Interview preparation
- Documentation
- A Python encyclopedia

The focus is:

```text
Deep understanding
through
deliberate practice
```

---

## 💡 Important Design Decisions

When creating exercises:

Prefer:

- Small exercises
- One new concept at a time
- Progressive difficulty
- Practical examples
- Reflection questions
- Stretch goals

Avoid:

- Massive jumps in difficulty
- Multi-topic exercises too early
- Teaching five concepts at once
- Premature complexity

---

## 🚀 What I Want Help With In A New Chat

Help me:

- Design new topic structures
- Create progression paths
- Design exercises
- Create solution files
- Review exercise quality
- Improve learning flow
- Expand topics consistently
- Maintain consistency across the repository

Avoid:

- Overengineering
- Turning exercises into tutorials
- Unnecessary abstractions
- Huge projects before concepts are learned

---

## 🔑 Most Important Rule

Always optimize for learning.

When creating exercises:

```text
Simple
↓
Progressive
↓
Practical
↓
Reusable
```

The goal is not to complete exercises.

The goal is to build intuition.

A learner should eventually reach the point where a concept feels natural and can be applied without needing to look it up.