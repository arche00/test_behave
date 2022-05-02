import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.base_page import Page

class SettingPage(Page):
    SIGNOUT_BTN = (By.XPATH, "//android.widget.TextView[@text = '로그아웃']" )
    SETTING_BTN = (By.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView")

    def sign_out(self):
        self.swipe_to_down(self)
        time.sleep(5)
        self.swipe_to_down(self)
        time.sleep(5)
        self.click_on_element(self.SIGNOUT_BTN)
        time.sleep(5)

    def move_to_setting(self):
        time.sleep(5)
        self.click_on_element(self.SETTING_BTN)
        time.sleep(5)
