import pytest
from selenium import webdriver
from ..utilities.db_utils import DBUtils

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    DBUtils.create_branch_table()