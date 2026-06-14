# Change: Add GitHub Actions CI

## Summary

Add a GitHub Actions workflow that runs automatically for repository changes and verifies the Python calculator project by installing dependencies with `uv`, building the package, and running the test suite.

## Motivation

The project is now published as a public GitHub repository. Each pushed commit should be checked remotely so regressions in packaging or tests are visible on GitHub without relying only on local execution.

## Scope

- Add a GitHub Actions workflow under `.github/workflows/`.
- Trigger the workflow on pushes to `main` and on pull requests targeting `main`.
- Use `uv` for Python dependency installation and command execution.
- Run package build verification.
- Run the existing pytest test suite.

## Non-goals

- No application feature changes.
- No dependency upgrades beyond the workflow runner setup actions.
- No release publishing, package publishing, secrets, deployments, or branch protection changes.
- No changes to calculator behavior.

## Safety

- The workflow must not require or expose secrets.
- The workflow must not print tokens, credentials, private endpoints, or authorization headers.
