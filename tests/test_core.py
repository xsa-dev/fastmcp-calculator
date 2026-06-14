import pytest

from calculator.core import add, divide, multiply, subtract


def test_add_returns_sum_of_two_numbers():
    assert add(2, 3) == 5


def test_subtract_returns_difference_between_two_numbers():
    assert subtract(10, 4) == 6


def test_multiply_returns_product_of_two_numbers():
    assert multiply(6, 7) == 42


def test_divide_returns_quotient_of_two_numbers():
    assert divide(8, 2) == 4


def test_divide_rejects_zero_denominator_with_clear_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)
