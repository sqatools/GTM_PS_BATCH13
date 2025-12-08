"""
pip install pytest
"""
import pytest

@pytest.mark.somek
def test_addition():
    n1 = 20
    n2 = 30
    assert n1 + n2 ==50

@pytest.mark.smoke
def test_multiplication():
    x = 3
    y = 20
    assert x*y ==60

@pytest.mark.somek
def test_division():
    v1 = 30
    v2 = 4
    assert v1 / v2 ==8

@pytest.mark.somek
@pytest.mark.sanity
def test_subtraction():
    n1 = 500
    n2 = 200
    assert n1 - n2 ==300

@pytest.mark.sanity
def test_addition_1():
    n1 = 20
    n2 = 30
    assert n1 + n2 ==50

@pytest.mark.sanity
def test_multiplication_1():
    x = 3
    y = 20
    assert x*y ==60

@pytest.mark.sanity
def test_division_1():
    v1 = 30
    v2 = 4
    assert v1 / v2 ==8

@pytest.mark.sanity
def test_subtraction_2():
    n1 = 500
    n2 = 200
    assert n1 - n2 ==300










