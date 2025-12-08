import pytest

@pytest.mark.sanity
def test_Addition():
    a = 10
    b = 20
    assert a + b == 30

@pytest.mark.Regression
def test_subtraction():
    c = 100
    d = 35
    assert c - d == 20
@pytest.mark.smoke
def test_multiplication():
    a = 25
    b = 5
    assert a * b == 125

@pytest.mark.Regression
@pytest.mark.smoke
def test_division():
    n1 = 25
    n2 = 125
    assert n1 / n2 == 5