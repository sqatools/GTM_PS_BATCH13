import pytest

#Fixture : nothing but pre-request/pre-condition before test case execution
"""
Fixture :  fixture is a function that we want to execute before executing any test cases or with multiple scope.
to configure the pre-requisite on different levels.

function scope : This fixture will execute before and after execution of each test cases or test function.
class scope : This fixture will execute before and after execution of each test class.
module scope: This fixture will execute before and after execution of each test module or test suite file.
package scope:  This fixture will execute before and after execution of each test package.
session scope: This fixture will execute before and after execution of session of test execution.
"""

@pytest.fixture(scope="function",autouse=True)      #If we use autouse=True then it will apply for all test cases
def function_setup():
    print("\n Function Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n Function Fixture finished")


class TestMathOperation:
    def test_addition(self):
        n1 = 20
        n2 = 30
        assert n1+n2 == 50

    def test_multiplication(self,function_setup):    #here we define to use particular test case only
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