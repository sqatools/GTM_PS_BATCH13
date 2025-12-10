import pytest

@pytest.fixture(scope="function", autouse=True)
def function_setup():
    print("\n Function Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n Function Fixture finished")

@pytest.fixture(scope="class", autouse=True)
def class_setup():
    print("\n class Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n class Fixture finished")

@pytest.fixture(scope="module", autouse=True)
def module_setup():
    print("\n module Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n module Fixture finished")

@pytest.fixture(scope="package", autouse=True)
def package_setup():
    print("\n package Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n package Fixture finished")

@pytest.fixture(scope="session", autouse=True)
def session_setup():
    print("\n session Fixture initiated")
    yield                                      #yield : means after this execution
    print("\n session Fixture finished")

class TestMathOperation:
    def test_addition(self,):
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