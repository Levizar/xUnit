from models.TestCase import TestCase
from utils.utils import assert_equals


class TestCaseTest(TestCase):
    def __init__(self, name=""):
        super().__init__(name)
        self.log = ""

    def setup(self) -> None:
        super().setup()
        self.log += "Setup "

    def teardown(self) -> None:
        self.log += "tearDown "

    def test_method(self) -> None:
        self.log += "test_method "

    def failing_test_method(self) -> None:
        self.log += "failing_test_method "
        raise Exception("failing method error message")

    def test_dummy(self) -> None:
        self.log += "test_dummy "

    def test_test_methods_should_always_run_in_the_correct_order(self) -> None:
        test = TestCaseTest("test_method")
        test.run()
        assert_equals(
            test.log,
            "Setup test_method tearDown ",
            "Setup, method and teardown should always happen in that order"
        )

    def test_test_should_teardown_even_when_test_failed(self) -> None:
        test = TestCaseTest("failing_test_method")
        test.run()
        assert_equals(
            test.log,
            "Setup failing_test_method tearDown ",
            "teardown should always happen even when the test failed"
        )

    def test_test_template_should_succeed(self) -> None:
        test = TestCaseTest("test_method")
        result = test.run()
        assert_equals(
            result.summary(),
            "1 test(s) run - 0 fail",
            "basic formatting error"
        )

    def test_test_template_should_failed(self) -> None:
        test = TestCaseTest("failing_test_method")
        result = test.run()
        assert_equals(
            result.summary(),
            "1 test(s) run - 1 fail: failing_test_method",
            "basic formatting error when failure happens"
        )

    def test_test_should_compared(self) -> None:
        test_a = TestCaseTest("test_method")
        test_b = TestCaseTest("test_method")
        assert_equals(test_a, test_b, "Tests should be equals comparing their name")
