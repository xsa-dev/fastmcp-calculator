from calculator.cli import main


def test_cli_add_prints_result_and_exits_zero(capsys):
    exit_code = main(["add", "2", "3"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "5\n"
    assert captured.err == ""


def test_cli_subtract_prints_result_and_exits_zero(capsys):
    exit_code = main(["subtract", "10", "4"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "6\n"
    assert captured.err == ""


def test_cli_multiply_prints_result_and_exits_zero(capsys):
    exit_code = main(["multiply", "6", "7"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "42\n"
    assert captured.err == ""


def test_cli_divide_prints_result_and_exits_zero(capsys):
    exit_code = main(["divide", "8", "2"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "4\n"
    assert captured.err == ""


def test_cli_invalid_number_prints_error_and_exits_nonzero(capsys):
    exit_code = main(["add", "not-a-number", "3"])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert "Invalid number" in captured.err


def test_cli_division_by_zero_prints_error_and_exits_nonzero(capsys):
    exit_code = main(["divide", "1", "0"])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert "Cannot divide by zero" in captured.err
