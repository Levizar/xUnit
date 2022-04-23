from models import TestCase
from models.ResultReport import ResultReport

TestCaseList = list[TestCase]


class TestSuite:
    def __init__(self, test_cases: TestCaseList = None):
        if test_cases is None:
            test_cases = []
        self.test_suite = test_cases

    def add(self, test: TestCase) -> None:
        self.test_suite.append(test)

    def run(self) -> ResultReport:
        test_suite_results = ResultReport()
        for test in self.test_suite:
            test.run(test_suite_results)
        return test_suite_results

    def contain_test(self, test: TestCase) -> bool:
        return test in self.test_suite

    def contain_tests(self, tests: TestCaseList) -> bool:
        return set(tests).issubset(self.test_suite)
