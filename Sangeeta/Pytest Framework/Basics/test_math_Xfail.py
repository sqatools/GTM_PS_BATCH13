import pytest

ENV ='prod'

def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50

def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60

@pytest.mark.Xfail(ENV == 'prod', reason = 'Cannot execute in prod')
def test_division():
    v1 = 32
    v2 = 4
    assert v1//v2 == 9

def test_subtraction():
    m = 500
    n = 200
    assert m -n == 300

def test_greeting():
    print("Good Morning")