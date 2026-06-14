"""Command-line interface for the calculator."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from calculator.core import add, divide, multiply, subtract

_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def _parse_number(value: str) -> float:
    try:
        return float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid number: {value}") from exc


def _format_result(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="calculator", description="Simple terminal calculator")
    parser.add_argument("operation", choices=sorted(_OPERATIONS))
    parser.add_argument("a", type=_parse_number)
    parser.add_argument("b", type=_parse_number)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        if isinstance(exc.code, int):
            return exc.code
        if exc.code is None:
            return 0
        return 1

    try:
        result = _OPERATIONS[args.operation](args.a, args.b)
    except ZeroDivisionError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(_format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
