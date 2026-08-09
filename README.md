# Python Exercise Gym

A collection of progressive Python exercises designed to build deep understanding through deliberate practice.

The goal of this repository is simple:

> Pick a Python topic. Start with the first exercise. Progressively work through increasingly challenging exercises until you can confidently use the topic in real-world projects.

Unlike many exercise collections, this repository focuses on **depth rather than breadth**.

Instead of jumping between unrelated topics, each topic contains a carefully structured sequence of exercises where every new exercise builds on knowledge gained from previous exercises.

---

## Philosophy

Learning Python is not about reading more documentation.

Learning Python is about **using the same concept repeatedly in increasingly challenging situations until it feels natural**.

For example:

```text
decorators
├── Exercise 01
├── Exercise 02 (requires Exercise 01)
├── Exercise 03 (requires Exercise 01-02)
├── Exercise 04 (requires Exercise 01-03)
└── ...
```

Knowledge accumulates.

Nothing is thrown away.

The objective is to move from:

```text
"I understand the concept."
```

to:

```text
"I can use the concept without thinking."
```

---

## Repository Structure

Each top-level directory represents a specific Python topic.

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

If you want to practice decorators, go directly to:

```text
decorators/
```

If you want to practice pathlib, go directly to:

```text
pathlib/
```

The repository is designed to minimise decision fatigue and maximize practice time.

---

## Topic Structure

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

### 1. Foundations

Learn the basic syntax and core ideas.

Example questions:

- What is this feature?
- How does it work?
- What is the simplest possible example?

---

### 2. Exploration

Explore variations and different use cases.

Example questions:

- What else can it do?
- What happens if I change the input?
- What patterns are commonly used?

---

### 3. Manipulation

Use the topic to solve small practical problems.

Example goals:

- Build helper functions
- Create reusable utilities
- Apply the concept in realistic scenarios

---

### 4. Problem Solving

Use the topic to solve increasingly challenging exercises.

Example goals:

- Handle edge cases
- Combine multiple techniques
- Build confidence through repetition

---

### 5. Mini Project

Bring everything together in a larger exercise.

The mini project acts as proof that you've mastered the material covered within the topic.

---

## Exercise Design

Exercises are intentionally progressive.

For example:

```text
01 → Learn a basic concept
02 → Reuse 01 and introduce something new
03 → Reuse 01-02 and introduce something new
04 → Reuse 01-03 and introduce something new
```

Each exercise should feel like a natural next step rather than a completely new challenge.

---

## Recommended Workflow

When working through a topic:

1. Start at Exercise 01.
2. Complete exercises in order.
3. Avoid looking at solutions immediately.
4. Experiment with your own variations.
5. Complete the mini project.
6. Use the topic in one of your own projects.

The goal is not to finish exercises quickly.

The goal is to build intuition through practice.

---

## Topics

Current topics include:

- pathlib
- shutil
- exceptions
- logging
- dataclasses
- typing
- decorators
- generators
- iterators
- context managers
- testing
- sqlite
- packaging
- concurrency
- async

Additional topics may be added over time.

---

## Who Is This For?

This repository is intended for Python developers who already know the basics and want to strengthen their understanding of Python's standard library and more advanced language features through focused, deliberate practice.

---

## Remember

Reading creates familiarity.

Practice creates skill.

This repository exists to help turn Python concepts into Python instincts.