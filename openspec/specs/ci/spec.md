# Capability: Continuous Integration

## Requirements

### Requirement: GitHub Actions CI

The repository SHALL run a GitHub Actions workflow that validates the Python calculator project after repository changes.

#### Scenario: Push to main runs CI

- WHEN a commit is pushed to the `main` branch
- THEN GitHub Actions SHALL run the CI workflow
- AND the workflow SHALL install dependencies with `uv`
- AND the workflow SHALL build the package
- AND the workflow SHALL run the pytest suite

#### Scenario: Pull request to main runs CI

- WHEN a pull request targets the `main` branch
- THEN GitHub Actions SHALL run the CI workflow
- AND the workflow SHALL install dependencies with `uv`
- AND the workflow SHALL build the package
- AND the workflow SHALL run the pytest suite

#### Scenario: CI requires no secrets

- WHEN the CI workflow runs for normal build and test verification
- THEN it SHALL complete without requiring repository secrets
- AND it SHALL not expose credentials or tokens in workflow configuration
