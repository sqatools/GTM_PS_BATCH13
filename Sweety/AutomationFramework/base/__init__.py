->  install pytest with command
    ->  pip install pytest


-> create a test file with test_<filename> as prefix

-> create test function with test_<function_name> as prefix


->  command to run the test file from command prompt.
    ->  python -m pytest -v <test_file_path/name>
    ->  -m :  python path to consider as root directory
    ->  -v :  verbose of test execution to provide detailed information.
    e.g. python -m pytest -v .\test_math_operation.py


->  Execute specific group of test cases with command
    -> python -m pytest -v -m "smoke" test_<file_path>


->  Execute test cases with multiple marker using or condition.
    ->  python -m pytest -v -m "smoke or sanity" .\Basics\


-> Execute test cases with multiple marker using and condition.
    ->  python -m pytest -v -m "smoke and sanity" .\Basics\


->  There are 2 skip markers in pytest
    ->  @pytest.mark.skip : un conditional skip, it will skip test case in any condition.
    ->  @pytest.mark.skipif(env=='prod') , it will skip test cases in production environment


->  Xfail Marker
    ->  @pytest.mark.xfail :  test cases marked as xfail if the particular is failing due to
                              expected condition it could be prod issue or environment issue.

    ->  If expected failure condition is fixed, the xfail marker test will show as xpassed in the result
    ->  we can mention reason and condition as well in xfail marker.
    ->  @pytest.mark.xfail(ENV=="prod", reason="feature is not available in prod environment")


-> Parametrize marker
   -> @pytest.mark.parametrize("v1, v2", [('abc', '123'), ('pqr', 456)])
      -> parametrize marker help us to provide multiple inputs to single test function and consider as that
         number of test cases in the result.
      e.g.
      test_mark_parametrization.py::test_login[user1-user@123] PASSED        [ 25%]
      test_mark_parametrization.py::test_login[user2-pass@123] PASSED        [ 50%]
      test_mark_parametrization.py::test_login[user3-user@1234] PASSED       [ 75%]
      test_mark_parametrization.py::test_login[user4-admin@123] PASSED


->  Generate html report, we will install pytest-html package.
    ->  pip install pytest-html

    # execution command
    -> python -m pytest -v .\tests\ --html=logs/report.html
