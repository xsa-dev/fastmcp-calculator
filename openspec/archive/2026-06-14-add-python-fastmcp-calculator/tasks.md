# Tasks: Add Python terminal calculator with FastMCP server

## 1. Project setup

- [x] Choose minimal Python project layout and package name.
- [x] Use `uv` for project/dependency management.
- [x] Add `pyproject.toml` metadata for runtime dependencies, test dependencies, and CLI/server scripts.
- [x] Generate/update `uv.lock` if dependency resolution is required.
- [x] Keep generated/cache files out of version control.

## 2. Calculator behavior using TDD

- [x] Write failing unit tests for addition.
- [x] Implement minimal addition logic and verify tests pass.
- [x] Write failing unit tests for subtraction.
- [x] Implement minimal subtraction logic and verify tests pass.
- [x] Write failing unit tests for multiplication.
- [x] Implement minimal multiplication logic and verify tests pass.
- [x] Write failing unit tests for division.
- [x] Implement minimal division logic and verify tests pass.
- [x] Write failing unit test for division by zero.
- [x] Implement clear division-by-zero behavior and verify tests pass.

## 3. CLI using TDD

- [x] Write failing CLI tests for successful operations.
- [x] Implement CLI command parsing and output.
- [x] Write failing CLI test for invalid numeric input.
- [x] Implement invalid input handling.
- [x] Write failing CLI test for division by zero exit behavior.
- [x] Implement non-zero CLI exit for division by zero.

## 4. FastMCP server using TDD

- [x] Write failing tests proving MCP tool functions return expected results.
- [x] Implement FastMCP server module and expose add/subtract/multiply/divide tools.
- [x] Write failing tests for MCP division-by-zero behavior.
- [x] Implement clear MCP error behavior.
- [x] Add a documented stdio server entry point.

## 5. Documentation

- [x] Document installation steps using `uv`.
- [x] Document CLI examples.
- [x] Document MCP client registration example for stdio transport.
- [x] Document test and verification commands using `uv run`.

## 6. Verification and archive

- [x] Run full automated test suite.
- [x] Run CLI smoke commands.
- [x] If practical, run an MCP smoke/list-tools check.
- [x] Archive this OpenSpec change after implementation is verified.
- [x] Do not commit unless explicitly asked.
