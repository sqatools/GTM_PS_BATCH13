import pytest
from Nse_Page import MarketPage
from Nse_data import *


@pytest.mark.usefixtures("get_driver")
class TestMarketdata:

        @pytest.fixture(scope="function", autouse=True)
        def setup(self):
            self.mp = MarketPage(self.driver)

        def test_read_market_turnover_row_value(self):
            print("Launching NSE website")
            self.mp.launch_nse_website(url=Market_url)

            print("Reading market turnover row")
            data = self.mp.get_market_turnover_value(row_num=2)

            print("Data received:", data)
            assert len(data) > 0
