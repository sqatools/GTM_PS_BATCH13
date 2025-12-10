"""
pip install pytest
"""

class TestMath:

    def test_addition(self):
        n1 = 20
        n2 = 30
        assert n1+n2 == 50

    def test_multiplication(self):
        x = 3
        y = 20
        assert x*y == 60

    def test_division(self):
        v1 = 30
        v2 = 4
        assert v1//v2 == 8

    def test_subtraction(self):
        m = 500
        n = 200
        assert m -n == 300


    def test_greeting(self):
        print("Good Morning")