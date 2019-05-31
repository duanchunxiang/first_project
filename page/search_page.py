from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    button = By.ID, 'android:id/search_src_text'
    back = By.XPATH, '//*[@content-desc="收起"]'

    def input_search(self, value):
        self.input(self.button, value)

    def click_back(self):
        self.click(self.back)
