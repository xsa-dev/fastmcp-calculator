# Change: Add Python terminal calculator with FastMCP server

## Summary

Create a new Python application that works both as:

1. a terminal calculator for simple arithmetic operations, and
2. a FastMCP-based MCP server exposing the same calculator capabilities to AI agents.

## Motivation

The user wants a small program that can be used directly from a terminal and also registered as an MCP server so agents can call calculator tools programmatically.

## Scope

In scope:

- Python project scaffolding for a calculator package.
- `uv`-managed Python project setup, including dependency and script metadata.
- Command-line interface for simple operations.
- FastMCP server entry point exposing calculator operations as MCP tools.
- Automated tests written before production code using TDD.
- Documentation for local terminal use and MCP registration.
- Verification commands for tests and basic CLI/MCP smoke checks.

Out of scope:

- Advanced symbolic math.
- Scientific calculator functions beyond simple arithmetic.
- GUI, web UI, or mobile UI.
- Persistent history/database.
- Authentication, remote deployment, or network-hosted MCP service.
- Modifying Hermes Agent user/profile config automatically.

## Proposed capabilities

### Terminal calculator

The terminal app must support simple operations:

- addition
- subtraction
- multiplication
- division

The CLI should support a non-interactive mode suitable for scripts, for example:

```bash
calculator add 2 3
calculator subtract 10 4
calculator multiply 6 7
calculator divide 8 2
```

It should print only the result on success, making it easy to pipe or parse.

### Python API

A small internal Python API should implement calculator behavior separately from the CLI and MCP transport, so both entry points share tested logic.

### FastMCP server

The MCP server must expose tools for the same operations:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

The server should be runnable through a local stdio command compatible with MCP clients.

### Error handling

- Division by zero must return a clear error in CLI mode and raise/report a clear MCP tool error in MCP mode.
- Invalid numeric input must fail with a clear message and non-zero exit code in CLI mode.

## Acceptance criteria

- Running the test suite passes.
- CLI returns correct results for add/subtract/multiply/divide.
- CLI exits non-zero on division by zero.
- FastMCP server defines callable tools for all four operations.
- Calculator business logic is covered by unit tests.
- CLI behavior is covered by tests.
- MCP tool functions are covered by tests without requiring a long-running interactive agent session.
- README documents installation, CLI use, and MCP client registration example.

## Verification plan

Implementation must record and run commands equivalent to:

```bash
uv run pytest -q
uv run python -m calculator.cli add 2 3
uv run python -m calculator.cli divide 8 2
uv run python -m calculator.cli divide 1 0
```

If a package manager script is added, also run the project-level test command documented in README.

## Safety and secrets

This change should not introduce or require secrets. Documentation must not include real tokens, private endpoints, or authorization headers.
