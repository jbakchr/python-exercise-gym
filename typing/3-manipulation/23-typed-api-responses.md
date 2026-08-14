# Exercise 23 - Typed API Responses

## Progression

```text
✅ Foundations Complete
✅ Exploration Complete
✅ Exercise 21 - Typed Configuration Data
✅ Exercise 22 - Typed Environment Settings
➡️ Current Manipulation Exercise
⬜ Exercise 24 - Generic Data Containers
```

---

## Goal

Use:

```text
TypedDict
Type Aliases
Literal
Nested Data Structures
Function Type Annotations
```

to build a practical utility.

By the end of this exercise you will have created:

```text
A type-safe API response model.
```

---

## Previously Learned

Before starting this exercise you should already understand:

- Basic type annotations
- Function parameter and return types
- Type aliases
- TypedDict
- Literal
- Dictionary annotations
- Nested structures
- Typed configuration models

This exercise builds on concepts introduced earlier in the topic.

---

## Scenario

Imagine you are calling an external API.

The API returns user information in the following structure:

```python
{
    "status": "success",
    "data": {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com"
    }
}
```

Many developers treat API responses as untyped dictionaries.

This often leads to mistakes such as:

```python
response["userdata"]
```

instead of:

```python
response["data"]
```

or assuming fields exist when they do not.

You want to model API responses using Python's typing system so that the expected structure is clearly defined and easier to work with.

The goal is to create a reusable type-safe response model.

---

## Challenge

Build a solution that:

1. Defines a typed user model.
2. Defines a typed API response model.
3. Supports successful API responses.
4. Provides a utility function for extracting a user's email address.

Focus on creating something useful rather than simply demonstrating syntax.

---

## Requirements

Your solution must:

- Create a type alias called `ApiStatus`
- Restrict status values to:

```text
success
error
```

- Create a `TypedDict` called:

```python
UserData
```

containing:

```text
id
username
email
```

- Create a second `TypedDict` called:

```python
ApiResponse
```

containing:

```text
status
data
```

- Create a function:

```python
def get_user_email(response: ApiResponse) -> str:
```

that returns the user's email address.

Your solution should not:

- Use `Any`
- Use untyped dictionaries
- Hardcode email values

---

## Starter Code

```python
from typing import Literal, TypedDict


# Create an ApiStatus alias


# Create UserData


# Create ApiResponse


response = {
    "status": "success",
    "data": {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
    },
}


def get_user_email(response):
    pass


print(get_user_email(response))
```

---

## Verify Your Solution

Your completed program should be able to:

```text
Represent an API response using types.
Model nested response data.
Restrict response status values.
Extract user information safely.
```

Expected output:

```text
alice@example.com
```

You should also be able to explain:

- Why TypedDict is useful for API responses
- How nested typing improves readability
- What mistakes type checkers can identify
- How this pattern can be reused for other APIs

---

## Hints

### Hint 1

The response contains another dictionary inside it.

Think about creating multiple `TypedDict` definitions.

---

### Hint 2

The `data` field should use your `UserData` type.

---

### Hint 3

Use:

```python
response["data"]["email"]
```

inside the utility function.

---

## Possible Improvements

Once the basic solution works, consider:

- Supporting error responses
- Adding additional user fields
- Creating response models for other API endpoints
- Modelling lists of users
- Creating reusable API response patterns

These are optional improvements.

---

## Reflection

Answer the following questions.

1. Why are API responses good candidates for TypedDict?
2. How does nesting TypedDict objects improve maintainability?
3. Which concepts from previous exercises were reused?
4. What kinds of API mistakes could type checking help prevent?

---

## Stretch Goal

Extend the utility with one additional feature.

Create a function:

```python
def get_username(response: ApiResponse) -> str:
```

that returns the username from the response.

---

## Real-World Connection

This pattern appears in:

- REST APIs
- FastAPI applications
- Flask applications
- Web services
- Third-party integrations

Developers frequently work with JSON responses that contain nested structures.

Using TypedDict helps document the expected shape of API responses and allows type-checking tools to detect mistakes before code reaches production.

---

## Success Criteria

You can consider this exercise complete when:

- [ ] The `ApiStatus` type alias is implemented
- [ ] The `UserData` TypedDict is implemented
- [ ] The `ApiResponse` TypedDict is implemented
- [ ] The response data is correctly typed
- [ ] `get_user_email()` works correctly
- [ ] You understand how nested TypedDict structures work
- [ ] You can explain how typing improves API integrations

---

## Solution

See:

```text
solutions/23-typed-api-responses.py
```