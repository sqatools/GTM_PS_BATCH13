import pytest

@pytest.mark.smoke
def test_addition():
    n1 = 20
    n2 = 30
    assert n1 + n2 == 50

@pytest.mark.sanity
def test_subtraction():
    n1 = 20
    n2 = 30
    assert n2 - n1 == 10

@pytest.mark.regression
def test_multiplication():
    n1 = 20
    n2 = 30
    assert n1 * n2 == 600

@pytest.mark.smoke
@pytest.mark.regression
def test_division():
    n1 = 20
    n2 = 10
    assert n1 / n2 == 2

@pytest.mark.sanity
@pytest.mark.regression
def greet():
    print("Hello, Good Morning!")