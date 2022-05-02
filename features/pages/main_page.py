import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from features.pages.base_page import Page


def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(expected, real)

class MainPage(Page):
    MYTAB = (By.XPATH, "//android.widget.TextView[@text = 'MY']" )

    def move_to_mytab(self):
        time.sleep(5)
        self.tap_element(self.MYTAB)
        time.sleep(5)