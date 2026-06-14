# Project OpenSpec

## Purpose

This project uses OpenSpec changes to govern implementation work. Source code changes should follow an approved change proposal, task list, and capability spec.

## Active changes

None.

## Completed changes

- `2026-06-14-add-github-actions-ci`: added GitHub Actions CI for build and test verification on pushes and pull requests.
- `2026-06-14-add-python-fastmcp-calculator`: created a Python terminal calculator that also runs as a FastMCP MCP server for agent access.

## Working rules

- Do not edit production source before an OpenSpec change exists and has been reviewed.
- Keep each change scoped to one purpose.
- Use TDD for new behavior.
- Use `uv` for this Python project unless a later approved change says otherwise.
- Do not commit unless explicitly asked.
- Do not include secrets in code, tests, docs, logs, or examples.
