# FastMCP Calculator

A small Python calculator that works in two modes:

1. terminal CLI for simple arithmetic operations
2. FastMCP server exposing the same operations to MCP-compatible agents

The project is managed with `uv`.

## Requirements

- Python 3.12+
- uv

## Install dependencies

```bash
uv sync
```

## Run tests

```bash
uv run pytest -q
```

## CLI usage

Run through the module:

```bash
uv run python -m calculator.cli add 2 3
uv run python -m calculator.cli subtract 10 4
uv run python -m calculator.cli multiply 6 7
uv run python -m calculator.cli divide 8 2
```

Or use the installed console script through uv:

```bash
uv run calculator add 2 3
```

Successful commands print only the result:

```text
5
```

Division by zero exits non-zero and prints an error to stderr:

```bash
uv run python -m calculator.cli divide 1 0
```

## MCP server usage

Run the FastMCP server over stdio:

```bash
uv run python -m calculator.mcp_server
```

It exposes these MCP tools:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

Example Hermes MCP client registration:

```yaml
mcp_servers:
  calculator:
    command: "uv"
    args:
      - "--directory"
      - "/Users/alxy/Desktop/1PROJ/FIRM-A/hsh"
      - "run"
      - "python"
      - "-m"
      - "calculator.mcp_server"
```

After adding this to a client configuration, restart the client so it discovers the server tools.

## Verification commands

```bash
uv run pytest -q
uv run python -m calculator.cli add 2 3
uv run python -m calculator.cli divide 8 2
uv run python -m calculator.cli divide 1 0
uv run python - <<'PY'
import asyncio
from calculator.mcp_server import mcp

async def main():
    tools = await mcp.list_tools()
    print(sorted(tool.name for tool in tools))

asyncio.run(main())
PY
```

The division-by-zero command is expected to exit with a non-zero status.
