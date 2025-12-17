"""
pip install pytest
"""
import pytest

ENV = "prod"

@pytest.mark.xfail(
    ENV == "prod",
    reason="Test cases failed due environment #JIRA-345"
)
def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 504

def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60

@pytest.mark.xfail(
    reason="Test cases fail due functionality is broker with #JIRA-3457"
)
def test_division():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8

def test_subtraction():
    m = 500
    n = 200
    assert m -n == 300


def test_greeting():
    print("Good Morning")


@pytest.mark.xfail(
    reason="Test cases fail due functionality is broker with #JIRA-3456"
)
def test_addition_f1():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50

def test_multiplication_f2():
    x = 3
    y = 20
    assert x*y == 60

def test_division_f3():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8

def test_subtraction_f4():
    m = 500
    n = 200
    assert m -n == 400


def test_greeting_f5():
    print("Good Morning")
    