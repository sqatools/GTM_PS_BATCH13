"""
pip install pytest
"""
import pytest

@pytest.fixture(scope ="function",autouse=True)
def func_setup():
    print("\n --Function fixture initiated--")
    yield
    print("--Function fixture completed--")

@pytest.fixture(scope ="class",autouse=True)
def class_setup():
    print("\n --Class fixture initiated--")
    yield
    print("--Class fixture completed--")

@pytest.fixture(scope ="module",autouse=True)
def module_setup():
    print("\n --Module fixture initiated--")
    yield
    print("--Module fixture completed--")

@pytest.fixture(scope ="package",autouse=True)
def func_setup():
    print("\n --Package fixture initiated--")
    yield
    print("--Package fixture completed--")

@pytest.fixture(scope ="session",autouse=True)
def func_setup():
    print("\n --Session fixture initiated--")
    yield
    print("--Session fixture completed--")


def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50

def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60

def test_division():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8

def test_subtraction():
    m = 500
    n = 200
    assert m -n == 300


def greeting():
    print("Good Morning")