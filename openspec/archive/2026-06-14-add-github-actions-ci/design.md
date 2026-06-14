# Design: GitHub Actions CI

## Overview

Add a single GitHub Actions workflow to validate the Python project on GitHub-hosted runners. The workflow should be small, deterministic, and limited to build/test verification.

## Workflow design

File: `.github/workflows/ci.yml`

Name: `CI`

Triggers:

- `push` to `main`
- `pull_request` targeting `main`

Job:

- `test`
- Runner: `ubuntu-latest`
- Python version: `3.12`, matching the project's `requires-python = ">=3.12"` baseline.

Steps:

1. Check out repository contents.
2. Install `uv` using the official `astral-sh/setup-uv` action.
3. Set up Python 3.12 using `actions/setup-python`.
4. Run `uv sync --dev` to install runtime and dev dependencies from the lockfile/project metadata.
5. Run `uv build` to verify packaging.
6. Run `uv run pytest` to execute all tests.

## Alternatives considered

- Matrix across multiple Python versions: not needed for the initial CI because the current project only requires a baseline public verification path.
- Lint/type checking: not part of this change unless the project already defines stable commands for them.
- Publishing artifacts/releases: explicitly out of scope.

## Verification

Local verification before pushing:

- `uv build`
- `uv run pytest`

Remote verification after pushing:

- `gh run list --workflow CI --limit 1`
- `gh run watch <run-id> --exit-status`

## Risks

- If the lockfile is missing or stale, `uv sync --dev` could fail remotely. Verify locally before pushing.
- If GitHub Actions has transient network issues, rerun the workflow rather than changing project code.
