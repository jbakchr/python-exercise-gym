**Prompt [Thanks. Despite the roadmap saying that the next... | Try in Copilot Chat](https://m365.cloud.microsoft/chat/entity1-d870f6cd-4aa5-4d42-9626-ab690c041429/eyJpZCI6IlZYTmxjbFl4ZkdoMGRIQnpPaTh2YzNWaWMzUnlZWFJsTFdsdWRDNXZabVpwWTJVdVkyOXRMM3hQU1VRNk5UVTVZVEV5WWprdE9EUTVNaTAwWW1Wa0xUazJOR0V0TW1ZME1HTXlNekF4Wm1JMWZHTTBNREk1T0RnNExUazRaalV0TkdWbE9TMWhaalUyTFRSak9EUmpaRE00WVdFMVlYd3lNREkyTFRBNExURXpWREV5T2pVd09qVTJMak14TnpReE5EUmEiLCJzY2VuYXJpbyI6InNoYXJlTGlua1ZpYVJpY2hDb3B5IiwicHJvcGVydGllcyI6eyJwcm9tcHRTb3VyY2UiOiJ1c2VyIiwiY2xpY2tUaW1lc3RhbXAiOiIyMDI2LTA4LTEzVDEyOjUwOjU2LjY5OVoifSwiY2hhdFR5cGUiOiJ3b3JrIiwidmVyc2lvbiI6MS4xfQ)**
Thanks. Despite the roadmap saying that the next thing to work on should be "pathlib" I would actually like for the next thing to work being "typing".

What's your thought on that?
**Response**
Honestly? I think **typing is a better choice than pathlib** for *this specific project*.

Not because `typing` is more important.

But because it is a better fit for the thing you're trying to build.

## My reasoning

When I look at your exercise-gym philosophy, I see this:

```text
Understand
↓
Practice
↓
Build intuition
↓
Use naturally
```

The topics that benefit the most from this style of learning are topics where:

```text
Reading ≠ Mastery
```

Decorators are a perfect example.

You can read about decorators for hours and still struggle to write one from memory.

Typing is similar.

***

## Pathlib Has A Different Learning Curve

With pathlib, most people learn through:

```python
Path("data")
Path.glob()
Path.read_text()
Path.mkdir()
```

and then immediately use it in real projects.

The challenge is:

```text
Remembering the API
```

not:

```text
Developing deep mental models
```

Many pathlib exercises will naturally become:

```text
Use this method
Use that method
Use another method
```

which risks feeling a bit documentation-driven.

Not bad.

Just different.

***

## Typing Is Made For Skill Ladders

Typing has something decorators also have.

A progression.

Example:

```text
Type hints
↓
Return types
↓
Optional
↓
Union
↓
Type aliases
↓
TypedDict
↓
Protocols
↓
Generics
↓
TypeVar
↓
Bounded TypeVars
```

Each concept naturally builds on previous concepts.

That's exactly how your repository is structured.

***

## Typing Also Solves A Real Pain Point

One thing I've noticed from our previous discussions is that you're interested in:

* Professional Python development
* FastAPI
* APIs
* AI tooling
* Larger codebases

Typing appears everywhere in those domains.

A learner who masters typing gains skills that transfer directly to:

```text
FastAPI
Pydantic
Dataclasses
Libraries
Testing
Large projects
Open source work
```

The return on investment is huge.

***

## The Exercise Potential Is Excellent

I can immediately imagine the progression.

### Foundations

```text
01 Basic Parameter Types
02 Return Types
03 Multiple Parameters
04 Optional Values
05 Union Types
06 Collections
07 Dicts and Lists
08 Type Aliases
09 Annotating Functions
10 Build a Typed Utility
```

You are learning the syntax.

***

### Exploration

```text
11 Literal
12 Final
13 NewType
14 TypedDict
15 NamedTuple
16 Callable
17 Any
18 Self
19 Type Inference
20 Type Narrowing
```

You start exploring behaviour.

***

### Manipulation

```text
21 Typed Configuration Loader
22 Typed API Response
23 Typed User Records
24 Typed Data Transformer
25 Typed Validation Utility
26 Generic Container
27 Generic Cache
28 Generic Stack
29 Generic Repository
30 Type-Safe Toolkit
```

Now things get interesting.

***

### Problem Solving

```text
31 Refactor Untyped Legacy Code

32 Eliminate Any

33 Build Type-Safe Plugin System

34 Replace Runtime Bugs With Types

35 Validate Nested Data

36 Generic Data Pipeline

37 Type-Safe Event System

38 Typed Configuration Framework

39 Protocol-Based Architecture

40 Design Challenge
```

This is where the real learning happens.

***

## Typing Fits Your Future Topics Better

Something else occurred to me.

Typing acts as a force multiplier.

After completing typing:

```text
exceptions
logging
dataclasses
sqlite
testing
async
```

all become opportunities to reinforce typing.

For example:

```python
def load_config(path: Path) -> dict[str, Any]:
```

```python
async def fetch_user(user_id: int) -> User:
```

```python
class Config(TypedDict):
    host: str
    port: int
```

Typing enhances every future topic.

Pathlib doesn't.

***

## One Possible Reordering

If this were my repository, I might actually evolve the roadmap to:

```text
typing
pathlib
exceptions
logging
dataclasses
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
Typing becomes a foundation
that improves every subsequent topic.
```

***

## One Caveat

There is one danger with a typing topic.

Many typing resources become:

```text
Let's learn every type annotation feature.
```

which becomes boring quickly.

I would instead focus relentlessly on:

```text
How does typing help me write better code?
```

For example, compare these two exercises:

Less interesting:

```text
Create a TypeAlias.
```

More interesting:

```text
You inherit a function that returns:

dict[str, str | int | bool]

Create a clearer type definition.
```

Same concept.

Much more meaningful.

***

## My Verdict

If your goal were:

```text
Build practical Python utilities
```

I'd say:

```text
pathlib first
```

If your goal is:

```text
Build a world-class deliberate practice curriculum
```

I'd say:

```text
typing first
```

Because typing has:

* Better concept progression
* More opportunity for accumulated learning
* Better "skill ladder" characteristics
* Strong transfer to future topics
* More room for deliberate practice
* More opportunity for genuine mastery

In fact, looking at your repository philosophy, I suspect **typing may ultimately become an even stronger reference implementation than decorators** if designed well. Decorators teach a powerful language feature. Typing teaches a mindset that will show up throughout the rest of the curriculum.
