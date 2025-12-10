import pytest

class TestMathoperation:
    def test_Addition(self):
        a = 20
        b = 30
        assert a + b == 50

    def test_Subtraction(self,func_setup):
        n1 = 50
        n2 = 20
        assert n1 - n2 == 20

#here from conftest directly it will take pre-request

#here I define in substraction test case their only it will get apply
'''
Test_math_operation_fixture.py::TestMathoperation::test_Addition PASSED
Test_math_operation_fixture.py::TestMathoperation::test_Subtraction 
 ---Launch URL : https://www.google.com  ---- 
FAILED
-- closing browser ----
'''

#if we keep autuse = True apply for both test case
'''
Test_math_operation_fixture.py::TestMathoperation::test_Addition 
 ---Launch URL : https://www.google.com  ---- 
PASSED
-- closing browser ----

Test_math_operation_fixture.py::TestMathoperation::test_Subtraction 
 ---Launch URL : https://www.google.com  ---- 
FAILED
-- closing browser ----

'''