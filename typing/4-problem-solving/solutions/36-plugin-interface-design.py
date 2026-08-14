"""
Solution Guidelines
- Solve only the stated exercise requirements.
- Do not include stretch goals.
- Do not include experimentation code.
- Prefer the simplest correct implementation.
- Prioritize readability over cleverness.
"""

from typing import Protocol


"""
Exercise 36 - Plugin Interface Design

Protocols allow applications to depend on
behaviour rather than concrete implementations.

This makes systems easier to extend while
maintaining clear type-safe contracts.
"""


class Plugin(Protocol):
    def process(self, text: str) -> str:
        ...


class UpperCasePlugin:
    def process(self, text: str) -> str:
        return text.upper()


class LowerCasePlugin:
    def process(self, text: str) -> str:
        return text.lower()


def run_plugin(plugin: Plugin, text: str) -> str:
    return plugin.process(text)


def main():
    plugin = UpperCasePlugin()

    result = run_plugin(plugin, "hello")

    print(result)


if __name__ == "__main__":
    main()