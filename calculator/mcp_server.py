"""FastMCP server exposing calculator tools."""

from __future__ import annotations

from fastmcp import FastMCP

from calculator.core import add, divide, multiply, subtract

mcp = FastMCP("calculator")


@mcp.tool(name="add")
def add_tool(a: float, b: float) -> float:
    """Add two numbers."""
    return add(a, b)


@mcp.tool(name="subtract")
def subtract_tool(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return subtract(a, b)


@mcp.tool(name="multiply")
def multiply_tool(a: float, b: float) -> float:
    """Multiply two numbers."""
    return multiply(a, b)


@mcp.tool(name="divide")
def divide_tool(a: float, b: float) -> float:
    """Divide the first number by the second."""
    return divide(a, b)


def main() -> None:
    """Run the MCP server over stdio by default."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
