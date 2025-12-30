"""
pip install pytest
"""
import pytest

ENV = "PROD"

def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50
@pytest.mark.skip  # unconditional skip

def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60

@pytest.mark.skipif(ENV == "PROD", reason="can not execute on prod environment")
def test_division():
    v1 = 30
    v2 = 4
    assert v1/v2 == 8

def test_subtraction():
    m = 500
    n = 200
    assert m-n == 300

def test_greeting():
    print("Good Morning")




