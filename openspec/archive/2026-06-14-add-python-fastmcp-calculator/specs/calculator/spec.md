# Capability: Calculator

## ADDED Requirements

### Requirement: Shared arithmetic operations

The system SHALL provide shared calculator logic for addition, subtraction, multiplication, and division.

#### Scenario: Add two numbers

- WHEN the calculator is asked to add `2` and `3`
- THEN it SHALL return `5`

#### Scenario: Subtract two numbers

- WHEN the calculator is asked to subtract `4` from `10`
- THEN it SHALL return `6`

#### Scenario: Multiply two numbers

- WHEN the calculator is asked to multiply `6` and `7`
- THEN it SHALL return `42`

#### Scenario: Divide two numbers

- WHEN the calculator is asked to divide `8` by `2`
- THEN it SHALL return `4`

#### Scenario: Reject division by zero

- WHEN the calculator is asked to divide by `0`
- THEN it SHALL fail with a clear division-by-zero error

### Requirement: Terminal CLI

The system SHALL provide a terminal CLI for simple arithmetic operations.

#### Scenario: Run successful CLI operation

- WHEN a user runs `calculator add 2 3`
- THEN the CLI SHALL print `5`
- AND it SHALL exit with status `0`

#### Scenario: Reject invalid CLI numbers

- WHEN a user provides a non-numeric operand
- THEN the CLI SHALL print a clear error message
- AND it SHALL exit with a non-zero status

#### Scenario: Reject CLI division by zero

- WHEN a user runs `calculator divide 1 0`
- THEN the CLI SHALL print a clear division-by-zero error
- AND it SHALL exit with a non-zero status

### Requirement: FastMCP server

The system SHALL expose calculator operations through a local FastMCP server suitable for agent use.

#### Scenario: MCP tools are available

- WHEN the MCP server is loaded
- THEN tools named `add`, `subtract`, `multiply`, and `divide` SHALL be registered

#### Scenario: MCP tool returns calculation result

- WHEN an agent calls the MCP `add` tool with `2` and `3`
- THEN the tool SHALL return `5`

#### Scenario: MCP tool rejects division by zero

- WHEN an agent calls the MCP `divide` tool with denominator `0`
- THEN the tool SHALL report a clear division-by-zero error
