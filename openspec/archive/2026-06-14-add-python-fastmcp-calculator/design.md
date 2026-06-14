# Design: Python terminal calculator with FastMCP server

## Overview

Build a small Python package with three layers:

1. calculator domain logic
2. terminal CLI adapter
3. FastMCP server adapter

The calculator logic should be independent of terminal and MCP concerns so tests can cover behavior once and both adapters can reuse it.

## Proposed structure

```text
calculator/
  __init__.py
  core.py        # pure arithmetic functions
  cli.py         # argparse/typer-style terminal entry point
  mcp_server.py  # FastMCP app and tool registration
tests/
  test_core.py
  test_cli.py
  test_mcp_server.py
pyproject.toml
uv.lock
README.md
```

Exact files may change during implementation if justified, but the separation between core logic, CLI, and MCP server should remain.

## Runtime behavior

### Core logic

Use plain Python functions that accept numeric values and return numeric results. Division by zero should raise a project-owned exception or `ZeroDivisionError` with a clear message; adapters should translate that into user-facing errors.

### CLI

The CLI should support commands like:

```bash
calculator add 2 3
python -m calculator.cli add 2 3
```

Output should be result-only on success. Error text should go to stderr and use a non-zero exit code.

### MCP server

Use FastMCP to expose tools matching the core operations. Prefer stdio transport by default because it is the most common local MCP client registration path.

Example client configuration to document later:

```yaml
mcp_servers:
  calculator:
    command: "python"
    args: ["-m", "calculator.mcp_server"]
```

Because the project should use `uv`, documentation should prefer commands such as:

```yaml
mcp_servers:
  calculator:
    command: "uv"
    args: ["run", "python", "-m", "calculator.mcp_server"]
```

If package scripts are added, documentation may use the script command instead, but the examples should remain `uv`-based.

## Tooling

Use `uv` as the Python project and dependency manager. Project metadata should live in `pyproject.toml`; dependency locking should use `uv.lock` when dependencies are resolved. Verification commands should use `uv run` so tests and smoke checks run inside the managed project environment.

## Testing strategy

Follow strict TDD:

- write each failing test first
- run it and confirm the expected failure
- implement the minimum production code
- rerun the specific test and full test suite

Test levels:

- core unit tests for arithmetic and division by zero
- CLI tests through the command entry point or subprocess-style runner
- MCP tests by importing the server module and/or tool functions without depending on a real external agent

## Dependency notes

FastMCP dependency choice must be verified during implementation with `uv` against current package availability. If `fastmcp` packaging or import semantics differ from expectation, update implementation and documentation based on real tool output.

## Open questions

- Should numeric output preserve integers when possible (`5`) or always use floating point (`5.0`)? Proposal default: preserve clean human-readable numbers where practical.
- Should the CLI support an interactive REPL mode? Proposal default: no, keep v1 non-interactive and scriptable.
