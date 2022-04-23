import inspect
import tests


def main():
    classes_to_run = [obj for name, obj in inspect.getmembers(tests) if inspect.isclass(obj)]
    for cls in classes_to_run:
        run_test_class(cls)


def run_test_class(cls) -> None:
    test_suite = cls.make_TestSuite()
    report_results = test_suite.run()
    print(report_results.summary())
    if report_results.failed_tests:
        print(report_results.failure_details())


if __name__ == '__main__':
    main()
