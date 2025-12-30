"""
pip install pytest
"""
import pytest

"""
Fixture :  fixture is a function that we want to execute before executing any test cases or with multiple scope.
to configure the pre-requisite on different levels.

function scope : This fixture will execute before and after execution of each test cases or test function.
class scope : This fixture will execute before and after execution of each test class.
module scope: This fixture will execute before and after execution of each test module or test suite file.
package scope:  This fixture will execute before and after execution of each test package.
session scope: This fixture will execute before and after execution of session of test execution.
"""


@pytest.fixture(scope="function", autouse=True)
def fun_setup():
    print("\n--Fun fixture initiated--")
    yield
    print("\n--Fun fixture completed--")

@pytest.fixture(scope="class", autouse=True)
def class_setup():
    print("\n--Class fixture initiated--")
    yield
    print("\n--Class fixture completed--")
@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n--Module fixture initiated--")
    yield
    print("\n--Module fixture completed--")
@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n--Package fixture initiated--")
    yield
    print("\n--Package fixture completed--")
@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n--Session fixture initiated--")
    yield
    print("\n--Session fixture completed--")

class TestMatch0pration:

     def test_addition(self, fun_setup):
            n1 = 20
            n2 = 30
            assert n1 + n2 == 50
     def test_multiplication(self):
         x = 3
         y = 60
         assert x * y == 180

     def test_division(self):
         v1 = 500
         v2 = 200
         assert v1/v2 == 100

     def test_subtraction(self):
         m = 800
         n = 400
         assert m - n == 400

     def test_greeting(self):
         print("Good Morning")







