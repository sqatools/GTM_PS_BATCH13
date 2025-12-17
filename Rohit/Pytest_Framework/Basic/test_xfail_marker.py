import pytest

ENV = "prod"


def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 504

@pytest.mark.xfail(ENV=="prod", reason="test case failed due to environment #JIRA 3452")
def test_multiplication():
    x = 3
    y = 20
    assert x*y == 61


def test_division():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8

@pytest.mark.xfail(ENV=="prod", reason="test case failed due to funcationality broker with #JIRA-6789 ")
def test_subtraction():
    m = 500
    n = 200
    assert m -n == 300


def test_greeting():
    print("Good Morning")


@pytest.mark.xfail(ENV=="prod", reason="Test case due to CBS queue 1080 down")
def test_addition_f1():
    n1 = 20
    n2 = 30
    assert n1+n2 == 40

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