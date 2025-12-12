import pytest

@pytest.mark.smoke
def test_add():
    a = 25
    b = 35
    assert a+b == 60

@pytest.mark.sanity
def test_minus():
    x = 40
    y = 20
    assert x-y == 20

@pytest.mark.regression
def test_multiply():
    m = 5
    n = 8
    assert m*n == 40
@pytest.mark.adhoc
def test_divide():
    p = 10
    h = 5
    assert p//h == 3

@pytest.mark.smoke
def test_add1():
    a = 25
    b = 35
    assert a+b == 60

@pytest.mark.sanity
@pytest.mark.smoke
def test_minus1():
    x = 40
    y = 20
    assert x-y == 20

@pytest.mark.regression
def test_multiply1():
    m = 5
    n = 8
    assert m*n == 40

@pytest.mark.adhoc
def test_divide1():
    p = 10
    h = 5
    assert p//h == 2

@pytest.mark.smoke
def test_add2():
    a = 25
    b = 25
    assert a+b == 50

@pytest.mark.sanity
def test_minus2():
    x = 20
    y = 20
    assert x-y == 00

@pytest.mark.regression
def test_multiply2():
    m = 10
    n = 8
    assert m*n == 40

@pytest.mark.adhoc
def test_divide2():
    p = 15
    h = 3
    assert p//h == 5

