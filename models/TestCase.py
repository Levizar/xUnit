from models.ResultReport import ResultReport
from models.TestSuite import TestSuite


class TestCase:
    def __init__(self, name: str = ""):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

    def __hash__(self):
        return 0

    def setup(self) -> None:
        pass

    def run(self, result_report: ResultReport = None) -> ResultReport:
        if result_report is None:
            result_report = ResultReport()
        result_report.test_started()
        self.setup()
        method = getattr(self, self.name)
        try:
            method()
        except Exception as e:
            result_report.test_failed(method.__name__, e)
        self.teardown()
        return result_report

    def teardown(self):
        pass

    @classmethod
    def make_TestSuite(cls) -> TestSuite:
        test_method_list = [
            cls(method)
            for method
            in dir(cls)
            if callable(getattr(cls, method)) and method.startswith("test_")
        ]
        return TestSuite(test_method_list)
