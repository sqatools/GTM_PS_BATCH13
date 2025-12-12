import pytest
from data_file import *

@pytest.mark.parametrize("username, password",
                         [('user1', 'user@123'),
                          ('user2', 'pass@123'),
                          ('user3', 'user@1234'),
                          ('user4', 'admin@123')])
def test_login(username, password):
    print(username,  password)



@pytest.mark.parametrize("username, password", input_list)
def test_register(username, password):
    print(username,  password)