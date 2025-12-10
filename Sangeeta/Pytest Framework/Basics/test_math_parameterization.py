import pytest

@pytest.mark.parametrize("name,age",[('ShreeNidhi',20),
                                     ('Abhimanyu',15),
                                     ('Demi',22),
                                     ('Debbie', 25)])
def guest_info(name,age):
    print(name,age)