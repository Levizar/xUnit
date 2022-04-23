from models.TestCase import TestCase
from tests.test_CaseTest import TestCaseTest
from models.TestSuite import TestSuite
from utils.utils import assert_equals, assert_true


class TestSuiteTest(TestCase):
    def test_test_suite_with_2_test_template_should_run(self) -> None:
        test_suite = TestSuite()
        test_suite.add(TestCaseTest("test_method"))
        test_suite.add(TestCaseTest("failing_test_method"))
        result = test_suite.run()
        assert_equals(
            result.summary(),
            "2 test(s) run - 1 fail: failing_test_method",
            "basic reporting error"
        )

    def test_test_suite_created_from_TestTestCase_should_contain_test_method(self) -> None:
        test_suite = TestCaseTest().make_TestSuite()
        assert_true(
            test_suite.contain_test(TestCaseTest("test_method")),
            "Test suite should contains test_method from TestCaseTest "
        )

    def test_test_suite_contain_tests(self) -> None:
        test_suite = TestSuite()
        test_a = TestCaseTest("test_method")
        test_b = TestCaseTest("failing_test_method")
        test_suite.add(test_a)
        test_suite.add(test_b)
        assert_true(test_suite.contain_tests([test_a, test_b]))

    def test_test_suite_created_from_TestTestCase_should_contain_all_test_methods(self) -> None:
        test_suite = TestCaseTest().make_TestSuite()
        assert_true(
            test_suite.contain_tests([
                TestCaseTest("test_method"),
                TestCaseTest("test_dummy")
            ]),
            "Test suite should contains test_method and failing_test_method from TestCaseTest "
        )


if __name__ == '__main__':
    ts_TestSuiteTest = TestSuiteTest().make_TestSuite()
    res = ts_TestSuiteTest.run()
    print(res.summary())
    if res.failed_tests:
        print(res.failure_details())
