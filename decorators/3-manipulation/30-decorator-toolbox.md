# Exercise 30 - Decorator Toolbox

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
✅ Retry Decorator
✅ Debug Decorator
✅ Access Counter
✅ Cache Decorator
✅ Permission Decorator
✅ Validation Decorator
✅ Logging Decorator
➡️ Current Manipulation Exercise
```

***

## Goal

Use:

```text
multiple decorators together
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A small decorator toolbox that combines
multiple reusable decorators to solve
real-world problems.
```

***

## Previously Learned

Before starting this exercise you should already understand:

* Timing decorators
* Repeat decorators
* Retry decorators
* Debug decorators
* Access counters
* Cache decorators
* Permission decorators
* Validation decorators
* Logging decorators
* Function arguments
* Flexible wrappers

This exercise builds on everything introduced during the Manipulation stage.

***

## Scenario

Imagine you need to:

```text
Build a function used by a real application.
```

Requirements quickly start to grow:

```text
Track usage

Validate input

Record activity

Measure performance
```

You could place all of this logic inside the function.

Or:

```text
Use multiple decorators.
```

The goal is to solve a practical problem by combining reusable tools.

***

## Challenge

Build a solution that:

1. Combines multiple decorators
2. Keeps business logic simple
3. Separates responsibilities
4. Demonstrates decorator composition

Focus on creating something useful rather than simply demonstrating syntax.

***

## Requirements

Your solution must:

* Use at least three decorators together
* Apply decorators to a practical function
* Preserve the original function behavior
* Demonstrate how decorator order affects execution

Your solution should not:

* Duplicate logic inside the function
* Move decorator responsibilities into the business logic

***

## Starter Code

```python
@decorator_a
@decorator_b
@decorator_c
def process_order(amount):
    print("Processing order")
```

Replace the placeholder decorators with decorators you created in earlier exercises.

***

## Verify Your Solution

Your completed program should be able to:

```text
Validate input

Track function calls

Record activity

Execute the original function
```

Example:

```text
withdraw has been called 1 time(s)

Withdrawing 100
```

Another example:

```text
Validation Failed
Value must be positive
```

Example:

```text
Function call written to log file

Withdrawing 100
```

You should also be able to explain:

* Which decorators were combined
* Why those decorators were chosen
* How decorator order affects behavior

***

## Hints

### Hint 1

You already have several decorators available.

Consider reusing:

```text
count_calls
validate_positive
log_calls
timer
debug
```

***

### Hint 2

Decorators execute in a specific order.

Consider:

```python
@a
@b
def func():
    ...
```

Think about:

```text
Which decorator receives the function first?

Which decorator executes first when
the function is called?
```

***

### Hint 3

Try applying multiple decorators to a function such as:

```python
withdraw()
```

or:

```python
process_order()
```

and observe the output carefully.

***

## Possible Improvements

Once the basic solution works, consider:

* Combining four or more decorators
* Adding timestamps to log entries
* Preserving metadata with `functools.wraps`
* Supporting configurable decorators
* Refactoring decorators into a separate module

These are optional improvements.

***

## Reflection

Answer the following questions.

1. What problem does the decorator toolbox solve?
2. Which decorators work well together?
3. How does decorator order affect execution?
4. What advantages come from separating responsibilities?
5. Which decorator did you find most useful and why?

***

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Create a reusable decorators.py module
containing all decorators from
Exercises 21-29.
```

Or:

```text
Build a function that combines:

Validation
Logging
Timing
Call Counting
```

Example:

```python
@count_calls
@log_calls("app.log")
@validate_positive
@timer
def purchase(amount):
    print(f"Processing purchase: {amount}")
```

Observe how each decorator contributes to the final behavior.

***

## Real-World Connection

This pattern appears in:

* Web applications
* APIs
* Monitoring systems
* Data processing pipelines
* Business applications

Most decorators are not used alone.

Real applications often combine validation, logging, security, monitoring, debugging, and performance tracking around the same function.

Decorator composition allows developers to build complex behavior from small reusable pieces while keeping business logic clean and focused.

***

## Success Criteria

You can consider this exercise complete when:

* [ ] At least three decorators are combined
* [ ] The utility works as required
* [ ] The original function remains simple
* [ ] Decorator responsibilities remain separate
* [ ] You understand decorator execution order
* [ ] You can explain why specific decorators were combined
* [ ] You completed at least one practical use case

***

## Solution

```text
solutions/30-decorator-toolbox.py
```
