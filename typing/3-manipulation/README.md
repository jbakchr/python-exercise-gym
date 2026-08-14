## Manipulation

### Overview

The goal of the Manipulation stage is to start using Python's typing system to build practical and reusable tools.

In the previous stages, you learned:

- Basic type annotations
- Optional and Union types
- Collection annotations
- Type aliases
- TypedDict
- Literal
- Callable
- Any
- NewType
- NamedTuple
- Type narrowing
- Self
- Advanced annotation patterns

Now it is time to apply that knowledge.

Instead of focusing on what typing features are, this stage focuses on using them to model real-world data and improve code quality.

Many of the exercises mirror situations commonly found in production applications, including configuration management, API integrations, data processing, service design, and reusable utility development.

### Learning Goals

By the end of this stage you should be able to:

- Design typed data structures for real applications
- Build reusable type-safe utilities
- Model application configuration with types
- Create typed interfaces between components
- Use generics to build flexible tools
- Process and transform typed data safely
- Improve maintainability through strong typing
- Apply typing to common software development scenarios

### What You Will Practice

Topics covered in this stage:

- Typed configuration data
- Environment settings
- API response modelling
- Generic containers
- Validation helpers
- Reusable type utilities
- Typed data processing
- Service interfaces
- Data transformation pipelines
- Building a typing utility toolbox

### Recommended Approach

For every exercise:

- Read the challenge carefully.
- Attempt a solution without looking at hints.
- Experiment with your own variations.
- Refactor and improve your solution.
- Compare against the provided solution.
- Reflect on what you learned.
- Move on only when the concept feels comfortable.

Remember:

Working code is the starting point.

Understanding why the types improve the design is the goal.

### Exercises

#### 21 Typed Configuration Data

Create a typed configuration structure for an application using TypedDict, Literal, Optional values, and type aliases.

#### 22 Typed Environment Settings

Build a system for representing application environments such as development, testing, and production using strong type definitions.

#### 23 Typed API Responses

Create type-safe models for API response data and build functions that process those responses.

#### 24 Generic Container

Build a reusable container that can safely store and return values of different types using generics.

#### 25 Validation Helper

Create utility functions that validate incoming data while preserving type information.

#### 26 Type Utility Functions

Build a collection of reusable helper functions that work with typed data structures.

#### 27 Typed Data Processor

Create a small data-processing utility that transforms typed input into typed output.

#### 28 Service Interface Design

Define typed interfaces for application services and implement simple examples.

#### 29 Data Transformation Pipeline

Build a type-safe pipeline that accepts, transforms, and returns structured data.

#### 30 Build a Typing Toolbox

Create a reusable collection of utilities for:

- Configuration management
- Validation
- Data transformation
- Generic containers
- Service interfaces

This exercise acts as the capstone for the Manipulation stage.

### Success Criteria

You are ready to continue to the next stage when:

- All exercises are complete
- You understand why the chosen types improve code quality
- You can model structured data confidently
- You can design reusable typed utilities
- You can use generics without relying heavily on documentation
- You can create type-safe interfaces between components
- You can recognize opportunities to improve code with typing

### What Comes Next?

After completing this stage, move on to:

4-problem-solving

In the next stage you will apply typing to realistic software engineering problems.

The focus will shift from:

Building typed utilities

to:

Solving real-world development challenges with type-safe designs.

Examples may include:

- Application architecture
- Data validation workflows
- Service integrations
- Configuration systems
- Plugin systems
- Processing pipelines
- Complex domain modelling

### Remember

Typing is not about satisfying a type checker.

Typing is about making code easier to understand, safer to change, and more reliable to maintain.

Good type annotations communicate intent.

Great type annotations make complex code feel simple.