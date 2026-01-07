import pytest

@pytest.mark.smoke
def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50

@pytest.mark.smoke
def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60

@pytest.mark.smoke
def test_division():
    v1 = 30
    v2 = 6
    assert v1//v2 == 5

@pytest.mark.smoke
@pytest.mark.sanity
def test_subtraction():
    m = 500
    n = 200
    assert m -n == 300

@pytest.mark.sanity
def test_addition_1():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50

@pytest.mark.sanity
def test_multiplication_2():
    x = 3
    y = 20
    assert x*y == 60

@pytest.mark.sanity
@pytest.mark.regression
def test_division_3():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8

@pytest.mark.regression
@pytest.mark.sanity
def test_subtraction_4():
    m = 500
    n = 200
    assert m -n == 300