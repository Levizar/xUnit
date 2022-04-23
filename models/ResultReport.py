from utils.utils import format_error_string


class ResultReport:
    def __init__(self):
        self.test_count = 0
        self.test_failed_count = 0
        self.failed_tests = []

    def test_started(self) -> None:
        self.test_count += 1

    def test_failed(self, test_name: str, test_error: Exception) -> None:
        self.failed_tests.append((test_name, test_error))

    def summary(self) -> str:
        failed_test_names = [test_name for test_name, _ in self.failed_tests]
        return (
            f"{self.test_count} test(s) run - {len(self.failed_tests)} fail"
            f"{': ' + ', '.join(failed_test_names) if self.failed_tests else ''}"
        )

    def failure_details(self) -> str:
        failure_details = ""
        for test_name, error in self.failed_tests:
            failure_details += f"{test_name} {format_error_string(error)}\n"
        return failure_details
