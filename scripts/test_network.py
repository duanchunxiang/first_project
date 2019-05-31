from base.base_driver import init_driver
from page.page import Page


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_2g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_2g()

    def test_3g(self):
        self.page.setting.click_more()
        self.page.more.click_mobile_network()
        self.page.mobile_network.click_first_network()
        self.page.mobile_network.click_3g()
