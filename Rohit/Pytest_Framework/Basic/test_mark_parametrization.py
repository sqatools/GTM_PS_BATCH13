import pytest
from data_file import *

@pytest.mark.parametrize("username,password",
                         [('user1','user@123'),
                         ('admin','admin@123'),
                         ('rohit','rohit@123'),
                         ('karad','karad@123')])
def test_login(username,password):

    print(username,password)

#python -m pytest -v -s .\test_mark_parametrization.py    -s--> for Print


@pytest.mark.parametrize("username,password", input_list)
def test_registrer_user_page(username,password):

    print(username,password)