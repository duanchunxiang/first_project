from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileNetworkPage(BaseAction):

    # 首选网络类型
    first_network_button = By.XPATH, "//*[@text='首选网络类型']"

    # 2g
    network_2g_button = By.XPATH, "//*[@text='2G']"

    # 3g
    network_3g_button = By.XPATH, "//*[@text='3G']"

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)
