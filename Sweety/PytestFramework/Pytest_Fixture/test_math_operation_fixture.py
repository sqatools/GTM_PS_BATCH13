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
    print("\n--class fixture initiated--")
    yield
    print("\n--class fixture completed--")


@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n--module fixture initiated--")
    yield
    print("\n--module fixture completed--")

@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n--package fixture initiated--")
    yield
    print("\n--package fixture completed--")


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n--session fixture initiated--")
    yield
    print("\n--session fixture completed--")


class TestMathOperation:

    def test_addition(self, fun_setup):
        n1 = 20
        n2 = 30
        assert n1+n2 == 50

    def test_multiplication(self):
        x = 3
        y = 20
        assert x*y == 60

    def test_division(self):
        v1 = 30
        v2 = 4
        assert v1//v2 == 8

    def test_subtraction(self):
        m = 500
        n = 200
        assert m -n == 300


    def test_greeting(self):
        print("Good Morning")