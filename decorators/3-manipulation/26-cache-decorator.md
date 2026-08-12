# Exercise 26 - Cache Decorator

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Timing Decorator
✅ Repeat Decorator
✅ Retry Decorator
✅ Debug Decorator
✅ Access Counter
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and stored state
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable cache decorator that stores
previously calculated results and reuses
them when possible.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Flexible wrappers
- Return values
- State management
- Closures
- Function arguments
- Positional arguments
- Keyword arguments

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Avoid performing the same expensive
calculation over and over again.
```

Example:

```text
A function calculates the 35th Fibonacci number.

The calculation is slow.

If the same value is requested again,
you want to reuse the previous result
instead of recalculating it.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Stores previously calculated results
2. Reuses stored results when possible
3. Avoids unnecessary work
4. Returns the original result unchanged

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `cache`
- Store results from previous function calls
- Return cached results when the same inputs are used
- Work with function arguments
- Return the original result unchanged

Your solution should not:

- Recalculate values that already exist in the cache
- Store cached values in global variables

---

## Starter Code

```python
def cache(func):
    pass


@cache
def square(number):
    print("Calculating...")
    return number * number


print(square(5))
print(square(5))
print(square(5))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Calculate a result once and reuse it
for future calls with the same inputs.
```

Example:

```text
Calculating...
25

Using cached result
25

Using cached result
25
```

Another example:

```python
print(square(10))
print(square(10))
```

Output:

```text
Calculating...
100

Using cached result
100
```

You should also be able to explain:

- Where cached values are stored
- How the decorator determines whether a result already exists
- Why caching can improve performance

---

## Hints

### Hint 1

The Access Counter exercise stored a single value:

```python
count = 0
```

This exercise may need to store multiple values.

---

### Hint 2

A dictionary can associate inputs with results.

Example:

```python
{
    5: 25,
    10: 100
}
```

---

### Hint 3

Before executing the function, check whether the input already exists in the cache.

If it does:

```text
Use the stored result.
```

Otherwise:

```text
Run the function and save the result.
```

---

## Possible Improvements

Once the basic solution works, consider:

- Supporting multiple arguments
- Supporting keyword arguments
- Limiting cache size
- Tracking cache hits and misses
- Preserving metadata with `functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Where are cached results stored?
3. How does the decorator know when it can reuse a result?
4. What are the advantages of caching?
5. What are the disadvantages of storing too many cached values?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Display cache hits and cache misses.
```

Example output:

```text
Cache Miss
Calculating...

Cache Hit
Using cached result
```

Or:

```text
Track how many results are currently
stored in the cache.
```

Example output:

```text
Cache Size: 5
```

---

## Real-World Connection

This pattern appears in:

- Web applications
- API clients
- Data processing systems
- Scientific computing
- Performance optimization

Caching is one of the most common performance techniques in software development. Rather than recomputing expensive results, applications often store and reuse previously calculated values.

Python's standard library includes similar functionality through:

```python
functools.cache
```

and:

```python
functools.lru_cache
```

which are widely used in production systems.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Results are stored and reused
- [ ] Duplicate calculations are avoided
- [ ] The original result is preserved
- [ ] The cache persists between function calls
- [ ] You understand how state is being stored
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/26-cache-decorator.py
```