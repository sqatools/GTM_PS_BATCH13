import pytest
from ...page_objects.dynamic_data.market_page_class import MarketPage
from ...page_objects.dynamic_data.market_page_data import *


@pytest.mark.usefixtures("get_driver_with_headless")
class TestMarketData:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.mp = MarketPage(self.driver)

    def test_read_market_turnover_row_value(self):
        self.mp.launch_nse_website(url=market_url)
        data = self.mp.get_market_turnover_value(row_num=2)
        assert len(data) == 5
        self.mp.log.info(f"market turnover first row: {data}")
