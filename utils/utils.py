ERROR_COLOR = "\033[91m"
END_COLOR = "\033[0m"


def assert_equals(result, expected, message) -> None:
    message = message + "\n"
    message += f"expected: {expected}\n"
    message += f"result: {result}"
    assert result == expected, message


def assert_true(result, message="") -> None:
    message = message + "\n"
    message += f"expected: True\n"
    message += f"result: {result}"
    assert result, message


def format_error_string(error) -> str:
    return ERROR_COLOR + f"{error}" + END_COLOR
