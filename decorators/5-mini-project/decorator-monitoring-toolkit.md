# Mini Project - Decorator Monitoring Toolkit

### Topic

Decorators

### Project Overview

In this mini project, you will build:

```text
Decorator Monitoring Toolkit
```

A reusable toolkit containing decorators that solve common application concerns.

Your toolkit should help developers:

- Monitor function execution
- Measure performance
- Validate inputs
- Restrict access
- Track usage
- Optimize expensive operations

The toolkit should be designed so these concerns can be added to existing functions without changing the underlying business logic.

This project combines concepts from the entire decorators topic and serves as proof of understanding.

---

### Learning Goals

By completing this project you will practice:

- Creating reusable decorators
- Building decorator factories
- Working with function arguments
- Working with return values
- Preserving function behavior
- Managing decorator state
- Combining multiple decorators
- Designing reusable utilities
- Choosing appropriate decorator solutions
- Structuring a small decorator library

You should rely primarily on techniques learned throughout this topic.

---

### Background

A development team is building an internal business application.

As the system grows, the team encounters common software engineering concerns:

```text
Monitoring

Validation

Authorization

Performance

Debugging

Usage Tracking
```

Initially, developers add these features directly inside individual functions.

Soon the codebase begins to suffer from:

```text
Duplicated code

Inconsistent behavior

Maintenance difficulties
```

The team decides to create a reusable decorator toolkit that can be applied consistently throughout the application.

Your task is to build that toolkit.

---

### Project Requirements

Your project must:

- Create at least five reusable decorators
- Include at least one decorator factory
- Include at least one stateful decorator
- Demonstrate decorator composition
- Preserve original function behavior
- Work across multiple example functions
- Clearly separate business logic from supporting concerns

Your project should:

- Be easy to extend
- Be easy to understand
- Minimize duplication
- Follow consistent naming patterns

Your project must not:

- Hardcode solutions for individual functions
- Duplicate logic across decorators
- Mix monitoring concerns with business logic

---

### Required Features

Your toolkit must include solutions for several of the following concerns:

```text
Timing

Logging

Validation

Caching

Usage Tracking

Authorization

Debugging

Auditing
```

You may implement additional decorators if desired.

---

### Demonstration Application

Create several functions representing features of a small application.

Examples:

```python
create_user()

generate_report()

export_data()

delete_user()

calculate_statistics()
```

Use your decorators to improve these functions.

Different functions should require different combinations of decorators.

---

### Example Usage

The completed project should support behavior similar to:

```python
create_user("Alice")

create_user("")

generate_report("customer-123")

generate_report("customer-123")

delete_user("admin")

delete_user("guest")

export_data()
export_data()
```

This demonstrates the intended outcome.

Do not treat these examples as implementation requirements.

---

### Expected Behaviour

When the project is working correctly:

```text
Validation occurs automatically.

Unauthorized users are blocked.

Execution times can be displayed.

Expensive calculations can be cached.

Function usage can be tracked.

Monitoring information is displayed automatically.

Functions continue behaving normally.

Multiple decorators work together.
```

Users of the toolkit should be able to add functionality to existing functions with minimal effort.

---

### Suggested Milestones

Break the project into manageable pieces.

#### Milestone 1

Build the core decorators.

Examples:

```text
Logging

Timing

Validation
```

---

#### Milestone 2

Build stateful decorators.

Examples:

```text
Caching

Usage Tracking
```

---

#### Milestone 3

Build configurable decorators.

Examples:

```text
Permission Checks

Rate Limiting
```

---

#### Milestone 4

Create a demonstration application.

Apply your decorators to several example functions.

Show realistic usage.

---

#### Milestone 5

Refactor the toolkit.

Improve:

- Naming
- Organization
- Readability
- Reusability

These milestones are suggestions, not requirements.

---

### Design Considerations

Before writing code, think about:

- Which decorators belong in the toolkit?
- Which decorators should be configurable?
- Which decorators need state?
- Which decorators can be combined?
- What information should be displayed?
- How should usage data be stored?
- How can the toolkit remain simple while remaining useful?

There is rarely a single correct solution.

---

### Testing Your Project

Verify that:

- Logging works correctly
- Timing works correctly
- Validation prevents invalid input
- Authorization prevents unauthorized access
- Caching avoids repeated work
- Usage tracking records activity
- Decorators preserve return values
- Multiple decorators can be stacked
- Different decorators work together

Create your own additional tests wherever appropriate.

---

### Optional Extensions

Once the core project is complete, consider adding:

- Retry support
- Audit logging
- Cache statistics
- File-based logging
- Configurable monitoring levels
- Error tracking
- Request throttling
- Shared monitoring dashboard
- Decorator registry

These should enhance the project rather than replace it.

---

### Reflection

After completing the project, answer the following questions.

- Which concepts from this topic were most useful?
- Which decorator was most difficult to design?
- Which decorators worked well together?
- Did decorator order matter?
- What trade-offs did you make?
- How would you improve the toolkit?
- Which decorators would you use in your own projects?
- Do you feel comfortable designing decorators independently?

---

### Real-World Connection

Projects like this appear in:

- Real applications
- Internal tools
- Automation scripts
- Open source projects
- Web frameworks
- Monitoring platforms

Many professional Python projects use decorators extensively.

Examples include:

```text
FastAPI

Flask

Click

Pytest

Django
```

Decorators are commonly used for:

```text
Authentication

Authorization

Routing

Caching

Logging

Monitoring

Validation
```

This project simulates the process of creating reusable infrastructure that can be applied throughout an application.

---

### Success Criteria

You can consider this mini project complete when:

- [ ] At least five reusable decorators are implemented
- [ ] At least one decorator factory is implemented
- [ ] At least one stateful decorator is implemented
- [ ] Multiple decorators can be composed together
- [ ] The project behaves as expected
- [ ] Business logic remains separate from supporting concerns
- [ ] The code is understandable and maintainable
- [ ] You can explain your design decisions
- [ ] You can extend the toolkit without major rewrites
- [ ] You feel confident using decorators independently

---

### Example Solution

See:

```text
solutions/decorator-monitoring-toolkit.py
```

Study the solution only after attempting the project yourself.
``