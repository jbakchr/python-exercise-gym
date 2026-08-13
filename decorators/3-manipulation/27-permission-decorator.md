# Exercise 27 - Permission Decorator

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
➡️ Current Manipulation Exercise
⬜ Next Manipulation Exercise
⬜ Future Exercise
```

---

## Goal

Use:

```text
decorators and conditional execution
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A reusable permission decorator that
controls access to protected functions.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic decorators
- Flexible wrappers
- Return values
- State management
- Function arguments
- Positional arguments
- Keyword arguments
- Conditional logic

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you need to:

```text
Restrict access to certain operations.
```

Example:

```text
Deleting user accounts should only be
allowed for administrators.

Viewing confidential information should
only be allowed for authorized staff.

Running maintenance operations should
require special permissions.
```

The goal is to solve a small practical problem.

---

## Challenge

Build a solution that:

1. Checks permissions before executing a function
2. Allows authorized users to continue
3. Blocks unauthorized users
4. Keeps the permission logic reusable

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a decorator named `requires_admin`
- Check whether the current user is an administrator
- Execute the function if permission is granted
- Display a message if permission is denied
- Work with functions that accept arguments

Your solution should not:

- Duplicate permission checks in every function
- Execute protected functions for unauthorized users

---

## Starter Code

```python
current_user_is_admin = False


def requires_admin(func):
    pass


@requires_admin
def delete_user(username):
    print(f"Deleting {username}")


delete_user("alice")
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Allow authorized users to execute
protected functions.

Prevent unauthorized users from
executing protected functions.
```

Example:

```text
Access Denied
```

Another example:

```text
Access Granted
Deleting alice
```

You should also be able to explain:

- Why the check occurs inside the wrapper
- Why the original function is not executed when permission is denied
- How the decorator could be reused

---

## Hints

### Hint 1

The wrapper decides whether the original function should run.

---

### Hint 2

You may need something similar to:

```python
if current_user_is_admin:
    ...
```

before calling the original function.

---

### Hint 3

If permission is granted:

```python
return func(*args, **kwargs)
```

Otherwise:

```python
display a message
```

and stop execution.

---

## Possible improvements

Once the basic solution works, consider:

- Supporting multiple permission levels
- Supporting custom permission names
- Logging denied access attempts
- Raising* eceptions instead of displaying messages
- Preserving metadata with functools.wraps`

These are optional improvements.

---

## Reflection

Answer the following questions.

1. What problem does this decorator solve?
2. Why is the permission check placed inside the wrapper?
3. What happens when access is denied?
4. How does this approach reduce duplicated code?
5. How could this utility be reused in larger applications?

---

## Stretch Goal

Extend the utility with one additional feature.

The extension should build on the existing solution.

Example:

```text
Support different roles instead
of a simple admin/non-admin check.
```

Example:

```text
admin
manager
employee
guest
```

Or:

```text
Allow the decorator to receive
the required role as a parameter.
```

Example:

```python
@requires_role("admin")
def delete_user():
    ...
```

---

## Real-World Connection

This pattern appears in:

- Web applications
- Administrative dashboards
- Internal business systems
- APIs
- Security frameworks

Many systems must verify permissions before allowing sensitive actions. Rather than placing permission checks inside every function, developers often centralize the logic using decorators.

Frameworks such as Flask, Django, and FastAPI commonly use similar patterns to protect routes and operations.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The utility works as required
- [ ] Authorized users can execute protected functions
- [ ] Unauthorized users are blocked
- [ ] The original function only executes when permission is granted
- [ ] The decorator works with function arguments
- [ ] You understand how conditional execution works inside a wrapper
- [ ] You completed at least one practical use case

---

## Solution

```text
solutions/27-permission-decorator.py
```