import pytest
from list1 import *

#@pytest.mark.parametrize("username,password",
                         #[("joe1","pwd123"),
                          #("joe2","pwd234")])
@pytest.mark.parametrize("username,password", input_list)

def test_login(username,password):
    print("username:",username,"password:",password)
