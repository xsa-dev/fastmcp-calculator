import asyncio

import pytest
from fastmcp.exceptions import ToolError

from calculator import mcp_server


def test_mcp_server_registers_all_calculator_tools():
    tools = asyncio.run(mcp_server.mcp.list_tools())
    tool_names = {tool.name for tool in tools}

    assert {"add", "subtract", "multiply", "divide"}.issubset(tool_names)


def test_mcp_add_tool_returns_sum():
    assert mcp_server.add_tool(2, 3) == 5


def test_mcp_subtract_tool_returns_difference():
    assert mcp_server.subtract_tool(10, 4) == 6


def test_mcp_multiply_tool_returns_product():
    assert mcp_server.multiply_tool(6, 7) == 42


def test_mcp_divide_tool_returns_quotient():
    assert mcp_server.divide_tool(8, 2) == 4


def test_mcp_divide_tool_rejects_zero_denominator():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        mcp_server.divide_tool(1, 0)


def test_mcp_call_tool_reports_division_by_zero_error():
    with pytest.raises(ToolError, match="Cannot divide by zero"):
        asyncio.run(mcp_server.mcp.call_tool("divide", {"a": 1, "b": 0}))
